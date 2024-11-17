---
title: "Facewave: Controlling Midi Expression with your webcam"
date: 2024-11-01
categories:
    - "mini-projects"
---

One gripe I've had with digital instruments is a lack of expression. Coming from a wind instrument background, I don't like having no control over a note once it starts. So I love the Roli Seaboard (I have the Rise 2) - a squishy playing surface that uses 'Midi Polyphonic Expression' (MPE) to let you vary all sorts of parameters by pushing, sliding, and squishing the keys. Unfortunately that's a $1000+ investment, not so easy to recommend. Recently they announced a new product, that lets you control sound dynamics by waving your hands about above the keyboard, using hand tracking with a pair of IR cameras. Very cool! But as soon as I saw it the question becomes: can we get most of this for free with a webcam?

'Facewave' is a proof-of-concept to show the answer is yes! I use mediaPipe to track face and hands in the shot, and send midi control codes (CC) out to be used in your synth of choice. Here's what it looks like in action:

![](images/facewave.png)

The code is available on [GitHub](https://github.com/johnowhitaker/facewave) and is hosted both on the accompanying github page (https://johnowhitaker.github.io/facewave/) and on my site (https://tools.johnowhitaker.com/facewave). You'll need a way to feed the midi from that into a synth - I use [loopmidi](https://www.tobias-erichsen.de/software/loopmidi.html) to create a virtual midi port that I can connect to my DAW. [Here](https://x.com/johnowhitaker/status/1851667773354840523) is a video of an early prototype in action.

This is a ton of fun! I made a simple [synth](https://tools.johnowhitaker.com/msynth) tool to test this out if you don't have a DAW / synth installed - you can play notes with your computer keyboard and modulate the sound with Facewave (as long as you have loopmidi set up). 

I love this idea, but don't know how much further I'll take it. I'd love someone with more musical contacts to share it around, or steal this idea and add it to your own tools!