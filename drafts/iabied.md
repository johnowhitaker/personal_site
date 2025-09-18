---
title: If Anyone Builds It, Does Everyone Die?
date: 2025-09-17
categories: 
    - essays
---

I've just finished IABIED. I think it's well-written, and will reach lots of people with the ideas that Eliezer and co have been worried about for decades, ideas which are suddenly feeling a lot more pressing in light of the rapid AI advances of today. My father-in-law David also pre-ordered it, and his reaction is, predictably, a fair bit of hopelessness. Corporations are racing ahead chasing the money, that's doesn't seem like it's going to stop. The book's only recommendations are to shut down, with threat of nuclear bombs, any un-monitored GPU cluser with >8 GPUs and ban new AI research. This seems unlikely to happen. What can we do? David's youngest son is expecting, and talked yesterday about a 529 college savings plan. "What can I say to him? Like you can't say this to a young father-to-be but there's no way his kid is going to go to college!". This essay is my attempt at some sense-making.

## A Quick Summary of the Book

Part 1:

1) Humans do well at intelligence (steering and predicting) which gives us immense power
2) LLMs and other AIs are 'grown not crafted'
3) Training for an objective leads to acting like you 'want' something - e.g. chess AI 'wants' to protect its queen
4) Optimising to an objective can lead to weird 'wants' - e.g. peacock feathers, non-reproductive sex in the case of evolution. 
5) An ASI's "wants" are likely to be extremely weird and not good for humans
6) We'd lose in a fight against ASI that wanted something different to us

Part 2: One specific, fictional example, to help people kinda maybe visualize how something bad could go down, without just waving hands at "some magic-like super-smart thing we don't understand hits us out of left field". There are lots of other tales in this genre.

Part 3: There are lots of things that make this problem very hard: we only get one try, takeoff might happen fast, this is a relatively new science (he compares it to alchemy), people are racing towards it anyway, believing it's better they try first, people are afraid to be alarmist, it would take pretty drastic measures to stop it.

The book is well-written, and a lot of the steps in the argument are hard to argue with. They clearly took great care to communicate things like reasoning model training in a way that is mostly accessible to non-tech folks. 

## So Are We Doomed?

There are a few key claims in the book where I find room for more hope than the authors:

- We don't know anything about what is happening inside these networks
- The 'wants' that result from AI training will almost certainly be completely alien and extremely unlikely to be good for humans
- We are building towards ASI of the kind he describes

## What Are They Thinking?

Clearly we're a ways from full understanding, but I think they undersell the interpretability field - we're making great strides, and so far seem to be quite lucky in terms of how far even 'simple' techniques like linear probes can go in terms of understanding behaviours or finding worrying patterns. There are some deep laws of intelligence lurking, pockets of computational reducibility that we can exploit for understanding, as Wolfram might say.

Plus chain of thought monitoring

Plus narrow AI helping with interpretability (and the agency vs oracle debate more generally - we can choose to build tool AI not super-agentic AGI)

## What Do They Want

Pre-training on the internet stacks the odds in our favour, compared to ASI emerging from game-play or physics experiments. We're initializing them with a fantastic prior of human values, based on this giant corpus. They don't have to learn how to be nice from scratch, by following some fragile list of wishes like an evil sorcerers lamp. They can just bootstrap off the 'nice assistant' prior implicit in trillions of tokens of human data. 

Backed up by 'goodness vectors', emergent misalignment (actually hopeful research), Hurt by RL

## What Are We Building?

We don't all want long-running indepenant agents... Agency is the danger. -> YB. Training looks like deployment, no long-term memory or coherent single identity or schemeing just yet, and no reason not to keep it that way (well... too stong to say that I guess).