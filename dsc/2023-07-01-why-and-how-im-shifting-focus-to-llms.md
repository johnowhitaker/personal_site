---
title: "Why and how I'm shifting focus to LLMs"
date: "2023-07-01"
---

While I've previously consulted on NLP projects, in the past few years my research focus has been chiefly on images. If you had asked me a few months ago about looking at LLMs, my default response would have been "No way, I bet there are far too many people working on that hyped topic". But then my research buddies (a crew originally put together by Jeremy Howard to look into diffusion models) switched focus to LLMs, a friend started trying to convince me to join him in starting an LLM-focused company, and I began to re-think my hesitancy. In this blog post, I'll try to unpack why I'm now excited to shift focus to LLMs, despite my initial misgivings about moving into a crowded market. And then I'll try to outline how I've gone about loading up my brain with relevant research so that I can become a useful contributor in this space as quickly as possible. Here goes!

## Part 1: Why LLMs are exciting

The TL;DR of this section is that it turns out there is a lot of innovation happening in this space, and lots of low-hanging fruit available in terms of improvements to be made, all driven by open-source models and the influx of new ideas. For a while, it felt like you needed to be at a big org with tons of compute to research LLM stuff and that OpenAI was just too far ahead for most things. Here are some specific thoughts I wrote out the other day when someone asked what I found exciting:

The explosion of interest in LLMs has led to a flurry of innovations around them. In particular, there are some cool techniques around lower-resource training and inference that I'm excited to see:

\- **[Quantization methods](https://huggingface.co/blog/4bit-transformers-bitsandbytes) to reduce the VRAM required** to train and serve larger models

\- Things like [GGML](https://github.com/ggerganov/ggml) for **fast inference without any dependencies**, optimized for things like Apple hardware and consumer GPUs (see Modular for a direction in which inference gets easy and fast on lots of different hardware)

\- [**Parameter-efficient fine-tuning**](https://huggingface.co/blog/peft) **methods** that allow training with much less compute. It's tricky to fine-tune the smallest GPT-2 model (125M parameters) on Google Colab when not using any tricks, and yet there are notebooks for SFT on Falcon 7B that can be run happily on the free tier thanks to LoRA and 8-bit Adam.

The upshot of all this is that it's now doable to train variants of these fairly powerful open-source models with a single GPU in very little time and to share the resulting models (or the much smaller LoRA weights) through things like HuggingFace so that anyone can play with them. 

**I think the next direction where things will rapidly improve is datasets** for fine-tuning. We've already seen a big leap in quality over the past few months, with more and more chat / instruct datasets being curated. An obvious next step is using existing LLMs to generate better training data, and/or filter existing data. 

**The evaluation is lagging a little IMO**. The [open LLM leaderboard](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard) is a cool initiative, although it highlights how fragile these benchmarks can be. I'm excited about using LLMs to evaluate other LLMs (even though this can be precarious) and also hoping to see other alternatives emerge - perhaps something equivalent to the PickScore model that is a useful tool for evaluating image generators and is based on crowd-sourced ratings. Actual human ratings are still super important and hard to do well.

**Another fun dynamic is just the constant stream of better base models available for fine-tuning** as people compete to make ‘The BEST Truly Open Source Model’. Better base models mean better synthetic data, easier fine-tuning, more use-cases unlocked, more data as a result… it’s a nice flywheel of improvement. And since fine-tuning is getting faster and faster, when a great new base model comes out it won’t take long to apply the same dataset+training strategy as you’ve used on whatever current best model you have. 

It feels like all these things make it easier than ever to do cool stuff with LLMs, but also that there are a lot of improvements still on the table - a good time to dive in!

PS: Other interesting directions:

- Ways to use multiple models of different sizes to speed up inference for ‘easy’ completions without sacrificing accuracy

- Moving away from RLHF towards something more like Direct Policy Optimization where you still incorporate feedback but without the RL messiness

- I still think very few people have good recipes for fine-tuning models and getting to know a specific model/task well would likely yield some interesting insights

It's important to be able to iterate quickly for research to be effective, and when testing an idea meant training an LLM for weeks on tons of GPUs I was not excited. But now that we can potentially tune a good open-source base model on a single machine it seems like we might be close to rapid iterations especially if we just focus on the fine-tuning/alignment/tweaking steps or inference-time innovations. "LLMs are having their Stable Diffusion moment".

## Part 2: How the heck would you 'learn LLMs'?

I've been vaguely keeping up-to-date with the field for years - reading the big announcements and maybe skimming the odd paper here and there. But it had mostly been in a 'wow PaLM seems cool' style outsider mode, rather than taking in any details of architecture or training that might be needed to actually work with the darn things. So, step one: start catching up on all the cool tricks everyone knows, and seeing what gems are hidden in some lesser-known papers.

The secret sauce for this is our research group. Twice a week we meed at look through papers we find interesting. Often something recent sparks a specific line of inquiry. For example, there was some buzz on Twitter about the "[Textbooks are all you need](https://arxiv.org/abs/2306.11644)" paper that used synthetic data alongside heavy LLM-assisted filtering of existing training data to train very good small code models. This leads us to look into some prior work (e.g. the [TinyStories](https://arxiv.org/abs/2305.07759) paper by some of the same authors that tested similar ideas at a smaller scale) which in turn cites other papers which... Before you know it we have a [Zotero library with 300+ papers](https://www.zotero.org/groups/5004697/llms/library) and some ongoing experiments to start building our own intuition for some of the methods we found interesting.

Some specific things I find extremely powerful about this group-study approach:

- Teaching others about something is an extremely good way to learn it, especially if your audience consists of people who can come up with questions to probe deeper and expand your collective understanding

- More people => more chance for 'aha' moments where something suddenly clicks, which can then be explained back in a different way. It seems crazy, but we've bootstrapped our understanding of some extremely complex topics just by explaining an idea back and forth to each other in different ways until it really makes sense!

- More people => more perspectives with different experiences to draw from. Someone shares a paper on document retrieval, which sparks a memory of a cool contrastive method used in images, which reminds someone of a paper aligning code and language from a few years ago, which brings up a nice benchmark we could use to test our new ideas...

- Practical experiments are great learning tools. Having multiple people tinkering with things or sharing proof-of-concept implementations is another major boost to understanding something.

It's one thing to load up your brain with tons of papers and techniques, but that on its own isn't quite enough to make you useful. So, for me, the next step is getting into the weeds with some actual projects. Run some models, try to train a few on some different tasks, dive into some larger projects... A lot of what I've done in this phase isn't particularly new or interesting, but it builds the muscles for later stuff. If you're bold you could find a way to get paid for this as a consultant, since everyone wants 'talk to your docs' bots and such! I have yet to cave in to that particular temptation, but I \*AM\* writing a book with some chapters devoted to LLMs (with some amazing co-authors to catch any glaring mistakes I make) which I guess is also killing two birds with one stone in terms of learning while (eventually, hypothetically) earning... And soon I may be full-time at the aforementioned LLM-based startup at which point it stops being 'hacking around in my spare time' and turns into 'ML research' with a proper job title and everything :)

## Final Thoughts

This is a weird post, mostly me thinking out loud, but I hope you've found it interesting! I've gone from thinking LLMs are 'solved and saturated' to seeing all sorts of opportunities, and tons of ways someone with a novel perspective or a bit of luck can come in and contribute. So, wish me luck ;)
