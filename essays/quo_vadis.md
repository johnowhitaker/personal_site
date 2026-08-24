---
title: Quo Vadis?
date: 2026-08-24
categories: 
    - essays
description: "What should I work on next? Assorted musings"
---

I took the summer off as a sabbatical from answer.ai, to travel with my wife, tinker with some side-projects, and spend some thinking through what I want to do in what feels like a particularly pivotal time. I've decided not to return to answer, but am still unsure about how to choose between my remaining options. This essay is for me, to consider them all in one place, and for everyone else who has been asking me what I'm going to do now :)

(DRAFT, WIP, IGNORE FOR NOW)

## Why Now?

![Measures like the Epoch Capabilities Index track the continued improvement of models (source: https://epoch.ai/eci)](eci_plot.png)

- AI is getting v. good
- Software skills may have a limited remaining shelf life
- I want to step back and see if I'm in the best spot to contribute vs doing work that will happen anyway

## Factors To Consider

- Do I enjoy it (e.g. I like teaching)
- Does it have lasting value (e.g. teaching some specific tech << teaching some general principle)
- Does it have +ve impact (I want to do good)
- Are other people doing it? (I prefer less populous areas of the map)
- Does it pay? (I've historically skewed unprofitable-but-fun, now worry about financial footing given how many of the skills I have might tank in value as they get automated)

## 1) Back To The Mines (AI Research)

Lots of effort and capital is flowing into AI research right now. Many things feel 'overdetermined' - that is, they're going to happen pretty much regardless of what I or any other individual chooses to work on. That said, even if you think AI research is on track to be fully automated in the next few years, you can't look at the **current** state of things and not see that there is still LOTS of work to do:

![There is plenty of room for careful work still - most things are still piles of hacks with lots of space for improvement!](jack_bugfinding.png)

I'm a little rusty on model training, but I have > a decade of experience at this point, and am sure I could find ways to contribute. There are organizations working to build AI that benefits people, doing hard + interesting technical work, that pay decently. I'm not sure the day-to-day of begging codex to fix distributed training code would be my *favourite* thing to do, especially if I don't have a compelling reason to want the result NOW (vs a little later, without me having to lift a finger). Still, I'm chatting to a few people who may convince me that their org is doing cool enough stuff that I'm compelled to chip in and help it along :)

## 2) Frontier?

- Probably not, unless alignment or application like bio.

## 3) Bio?

- Slow and expensive
- Possibility (e.g. ML 2014) to bring it to many more people
- ...and build on models getting better, cheaper synthesis etc in the future
- got some ideas...
- but not quite yet. Can't afford to pursue myself, but can keep on side jic (or beg for funding as a startup)

## 4) 'Poke The World With Science' course

- Didn't want to do a course
- But came up with an idea I would be OK charging for, that I love
- Participants get a kit of science stuff each [time period] and some lessons on a few things, then self-directed exploration using those principles to take stuff further and build up a tech tree for themselves over time
- more on this soon possibly

## Shorter-Term Projects

- Hardware Hacking Evals
- Portland DIYBio scene
- Electronics Kickstarter

## Why Not Answer.AI

- TODO copy fro rough notes below

## You Tell Me!


## What Is AAI Up To?

Jeremy has been trying to convince people to use his better way of developing software (nbdev, literate programming etc) for years. People are resistant to change, but AI agents can be instructed to code however we want! So, at the moment aai is focused on building out their own parallel ecosystem / meta-harness / ?? to help the models work with them 'the answerai way', including:
- Custom replacements for the normal harness tools, with python & some custom sandboxing, including lots of extra tricks for efficient editing etc
- A custom markdown/html subset, and integrations of this with llms.txt etc (also used a lot for legal doc work with Virgil)
- Custom tools for working with solveit dialogs (jupyter notebook style interactive code artifacts)
- A custom skills system based on python modules
- Custom terminal ipython-like tools
- Customizations for existing harnesses using an 'llm dojo' to have the models train 'katas' via injected fake chat histories, so that they learn how to use all the cool answerai tools

Their thesis is that by building the model better tools and teaching it to use better software development practices, they'll be able to do more. Sounds sensible! Hacking around on these tools with some friends, while occasionally using them to make something useful for the lawers, isn't a bad way to spend ones time :)

## Do I want to go back there?

For me (and I stress that this is personal perception) I feel that:

- A lot of the gains from harness-fiddling could be equally realized by waiting a model generation
- Given the pace of change, spending so long on the substrate+tooling to later build might not have much of advanatge over, just, starting to build with the tools as they are and adapting with them as they evolve and improve
- My personal threshold for how much I want to care about converting from a custom mdhtml format to MSWord's templated XML is... very low :shrug:
- It turns out I don't like maintaining and building on a vast + growing library of interconnected pieces. Cool to see, but keeping on top of rapid changes, fitting things into the larger whole, constant refactors and redesigns stressed me out rather than being fun. AAI has 540 repos and growing (Jeremy does >1k commits across >100 repos per month, not sure how!). There would probably be ways I could find my own niche working on more exploratory stuff that didn't require such tight integration though.

I'm glad solveit is now available (if not marketed yet) - but sad it took so long. It feels like the ideal tool for careful work with the AI of 2024, a great learning tool for people learning code with the AI of 2025, and a quirky niche tool for exploratory 'old-school' coding in 2026, aka 'the year agents actually got good'. Of course, it has more and more agentic features added in - but after living in Codex for a few months I'm more convinced than ever that the future of coding is likely not carefully typing + inspecting a few lines of code at a time.

A new iteration of the solveit course could be exciting, although I have no clue what/how I'd like to teach and think I might be resistant to pushing e.g. answerai's current stack on newbies.



- https://openai.com/index/ten-advances-in-mathematics/ and similar every day
- Fun to spectate vs react
- Coding is ~solved for a lot of my tinkering, it is a glorious time to be a gentleman scientist
- I am worried about pay and going to be a dad
- I am uninspired by writing software
- I am excited to see new applications of ~free software
- Bio is interesting but lacks goals + is expensive and slow
- Electronics is delightfully easy now but AI is looming at the door (where software was a few years ago - needing supervision, good for automating some boilerplate/hard bits, decent only in well-covered parts of the training data, amusingly spiky on things like routing that require spatial understanding, going to go with well-known parts the way early models loved react)
- 



I simultaneously feel 
1) there is still so much work to do improving the giant pile of hacks that is the current state of AI software, and 
2) coding is ~on track to be 'solved', such that hard work now feels almost redundant compared to just waiting a bit. I'm glad people like Jack are burning the tokens to do stuff now of course, ditto all the security research being done under glasswing et al. But back in the day writing code felt like making something that would otherwise not exist, whereas now at best it feels like instantiating an idea slightly earlier than it would otherwise happen?? Or something??





Something physical would be cool. One of the few reasons I'd consider moving. Making manufacturing accessible to all @ sendcutsend or building air-to-methane with terraform or solving some genuinely useful robotics problem... 