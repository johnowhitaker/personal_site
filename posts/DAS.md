---
title: "Direct Ascent Synthesis: Revealing Hidden Generative Capabilities in Discriminative Models"
date: 2025-02-17
categories: 
  - "papers"
  - "blogs"
  - "wip"
description: "A new paper for an older idea: finding a good representation for turning a discriminative model into a generative model."
---

I have a paper out! What!?!? Johno doesn't write papers. True. But when Stanislav Fort discivered a neat trick that was one I'd also found back in the day, we got talking and figured it ought to be better documented so other people can use it too. I have to say: he did all the hard work! I sadly didn't have time to play much, but did chip in a little. This blog post is a few of my ow thoughts, but you should read the [paper](https://arxiv.org/abs/2502.07753) first.

![Figure 1 from our paper](images/das.png)

The TL;DR is as follows: instead of optimizing raw pixels, optimize a collection of image tensors at different resolutions that get resized and stacked together to form the final image. This turns out to have really neat regularization effects, and gives a really nice primitive for seeing what 'natural'-ish images trigger various features in classifiers etc. This is pretty much the idea behind my 2021 ['imstack'](https://github.com/johnowhitaker/imstack) stuff, but made cleaner and more general.

The other trick is to do some augmentations, critically adding some jitter (different crops) and noise. Once you have these pieces in place, you can optimize towards a text prompt with CLIP, or do style transfer, or trigger a specific class in a classification model... the possibilities are endless. Here's the code to make the quintessential 'jellyfish' from an imagenet model for e.g. ([colab](https://colab.research.google.com/drive/1gLZXcPIKpBwYWgweOVli9ORcOyJ-khJ5?usp=sharing))

```python
def stack(x, large_resolution):
  out = 0.0
  for i,p in enumerate(x):
    out += F.interpolate(p, size=(large_resolution, large_resolution), mode='bicubic' if resolutions[i] > 1 else 'nearest')
  return out

def raw_to_real_image(raw_image): return (torch.tanh(raw_image)+1.0)/2.0

large_resolution = 336
resolutions = range(1,large_resolution+1, 4)
image_layers = [torch.zeros(1,3,res,res).to("cuda") for res in resolutions]
for i,p in enumerate(image_layers): p.requires_grad = True
optimizer = torch.optim.SGD(image_layers, 0.005)
for step in tqdm(range(100)):
  optimizer.zero_grad()
  images = raw_to_real_image(stack(image_layers, large_resolution))
  images = make_image_augmentations(images, count=16, jitter_scale=56, noise_scale=0.2)
  loss = -model(normalize(images))[:, 107].mean()
  loss.backward()
  optimizer.step()
```

I want to do a video explanation soon to capture more thoughts on this and show off more of what this technique can do. See also, [Stanislav's announcement post](https://x.com/stanislavfort/status/1890724291752100265). The rest of this post is me rambling on some tangential bits that have come up since the paper was released.

## Thoughts


WIP, TODO:
- Describe the early days
- Link my initial experiments
- The benefits of curiosity driven independent researchers
- 'This doesn't cite X' - peer review pile-ons and the downsides of twitter
- I'm going to stick to blog posts