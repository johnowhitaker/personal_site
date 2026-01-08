---
title: How Much Grams? Having VLM's Guess Weight of Objects (DRAFT)
date: 2026-01-08
categories: 
    - mini-projects
---

I made a tiny little eval based on asking models to esitmate the weight of various objects in grams, inspired by [this guy on tiktok](https://www.youtube.com/shorts/NqtuquniGgM) who video calls ChatGPT and makes fun of it for being bad at this.

TODO main image

## Inspiration

I want to quantify an automated pipetting system using a precision scale, which required reading off the weight based on a photo of the scale. It seemed like the kind of simple thing that might work with a local VLM on my mac, and I wanted an excuse to play with LFM 2.5 1.6B that was released that day. So I snapped a few pics of my scale showing different weights, in different lighting and angles, and tried moondream v3 preview, zai-org/glm-4.6v-flash, and LFM 2.5 1.6B ([code](https://gist.github.com/johnowhitaker/ce8ab1fb34c8373b5e12db0eca9e27dc)). I was a little suprised how bad they are! LFM was fast enough that I fiddled with the prompt a couple of times, and felt that if I kept the lighting constant and didn't need fancy things like sign, it might *mostly* be OK with the occasional 8<=>0 mixup. Then I tried gemini-flash-3, which was near-perfect and cost $0.0005 per image. So the only sensible answer is to use that! It's really tough to compete with a cheap, fast, API model like this with local models. Anyway, jagged frontier and all that. I figured I might as well make an eval inspired by this, and the obvious extension is to see if the models can guess the weight of the objects without seeing the scale reading too.

![Gemini Flash 3 getting the scale readings mostly correct](images/scale_gemini.png)

## Collecting the data

This is the kind of thing that competent coding models really shine at. I made a data collection 'app' with this prompt to GPT-5.2-Codex (in Codex CLI):

**"I'd like to build a dataset for an AI eval. The way I'd like to gather the data is to run a Flask app on this Mac which we will create in this currently empty directory. It should, when I visit mac.local/whatever the port is for my phone, I should get a page that asks for camera permission and then it prompts me to take a picture of an object, take a picture of the object on the scale and then take a picture of the scale reading. So three photos for every object that's going to be in the dataset. These three should all be saved with a consistent ID for that object or that data point followed by _object _scale _scale reading. The app should be kind of nice to use and give me options for retaking a photo right after I've taken it or moving on to the next photo, canceling an observation at any point. You know just basically a nice simple data gathering UI so that I can quite rapidly build up a fun little dataset to demonstrate this. Let me know if you have any questions otherwise feel free to start the implementation!"** (voice dictated)

It nailed it first try. The resulting [app](https://github.com/johnowhitaker/how_much_grams) let me quickly snap some pics of 20 objects, with 3 pics each (object, object on scale, scale reading).

## Testing Some Models

TODO share

## Thoughts

VLMs with suprising gaps, SpecID text-only performance note, future idea of fine-tuning (with more data), how amazing codex/claude-code are for this kind of obvious-if-it-works mini-app, make your own evals, ...?