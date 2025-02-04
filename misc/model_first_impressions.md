---
title: "First Impressions of Three New AI Models"
date: 2025-02-04
categories: 
  - "misc"
description: "Trying out Deepseek R1, o3-mini and OpenAI's Deep Research"
---
# First Impressions of Three New AI Models

## Summary

The rest of this post will have a few examples from my experimenting with some additional commentary, but first, here are my main initial impressions of these models:

- DeepSeek R1: A truly impressive model. Seems on par with the frontier w.r.t. coding and such, but they've also done well tuning the genearl tone. I'm not suprised some of my non-technical family members have switched! It's free, it shows some of the benefits of 'reasoning models', it can search, it doesn't write in a stiff and censored manner... what more could you want?
- o3-mini-high: Another impressive coding model. Maybe not as good as Claude for style/taste when coding web apps? Maybe a little stronger than Sonnet or R1 on harder code stuff? Between these two I think the space of what you can do with one-shot asks / vibe coding is pretty darn impressive.
- Deep Research: When it works, it's suuuper useful. This one feels like it will bring me lots of insights + learnings that I wouldn't otherwise get, and save a ton of time for people who's work involves a lot of this specific kind of research. Still some amusing failure cases, but I'm glad to add this to the toolbox. Edit: some early glitches are putting me off in some cases though, keep expectations in check.

All of these models are amazing technical achievements, and do genuinely push forward the bounds of what is possible. But I'm kinda sad that the direction everyone is pushing is so stringly 'get the AI to do the whole thing' rather than augmenting humans more. Sigh. Anyway, on to some specific examples.

## Deep Research

**Prompt: Vitamin C crystals look cool in polarized light microscopy. I want you to come up with a way to use this to create art. Do a deep dive on what causes the colors, and how to begin to steer the process. Focus on quality sources + papers. Suggest experiments (they should be home-lab accessible) on different ways to control the appearance of what is grown. Give me a paintbrush the world hasn't seen before!**

The [result](https://gist.github.com/johnowhitaker/74680dc5a1bda4affa3ad4fabafa4ec2) had a ton of info, giving me terms for thigns I'd seen but not researched and suggesting some good experiments I'm planning to try. There was also one key idea not in any of the references that I *think* will work great! I did notice that a *lot* of the info came from one amazing blog post - it was nice to see this based on the references and just go read that directly. Verdict: a good start!

**Prompt (from a relative not used to AI): I want a List of top 20 Cities in the US for investing in single family home rentals ranked by the following criteria. 1. Business friendly state where laws favor landlord and evictions are easy, 2. Growing population, 3. Business growth, 4. Affordable house prices. 5. Strong rent to house value ratio. Create a 5 point scale for each of these criteria that allow them to be quantitatively evaluated. Eg. For criterion 1, a score of 1 might be least business friendly and 5 would be most business friendly. Give specific criteria for each rank in each scale (eg. A ranking of   1 for criteria 1 means x and a ranking of 2 for criterion 1 means y etc).**

Unlike other chat systems that can't even attempt this, deep research was able to go off and run through tons of sources finding populations, stats etc. It came back with a list of 20 cities with notable features of each, and a table when asked in a follow-on. Hard to verify, but closer to what he wanted than anything else could give. It was an interesting chat: "shouldn't this kind of thing [repetitive assessment of lots of cities in parallel] be perfect for AI?" - for now at least such things would work best with some custom code - e.g. I could come up with a scorecard and then in parallel run 500 research 'agents' with one city to research each. To him, it was obvious the AI should just do this! And I guess deep research gets a little closer via a loooong search and reasoning trajectory.

Verdict: not bad, also eye opening to see an ask from someone not thinking as much about what might suit this type of system.

**Prompt: I recently ran into the map folding problem. I really want to add the next number in the sequence but my code (https://github.com/johnowhitaker/map_folding/blob/main/README.md) is too slow. This needs a new approach. Please see if you can come up with a way to efficiently leverage GPU compute to solve this problem efficiently. Check your ideas with the smaller numbers in the sequence if you can write and run code. Please give this your best go. Good luck!**

![The completely hallucinated conclusion of its work](thumbnails/dr_conc.png)

This was hilarious. It first wrote a nice long report outlining the problem, then when pressed for an implementation I got another long report talking about all the successful (!) experiments we'd run using the code it wrote, when in actuality said code was buggy and missing key implementation details. Most amusingly, the citations were all from my own past journey down this rabbit hole! **Verdict: major fail**. Perhaps they steer it away from using code much, and it is better suited to finding existing answers than coming up with something novel.

**Prompt: Create a nice, approachable blog post based on this paper: https://arxiv.org/abs/2501.19393
Include images if you can, and links to related work. I want something easier for semi-technical people to consume than the paper.**

Result: meh, an OK post, with things like `(Imagine an infographic here comparing 60k vs 1k training examples, showing a small stack of gold-standard problems outweighing a mountain of average ones.)` instead of actual images.

**Update:** A few more attempts this morning led to complete fails. Like saying it'll generate figures and then simply describing what they might look like, or acting like it was starting a job (" I'll let you know when it's ready!") and then just doing nothing. Each glitch makes me feel less like wanting to try more things - fastest hype-to-disappointment arc I've had with a model in a while.


## O3-MINI

[Thread with pics](https://x.com/johnowhitaker/status/1885515560689295826)

1) Facewave
A fairly complex ask. Made one small mistake on the OpenPIPE API but corrected in the first follow-up message. Could use some visual tweaks but it works (apart from drawing the points wrong)! Control midi with your webcam :)
App: https://tools.johnowhitaker.com/facewave_o3
Code: https://github.com/johnowhitaker/utils/tree/main/static_apps/facewave_o3
Verdict: Impressive start, not bad for 2 minutes

2) "I want you to make a p5 sketch I can paste into https://editor.p5js.org that draws a beetle. It should draw a different beetle each time it is run (use a random seed) to reflect the amazing diversity of life. Make it as good-looking as you can."
o3-mini (left) compared to me years ago (right)
Code: https://editor.p5js.org/johnowhitaker/sketches/Oj6Okn8rN
Verdict: runs first time, good variations, darn impressive! Quirky bugs but dang they're obviously bugs!

3) Shader: "Make me a shader toy opalescent nudibranch. I want code I can paste in that depicts these incredible creatures in a stunning way."
First attempt I had to fix some code issues and then got a blob. 'Make it cooler' made some improvements. changing to -high (used in prev 2) was better especially in motion.
Code: https://shadertoy.com/view/XXGBR3
Verdict: shaders are hard, meh results and maybe stuck on an older version of what shadertoy wants? (needs a more recent knowledge cutoff!) but hey I still got something with minimal fixing.

4) Synth: "I want a web page that is a synthesizer. I needs cool visuals of the sound, keyboard (AWSEDFT... keys mapped to piano notes) to play notes and should accept 2 midi CC codes using webmidi to modulate the sound. Make it epic - no simple sine waves and bland visuals, get really creative."
OK impressive, it works! Keys play sounds, having facewave open in another tab (with loopMIDI running) modulates filters/sound quality somehow. Not bad for first try, this thing is pretty good at zero-shot software making!

5) A nice enabling utility for today's Saturday making: an SVG-to-GCODE tool for a hanging pen plotter. Got it first time (I made a couple of easy tweaks).
Prompt: "I want you to make an SVG-to-GCODE tool for a hanging pen plotter. The user chooses and uploads an SVG containing one or more poly-lines. They specify how far apart the two stepper motors are, a 'scale factor' (how much string is let out based on sending a command to move 1mm, dependant on pulley size, steps per rotation, gearing and so on), and the starting length of the strings (i.e. how much string has been let out at the '0' position. Assume the steppers are driven with a control board that assumes a cartesian 3D printer - i.e. GCode to move +10mm in both X and Y will result in both motors turning the same amount. For cases with more than one poly-line, have user-configurable 'pen up' and 'pen down' GCODE strings. Make a preview section that actually simulates such a configuration accurately to render the drawing as it would be done by the bot. Include an option for scaling the SVG to determine it's size, assume the center of the SVG is (0, 0). Provide the code as a standalone HTML file (you can use js and CSS from a CDN of course). Good luck!"
The visual is important - make it easy to check if something works. If this translates to the robot you'll see pictures later today after a hardware store opens :)

## DeepSeek R1

### 3D Printer Control over USB (win)

Prompt: **I have an ender 3 v3 se 3D printer plugged into my linux laptop via USB C cable. It shows up as 'Bus 001 Device 008: ID 1a86:7523 QinHeng Electronics CH340 serial converter' when I do `lsusb`. The stepper motors are currently disabled and set to what I'd like the 0 position to be. Give me python code that, when run, lets me move the position using WASD and Q/E for up/down. Include a visual display of what is happening. Make the code clear and modular enough that I can reuse pieces of it. Use pygame for the GUI.**

It nailed the script on first try (!) and gave good instructions for running it. And yet the serial device wasn't showing up where I (or R1) expected it. It gave good debugging steps, and things that would fix it. But missed something I found with a quick search + skim of [this askubuntu.com thread](https://askubuntu.com/questions/1403705/dev-ttyusb0-not-present-in-ubuntu-22-04): removing `brltty` fixes it (a Braille screen reader uses the same product ID as this chip). A very odd and annoying and niche issue - finding others who'd had the same problem gave the fastest fix in this case. Still, chalking this up as a win for R1 - I now have code that would get me started doing exactly what I want, with a working PoC, in almost no time.

### Asking car questions I mostly know the answer to (win)

**Explain concisely to me how to check oil and coolant in my 2014 Buick encore**

Perfect response. I'm not a car guy but asking followups and comparing to the car manual it's all correct. If you knew nothing this would probably help you on simple stuff and be pretty reliable. But also, just read the manual :)

### Conding help on AI research (win)

**I'm working on a notebook exploring the GRPO loss function, which includes a KL divergence term comparing the model being trained to a reference model. Here's the code from my explorations so far, please give me some code and explanation for how to measure the KL divergence given the output text, the model and the reference model as I have them here. Make it clear and didactic, and suitable for exploratory notebook programming. [code...]**

It gave me an implementation of KL divergence that worked with the code I already had. The KL divergence it measured was considering all possible tokens, not just the selected tokens, which seemed to differ from what the implementation I was looking at does. This cased a double-take, although was arguably more likely that I'd miss this if I wasn't paying attention. It turns out the code I was looking at used [this approximation](http://joschu.net/blog/kl-approx.html). Talking this through with R1 was very helpful for understanding this - it could look at the code I was examining, confirm my reading of it and that it wasn't normal KL, then I could link the approzimation page, and it could convert the code to formulas and explain how it is indeed doing that approximation and why it's useful. This feels like having a super smart assistant, rather than prev AI models which can get a bit hallucinatory when it comes to harder stuff or new, research code. I asked it some follow-ups on related questions about GRPO and it was super helpful there too, noticing links to PPO and REINFORCE and explaining how they're related to the code I was examining.

### Exploring a new model release

**Summarize the new Qwen2.5 VL release and explain how it stacks up against existing models.**

"Oops! DeepSeek is experiencing high traffic at the moment. Please check back in a little while.". They did admirably keeping up with a huge surge in global demand, but did still drop out during the days of peak interest.

### Writing a blog post

As a test (we're talking about dos and don'ts for AI-assisted writing, spoiler I think mostly don't) I gave it four bullet points and a few pointers and it turned it into a very well-written and structured post - some of the nicest writing I've seen from a chatbot.


