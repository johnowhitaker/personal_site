---
title: "Stable Diffusion Deep Dive Notebook Run-through"
date: 2023-01-30
categories: 
  - "Video"
image: "thumbnails/844LY0vYQhc.jpg"
---

### Stable Diffusion Deep Dive Notebook Run-through

{{< video https://www.youtube.com/embed/844LY0vYQhc >}}

In this video/notebook Johno shows us what is happening behind the scenes when we create an image with Stable Diffusion, looking at the different components and processes and how each can be modified for further control over the generation process.The notebook is available in this repository - https://github.com/fastai/diffusion-nbs00/00 - Introduction00/40 - Replicating the sampling loop01/17 - The Auto-Encoder03/55 - Adding Noise and image-to-image08/43 - The Text Encoding Process15/15 - Textual Inversion18/36 - The UNET and classifier free guidance24/41 - Sampling explanation36/30 - Additional guidanceThis was made as a companion to lesson one of the new FastAI 2022 part 2 course (aka Lesson 9) by Jonathan Whitaker (his channel - https://www.youtube.com/channel/UCP6gT9X2oXYcssfZu05RV2g)Errata - there should be some scaling done to the model inputs for the unet demo in cell 49 (19 minutes in) - see scheduler.scale/model/input in all the loops for the code that is missing. And in the autoencoder part the 'compression' isn't exactly 64 times since there are 4 channels in the latent representation and only 3 in the input.
