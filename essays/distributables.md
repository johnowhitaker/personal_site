---
title: "The Idea Is The Software"
date: 2026-02-23
categories:
    - "essays"
---

Here's a device that only does X. Here's a binary you can run that does X. Here's code that you can compile and run that does X. Here's an X SAAS. Here's a prompt that creates code that does X. "Did you know computers can do X?". [Half-baked musings on software incoming].

There's always been a gap between 'works on my machine' and software that other people can easily use. So, if I coded up something that worked for me, it was a bit of a burden to polish that into something that others can use. You need to solve for different operating systems, you can't have a hard-coded "~/johnos_projects" path, there are requirements... Plus there is some education you feel obligated to do, for potential users who might not know what `pip` is or something.

With LLMs getting good, new ideas around this are beginning to float about. What if we just shared, like, a really good prompt? Everyone could have their agent build their own bespoke version. Karpathy found a nice example of this being used as an extensibility mechanism for a project recently, where the repo includes prompts to tell LLMs how to add functionality:

> I also love their approach to configurability - it's not done via config files it's done via skills! For example, /add-telegram instructs your AI agent how to modify the actual code to integrate Telegram. I haven't come across this yet and it slightly blew my mind earlier today as a new, AI-enabled approach to preventing config mess and if-then-else monsters. Basically - the implied new meta is to write the most maximally forkable repo and then have skills that fork it into any desired more exotic configuration.

This weekend it really hit home to me how far this goes for some things: at the end of the day, all I need to share is that something is **possible** - the implementation is left as an exercise for the reader, but that is no longer a gatekeeping, elitist move! The specific example was my [quick and dirty strobe tachometer](https://johnowhitaker.dev/mini-hw-projects/tachometer.html). It's a microcontroller, that lets you pulse an LED at different rates. When the flash speed matches the rotation speed of something, it looks like it's standing still. Nothing fancy. Historically, if I wanted others to re-create this, I'd need to share:

- An exact parts list
- A wiring diagram
- The code
- Installation instructions (how to install the Arduino IDE, how to connect your device)
- Tips for connecting to the board (serial ports on Windows are a nightmare, for example)

And odds are, a reader who wanted to re-create it won't have the exact parts on hand. For e.g. the board I used is an ancient NodeMCU ESP8266 dev board from the hackerspace junk bin - but there is no reason to use that specifically.

Contrast to today. The thing I share is the **idea**: flash a light with a microcontroller to estimate speed. You can use a transistor to push more current through the LED if you want it bright. Ask your agent to use the arduino-cli to handle the programming etc.

I'm somewhat confident that many could replicate this project, and it won't matter if they use an STM32 or a Raspberry Pi Pico or an ESP32. It won't matter if they have the same display as me (I can't even remember the model number, and did not tell codex - it figured it out anyway!). If they have different transistors on hand, I'm confident the model can tell them how to wire them up. In other words, the "source code" for this project is simply the notion that one can do such a thing - and all the tedious embedded engineering work is just an implementation detail that can be handled by an LLM.

In some ways this is the 'LLMs are lossy compilers' take that has been around for ages, but the point of this essay is me coming to terms with this now that the scope of tasks for which they are ~reliable is growing. There are lots of apps I've built for myself that would be a pain to release, since I'd need payments to cover inference costs, bla bla bla. It is somewhat freeing to think that maybe sharing a screenshot of the core idea is enough!

Of course, we're still far from this working for all software. But it's interesting to think how far you could push this, especially with OS building blocks. "Combine ThreeJS with [this mapping lib] and [that data API] to visualize cycle traffic in your city". That's a lot easier and more fun to type in and run than those old magazine code listings :) The future is going to be interesting!

PS: It's worth thinking through how your medium of choice works for sharing these 'idea seeds'. I've got some fun plans in solveit for this - a jupyter notebook packaging up demo code + suggested prompts seems like a nice format for this. Still trying to convince myself this is needed vs a simple .md file or screenshot, but we'll see :)

PPS: What's the coolest piece of software you've seen that can be distributed in this way? (i.e. as a one-shot prompt). I'd love to see cool examples.