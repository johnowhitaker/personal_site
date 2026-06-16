---
title: "Teaching Neural Cellular Automata To Play Games"
date: 2026-05-13
image: thumbnails/nca_game.png
description: "Playing Pong, Solving Mazes and Guessing At Pictionary using NCAs, with bonus vid using them to denoise/restore images"
categories:
    - "Video"
---

Some tiny experiments in pushing on what NCA can do, showing my own tiny experiments but also pointing at some resources and hopefully inspiring you to try some new ideas yourself :)

{{< video https://www.youtube.com/embed/0w_cVJoD2uk >}}

Markdown file with hopefully enough info for your coding agent of choice to get your own experiments going: https://gist.github.com/johnowhitaker/bf664eb56dfe50b05d5ef319a0364dae

Key references:

- https://wandb.ai/johnowhitaker/nca/reports/Fun-With-Neural-Cellular-Automata--VmlldzoyMDQ5Mjg0
- https://arxiv.org/abs/2111.13545
- https://distill.pub/2020/growing-ca/

Also, I did some content for fast.ai on NCAs hidden deep in [this video](https://youtu.be/PdNHkTLU2oQ?si=K0w67-4-yIgkD5KO&t=4479) - worth a look if you want more polished content from me on this stuff :)

A few days after that first video I also trained denoising NCAs, which were able to repair flower images somewhat plausibly! Very fun to play with. Video:

{{< video https://www.youtube.com/embed/sjAFcJBetuw >}}

PPS: Fable with a minimal prompt and the md file did a fantastic little project + writeup along similar lines to the first video, including some good explorations of info propagation speed factors and other clever little bits. Check out its writeup [here](https://johnowhitaker.github.io/fabNCA/) (code [here](https://github.com/johnowhitaker/fabNCA)). Hopefully we can do useful stuff with this model in the future if it ever comes back with more sensible safeguards :)