---
title: If Anyone Builds It, Does Everyone Die?
date: 2025-09-17
categories: 
    - essays
---

I've just finished IABIED. My father-in-law David also pre-ordered it, and his reaction is, predictably, a fair bit of hopelessness. Corporations are racing ahead chasing the money, that doesn't seem like it's going to stop. The book's only recommendations are to shut down, with threat of nuclear bombs, any un-monitored GPU cluster with >8 GPUs and ban new AI research. This seems unlikely to happen. What can we do? David's youngest son is expecting, and talked yesterday about a 529 college savings plan. "What can I say to him? Like you can't say this to a young father-to-be but there's no way his kid is going to go to college!". This essay is my attempt at some sense-making.

## A Quick Summary of the Book

Part 1:

- Humans do well at intelligence (steering and predicting) which gives us immense power
- LLMs and other AIs are 'grown not crafted'
- Training for an objective leads to acting like you 'want' something - e.g. chess AI 'wants' to protect its queen
- Optimizing to an objective can lead to weird 'wants' - e.g. peacock feathers, non-reproductive sex in the case of evolution. 
- An ASI's "wants" are likely to be extremely weird and not good for humans
- We'd lose in a fight against ASI that wanted something different to us

Part 2: One specific, fictional example, to help people visualize how a bad scenario could go down, without just waving hands at "some magic-like super-smart phenomenon we don't understand hits us out of left field". (review: There are other, better tales in this genre.)

Part 3: There are lots of pieces that make this problem very hard: we only get one try, takeoff might happen fast, this is a relatively new science (he compares it to alchemy), people are racing towards it anyway, believing it's better they try first, people are afraid to be alarmist, it would take pretty drastic measures to stop it.

I think it's well-written, and will reach lots of people with the ideas that Eliezer and co have been worried about for decades, ideas which are suddenly feeling a lot more pressing in light of the rapid AI advances of today. A lot of the steps in the argument are hard to argue with. They clearly took great care to communicate technical ideas like reasoning model training in a way that is mostly accessible to non-tech folks. 

## So Are We Doomed?

There are a few key claims in the book where I find room for more hope than the authors:

1) Interpretability: We don't know anything about what is happening inside these networks
2) Alignment: The 'wants' that result from AI training will almost certainly be completely alien and extremely unlikely to be good for humans
3) Technology: We are building towards ASI of the kind he describes

Let's dig into each of those one by one

## What Are They Thinking? (Interpretability)

Clearly we're a ways from full understanding, but I think they undersell the interpretability field - we're making great strides, and so far seem to be quite lucky in terms of how far even 'simple' techniques like linear probes can go in terms of understanding behaviours or finding worrying patterns. There are some deep laws of intelligence lurking - pockets of computational reducibility that we can exploit for understanding, as Wolfram might say.

As a bonus, reasoning models currently output their 'chain of thought' in ~English, and the labs are very aware that this is a fragile and beneficial state we shouldn't throw away. There's a [lot of agreement that this is worth preserving](https://arxiv.org/pdf/2507.11473), and a lot of work being done to ensure this remains a useful way to keep a window on these 'thinking' models to catch early signs of unwanted behaviour.

AI-assisted interpretability is also not nearly as doomed as they make out. The authors tend to treat intelligence as one singular, scalar value - a dumber model cannot hope to outwit a smarter model, and smarter models will be more dangerous. I disagree, and think (for example) we could build models focused on understanding what other models are 'reasoning' about, without needing to give the interpreter model any tools or agency.

## What Do They Want (Alignment)

Now onto alignment, which the authors frame as this near-impossible task. After all, we can't write down exactly what the 'human values' we want are, and even if we did, optimization towards those might instead lead to all sorts of warped and crazy actual 'wants', like a desire for smiles, which in turn might lead to engineering a smiling virus... If we were building these AIs from scratch, from some sort of self-assembling game-playing logic machines, which followed our specified rules like a malicious djinn following the letter of the wish in an old story, I'd agree we're in trouble.

But we're actually in a super lucky spot, thanks to how the tech is developing in practice. See, to get around the difficulty of carefully writing out the specific objective we want, it would be great if we could start the models out with some incredible, general distillation of human behaviours and values, some trove of interactions and information that gave them a more robust understanding of humans... something like the internet?

If you ask an LLM today "should I go camping in this park where there's a wildfire warning", the LLM will advise against it. This is not because the maker trained it to advise against hiking in wildfires, or because they carefully told it what to do in that situation. Instead, they trained it to advise against drinking bleach, and to recommend healthy habits, and to help out with programming and math problems. To get better at doing so, the LLM didn't have to start from scratch. Instead, it built on the rich features and concepts it learnt during pre-training, including the convenient shortcut ideas that make all the specific examples more likely: be helpful, be good. These bleed into other cases, giving us AI's that (in general) act 'good' in a huge number of situations.

This is great news! The model doesn't need to learn what good is from a list of rules, it can build on the priors introduced by trillions of tokens of human-written text. This is a far nicer situation than we could have hoped for! And not one the authors envisioned when they were dreaming of uncaring evil optimizers back in the 2000s.

This isn't to say that we get off easy. The trend is away from chatbots and more and more towards AI 'agents' that learn from reinforcement learning, not from human text. It's possible that doing more and more RL will push the models further from the base they learn in pre-training, and could lead to weirder and more scary objectives - indeed, we already see a little bit of this with so-called "reward hacking", where models are instructed to solve challenges fairly but learn over time that they can be rewarded for finding clever hacks to fool the tests they're being trained on. This is an active area of research.

There's also a worry here in terms of intentional mis-use. If a model understands good and bad, could someone train it to be bad intentionally? Alas, it seems so. In fact, training it to be bad in one area (e.g. writing insecure, hackable code) can [lead to a model that also acts racist and mean](https://arxiv.org/abs/2502.17424)! It might be almost as simple as flipping a plus sign to a minus sign deep in the model internals - something that will get more worrying as capabilities continue to advance.

## What Are We Building? (Technology now)

Building on the past two sections, the situation at present is nicer than the book would have us believe. Current systems are trained on human data, and have a more robust understanding of 'helpful', 'honest' and 'harmless' than early theorists could have hoped for. 

Furthermore, they're extremely incentivised to keep getting better in this regard. AI companies make money if their AI behaves well! Training involves taking in text and producing more text, and deployment looks the same. While some models have some 'situational awareness' to know when they're deployed, we can still: 

- inspect the text they're producing, including with other 'monitor' models that can detect early signs of bad behaviour
- pause the process at any time (the book uses lots of rhetoric about 10000X faster thinking to show danger, but current models have no way to know what speed they're going or if we're carefully inspecting their inner activations)
- catch signs of unintended behaviour in testing or early deployment, and roll back to earlier models if these are too bad (e.g. Grok's "MechaHitler" arc was rapidly cut short)

We're a far cry from the picture in the book's Part 2, where an AI entity schemes to itself for tens of thousands of GPU hours in inscrutable self-invented language, and then plans and executes it's evil plan over many instances of itself over many months.

People are actively working on safety in many different ways, and again labs have incentives to keep building systems that reliably do what we want. There's a lot of pressure against anything that develops 'misaligned' wants.

## What Will We Build Next

AI is being built by people, in corporations. Their motivations vary, but most are genuinely pursuing ways to add value: helping people do more, solving scientific challenges, creating more and more value for other corporations and society.

In one sense, there's a single direction we go from here: better. AI models will continue to do better and better on various objectives we set. But when you look closer, there are different paths we could take, determined by economic incentives and the choices of those leading the charge.

One dimension I wish we could tweak is the move towards more and more 'agentic' AI. This is something we care a lot about at my company - AI as human augmentation, with human driving, is an immensely useful and empowering tool. But too many view the real use as human replacement - a virtual employee you can delegate work to. Besides de-valuing humans, this is a direction that doesn't help the safety side! Yoshua Bengio prominently believes that pushing for non-agentic AI is key to maintaining safety as we push capabilities forward, and I agree.

We don't all want long-running indepenent agents... Agency is the danger. -> YB. Training looks like deployment, no long-term memory or coherent single identity or scheming just yet, and no reason not to keep it that way (well... too stong to say that I guess).

## Conclusions

I am much more hopeful than the authors that we will be able to keep solving problems and moving forward, building AI that helps humans do more, pushing back the frontiers of knowledge without destroying the world.

It's worth thinking carefully about the risks. It's good that people are thinking about policy that could slow down the chance of bad outcomes. I hope that concensus shifts away from the mad rush into agentic human replacements, and that we collectively spend some time dreaming about what types of future we'd like to usher in. I hope the 'race' dynamic doesn't cause megacorps to throw out some of their ideals.

I can't claim certainty. But I don't think everyone is going to die. Especially if we proceed carefully and push towards human-centered AI tools, and away from unchecked agency.

I have no idea what the future looks like. It probably involves a lot of change. But I hope this little brain-dump helps you keep a spark of hope that, just maybe, that kiddo will have a cooler college experience than any of us old cynics could dream of :)

### PS: Other Worries

This post focused on 'ASI' specifically, the focus of IABIED. There are other reasons to be concerned, some that come up if we do build powerful AI and some that stem from attempts to avoid that. The book mostly ignores these - fair, considering that if you believe the books titular conclusion then all of these are, by comparison, small fry. Still, including them here for completeness and reference until I decide to edit this out for brevity :)

If we try not to build it:

- Authoritarian surveillance state: The book advocates for extreme oversight measures, to ensure that nobody builds ASI. Implementing these would require extreme surveilance and power in the hands of the governments, which could lead to it's own bad outcomes. 

- Concentration of Power: Making (incredibly valuable and useful) AI something that only a few have direct control over is a recipe for concentration of power and wealth, leading to bad outcomes of a different kind

If we build it safely:

- Misuse: someone might still be able to transform safe, powerful AI into something harmful and unsafe, e.g. by re-training it to agentically pursue damaging cyberattacks or using it to design bioweapons

- Gradual disempowerment: if we become too dependant on AI, we might slowly lose our skills and bargaining power, leaving the bulk of the population with less hold on how they are treated and what their lives look like going forward.

- Misaligned incentives between corporations and humans, as is already happening with addictive scrolling content like tiktok, and which could get far worse as companies push 'relational' AI further while optimizing for engagement or profit.