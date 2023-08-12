---
title: "Sketchy Unet"
date: "2022-03-29"
---

![](https://datasciencecastnethome.files.wordpress.com/2022/03/screenshot-from-2022-03-29-10-31-48.png?w=946)

The [model demo running on Huggingface Spaces](https://huggingface.co/spaces/johnowhitaker/sketchy_unet_demo)

I wanted a fast way to go from an image to something like a rough charcoal sketch. This would be the first step in a longer pipeline that would later add detail and colour, so all it has to do is give a starting point with the right sort of proportions.

## Finding a dataset

I found a small dataset that seemed like a good starting point (originally created in '[APDrawingGAN: Generating Artistic Portrait Drawings From Face Photos With Hierarchical GANs](https://openaccess.thecvf.com/content_CVPR_2019/html/Yi_APDrawingGAN_Generating_Artistic_Portrait_Drawings_From_Face_Photos_With_Hierarchical_CVPR_2019_paper.html)' by Ran Yi, Yong-Jin Liu, Yu-Kun Lai, Paul L. Rosin). It's quick to download, and (with a little datablock wrangling) easy enough to load with fastai. See [the notebook](https://colab.research.google.com/drive/1ydcC4Gs2sLOelj0YqwJfRqDPU2sjQunb?usp=sharing) for details.

## Training the model

I chose to model this as an image-to-image task, and used fastai's `unet_learner` function to create a [U-net style](https://arxiv.org/abs/1505.04597) network based on a Resnet34 backbone. Starting with 128px images and then moving up to 224px, the model is trained to minimise the MSE between the output and the reference sketch. In about 3 minutes (!!) we end up with a model that is doing pretty much exactly what I want:

![](https://datasciencecastnethome.files.wordpress.com/2022/03/screenshot-from-2022-03-28-19-06-20.png?w=648)

Images (left), artist's sketch (center), model outputs (right)

## Sharing a Demo

I've been playing around with HuggingFace Spaces recently, and this model was a great candidate for a simple demo that should run reasonably fast even on a CPU (like those provided by Spaces). At the end of [the training notebook](https://colab.research.google.com/drive/1ydcC4Gs2sLOelj0YqwJfRqDPU2sjQunb?usp=sharing) you can see the gradio interface code. Very user-friendly for these quick demos! The [trained model was uploaded to huggingface](https://huggingface.co/johnowhitaker/sketchy_unet_rn34) as well, and they somehow detected that my code was downloading it because it shows up as a 'linked model' from [the space](https://huggingface.co/spaces/johnowhitaker/sketchy_unet_demo).

It's neat that I can so easily share everything related to a mini-project like this for others to follow along. The [colab notebook](https://colab.research.google.com/drive/1ydcC4Gs2sLOelj0YqwJfRqDPU2sjQunb?usp=sharing) provides a free cloud environment to replicate training, the [model](https://huggingface.co/johnowhitaker/sketchy_unet_rn34) is hosted by someone with lots of bandwidth and is easy to download, and [the demo](https://huggingface.co/spaces/johnowhitaker/sketchy_unet_demo) needs no technical skills and lets anyone try it out in seconds. Hooray for fastai, gradio, huggingface and so many others who work so hard to make our lives easy :)

## Update: What's this for?

![](https://datasciencecastnethome.files.wordpress.com/2022/04/screenshot-from-2022-03-31-14-19-42.png?w=978)

Waterface demo: https://huggingface.co/spaces/johnowhitaker/waterface

I used this model to 'sketchify' images before loading them into an imstack and optimising that to match a CLOOB prompt like 'A charcoal and watercolor sketch of a person'. After a few steps the result looks pretty OR more likely a little creepy. Ah, the power of AI :) Try it out [here](https://huggingface.co/spaces/johnowhitaker/waterface).
