---
title: "Trying Devin"
date: 2025-01-08
categories: 
  - "misc"
image: "thumbnails/devin.png"
description: "trying a trendy agent product to much disappointment"
---

NB: WIP

We got a Devin subscription to play with. Hamel has his thoughts here (TODO link when out) but I wanted to record my own take too. TL;DR: the only tasks it seems to be able to do are those small enough and well-specified enough that I could do them myself, faster and better. It feels overly complex as a system. The only real benefit I can see is to people working on common things or not wanting to worry about setting up their environments etc. The magical promise is there, but not yet delivered.

## Introduction

Devin is billed as "the first AI software engineer". It costs $500 to get 'him' on your team. You assign Devin tasks and it heads off and works on them, giving you updates, asking clarifying questions, and theoretically behaving like a fast and competent intern. At least, that's the promise.

In practice, a lot of people I know who tried it found it underwhelming - despite the hype around it when it launched, we struggled to get it to complete even fairly 'simple' tasks.

## Representative Examples

Copying in a few notes from my test notes:

- I want a ‘view counter’ thing that works as follows:
    - It’s a flask app running on my server at some URL
    - I dump a link like `![](https://serverurl/viewcounter/mypage.png` and it returns a tiny image with the text ‘mypage has been viewed 1823 times’ (any request increments the count)
    - It keeps a count for any unique page names. (In an sqlite DB)
    - it has an admin page `serverurl/vc_admin` that shows the counts for all pages tracked
    - Need to handle any nuance around caching if that comes up (but I don’t mind if it’s more a unique visitor count)
    - Notes
        - Claude did it well, with a few errors that were quickly resolved. I got it working with claude while waiting for a first attempt from Devin
        - Devin eventually kinda got there, a lot slower and I felt like a mostly-helpless spectator. Frustrating, but if I was scared of code maybe better?
        - This feels emblematic. The kids of tasks Devin can do are the ones small enough and well-specced enough that I can do them faster with claude. Larger tasks I suspect it’ll fail. So then what’s the benefit of Devin? I now have it running on a machine I can’t see or interact with as well? Using a lot more tokens to talk to itself? Meh.

- Create an app (website) that lets you hover over countries to see their 'true size' compared to the mercator projection version. Have an option to toggle on stats (land area, population). Include a short intro above the map and a longer explanation below with links to learn more.
    - Llama coder: can’t use external libs or something?
    - Devin: says it’s done, offers to deploy. Send me several links to a page with the main component (the map) blank. “This is an initial version that I'll now begin testing and improving. “. After 17 minutes it has a map showing, but no resizing. After 40 minutes it insisted it had fixed the issues but sent an identically non-functional app.

I did a few more tasks. Super small and easily-verifiable ones were OK (e.g. 'make a standalone viewer for this shader [gsl_code]' or 'find and plot this data') but most were frustrating. My colleagues tended to bounce rapidly after it got stuck a few times.  

## The Good

Kicking off tasks in Slack, getting notified when it needs input (e.g. API keys, a go-ahead to deploy), having it able to test code by running it or even browsing to a page.

Also, Hamel found that even though the code was mostly unuseable, seeing the robot *almost* do something was often motivation for him to see that the task is possible, at which point he'd do it himself with Devin's attempt as a reference or a how-not-to-do-it depending on how close it got. So that's a plus too I guess.

## The Bad

Opaque when there are errors, hallucinating functionality, slow, overly complex. ANd it takes ages!

## Coding can be better

I feel kinda bad hating on this so much. I'm sure for many this is revelatory! But I'm spoilt, and I think at least for experienced coders there are much better ways. Starting with just coding youself but using powerful LLMs for first drafts or as helpers, moving up to more iterative, interactive coding (like what we're doing with solveit) or just co-creating in a simpler + more transparent tool like code interpreter or Claude artifacts.

## Awaiting better agents

A colleague talked about the 'time an AI is worth waiting for'. o1 pro, when he's doing complicated stuff in C or whatever, is worth waiting a few minutes for. Devin, IMO, is not. But future agents powered by better models might make good the promise of being useful for many minutes or even hours. I look forward to that day :)