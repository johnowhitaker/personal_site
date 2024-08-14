---
title: "What You Should Read (AI Edition)"
date: 2024-08-14
categories:
  - Blog
---

# What You Should Read (AI Edition)

There have been hundreds of thousands of films made. But if you reveal that you haven’t seen Star Wars, you’re regarded with a mixture of sympathy and scorn. In this listicle, I’m going to attempt to give you a short list of essentials to spare you the same fate in the field of AI research. This is off the top of my head, so I’ll definitely miss things and get some timelines wrong. Let me know if there are things you think I absolutely must add. I’ve split things up into a few different categories to keep the story flowing.

See also: supposedly the list Ilya sent to Carmack: https://arc.net/folder/D0472A20-9C20-4D3F-B145-D2865C0A9FEE

Most of this list was written ~6 months ago to send to a friend, sharing in case I get asked for it again.

## Vision

Let’s start with how computers see. Back in the old days, computer vision was a hard task dominated by carefully hand-crafted features in controlled conditions. A forward-thinking Fei-Fei Li set a near-impossible-seeming task: learn to classify ~1M images into ~1000 classes. Some nerds figured out how to build convolutional neural networks in a way that let them use GPUs for training and got a much better score than any prior approach. Soon deep learning was a hot topic and more and more researchers fought for the top spot on the imagenet accuracy leaderboards. 

You don’t need to read every paper that claimed a 0.1% improvement. I’d recommend picking any ‘intro to convolutional nns’ tutorial to get the basics then following the main improvements:
- The original ResNet paper (https://arxiv.org/abs/1512.03385) showed how using residual connections makes it possible to train much deeper networks

- MobileNets (https://arxiv.org/abs/1704.04861) introduced “depth-wise separable convolutions to build light weight deep neural networks.” which made them popular for deployment on lower-power devices. 

- EfficientNet (https://arxiv.org/abs/1905.11946) took this further and was a fan favourite for a while in terms of performance and efficiency

- When transformer models started to get popular (see the LLM section), the VIT paper (https://arxiv.org/abs/2010.11929) fed patches of an image into a transformer and got extremely good results, kicking off a war between the convolutionists and the transformacons that continues to this day. 

- ConvNeXt (https://arxiv.org/abs/2201.03545) said ‘hey let’s take some good ideas from ViTs and elsewhere and see if we can make a better convnet for the 2020s.’

- MLP-Mixer (a personal fave, less pivotal) said ‘who needs attention or convolutions? Just make sure there’s some way to mix across channels (like the MLPs in a ViT) and some way to mix across space (like the attention in a ViT or the conv kernels in a convnet). I love that it works - hooray scaling and the bitter lesson :)

ViTs are probably the go-to these days, although there are attempts to fix some of their flaws (fixed size, need lots of compute especially for high-res images, less priors baked in so well-suited to data-rich regimes) - but most of the modifications proposed sort of make sense and also don’t make *that* big of a difference compared to scaling. If you want more on them maybe read “Scaling Vision Transformers” (https://arxiv.org/abs/2106.04560) and something like the Hierarchical ViT paper (https://arxiv.org/abs/2205.14949). 

While people were duking it out for the classification crown, there were a few other things happening
- A medical segmentation paper proposed the UNet architecture that turned out to be pretty good for anything that needs an image-shaped output (like segmentation) - https://arxiv.org/abs/1505.04597

- People figured out how to do object detection, although there ended up being tons of different ways to finagle the data and at least 8 papers with different architectures using the name YOLO. If you care about object detection probably just check what the most recent one is that everyone seems to use. 

- People found that a model trained on imagenet could then be fine-tuned for some new task using very few images, in a process called “transfer learning”. See the first lesson of fast.ai to get excited about this and to see how easy it can be.
You should check out this 2017 work exploring what these models learn: https://distill.pub/2017/feature-visualization/

There’s also the big question of labels. Imagenet is all well and good, but if we want to scale up more can we find ways to learn without class labels?

- Contrastive learning: two images of the same thing (or, pragmatically, two transforms of the same image) should map to similar features. Unrelated images should map to less-similar features. SimCLR “A Simple Framework for Contrastive Learning of Visual Representations” (https://arxiv.org/abs/2002.05709) is a goodie.

- MAEs “Masked Autoencoders Are Scalable Vision Learners” (https://arxiv.org/abs/2111.06377) - what if we instead learn to predict a masked-out region of an image? Turns out at scale this is enough to learn useful features. Lots of fun overlap between MAEs and generative models too…

- iJEPA “Self-Supervised Learning from Images with a Joint-Embedding Predictive Architecture” (https://arxiv.org/abs/2301.08243) Yann thinks there’s a better way, we predict the *embedding* of the target not the target itself. JEPA is an interesting line of research.

- CLIP (https://arxiv.org/abs/2103.00020) - a contrastive approach that maps images and text to the same space (ish). Let’s you learn from billions of captioned images on the web. Gives an incredibly useful way to get features from images and text that you can use for 0-shot classification, search, conditioning generative models… one of the most impactful vision papers IMO. Lots of derivatives, SigLIP etc improving on the core idea, OpenCLIP project with tons of models… 
Datacomp is an interesting one, asking ‘what data should you use for a clip-like thing if the model + compute is fixed?’

Finally, there’s the question of how we generate images. Can we just run a convnet backwards? Not quite, but:

- VAEs: papers can be very math-heavy. https://arxiv.org/abs/1906.02691 is a 2019 paper by D. Kingma and Max Welling who also did an important 2013 paper https://arxiv.org/abs/1312.6114. I think maybe skip both, maybe go for a more accessible intro like https://deeplearning.neuromatch.io/tutorials/W2D4_GenerativeModels

- Generative Adversarial Networks (https://arxiv.org/abs/1406.2661) introduce a great idea: use a second network trying to tell the diff between the output of the first network and real data. GAN literature got full of fiddly tricks and a mythical feeling that these beasts are hard to train. 

- BigGAN (https://arxiv.org/abs/1809.11096) scaled up and showed class conditioning. StyleGAN (https://arxiv.org/abs/1812.04948) learned ‘disentangled’ features and gave amazing control and trippy interpolations. light-weight GAN (https://arxiv.org/abs/2101.04775) is my go-to for something you can train on a relatively small dataset with all the modern tricks. And more recently GigaGAN (https://arxiv.org/abs/2303.05511) flexed fast text-to-image (meh) and super-resolution (incredible). 

- A Neural Algorithm of Artistic Style (https://arxiv.org/abs/1508.06576) came up with the cool idea of style transfer. My course has some more modern approaches https://johnowhitaker.github.io/tglcourse/representations.html

- Taming Transformers for High-Resolution Image Synthesis (https://arxiv.org/abs/2012.09841) aka the VQGAN paper showed how to tokenize images and also set us up for latent diffusion and the fun we had optimizing VQGAN latents with CLIP (https://johnowhitaker.github.io/tglcourse/generators_and_losses.html) 

- Dalle (https://arxiv.org/abs/2102.12092) modelled images and text as sequences - just learn to predict the next token in a sequence that looks like [text caption… image patch tokens]. Parti (https://sites.research.google/parti/) scaled it up and how weird that worked!

Diffusion models stole the show though

- Imagen and Dalle 2 showed off high-quality (closed)

- Stable Diffusion (https://arxiv.org/abs/2112.10752) gave us open-source stuff, newer versions track trends in what seems to work

- InstructPix2Pix (https://arxiv.org/abs/2211.09800) used synthetic data to get a model that can do image + text -> edited image. Emu Edit did more data. 

- Personalization happened (Dreambooth (https://arxiv.org/abs/2208.12242), Textual Inversion (https://arxiv.org/abs/2208.01618), ZipLoRA(https://arxiv.org/abs/2311.13600) are some standouts)

- Controlnet (https://arxiv.org/abs/2302.05543) and IPAdapter (https://arxiv.org/abs/2308.06721) added extra ways to control the generation, as did many others

- Making them fast w/ distillation, score matching, flow, …. It gets crowded and complicated here. Progressive Distillation (https://arxiv.org/abs/2202.00512) was an early big one. 

BTW diffusion models learn useful features for other tasks, there’s a whole bunch of stuff too much to cover here. 


## Language (WIP)

TODO:
Synthetic data
Textbooks are all you need (tinystories)
Orca, evol-instruct, restructured Pretraining
Optimizers, training dynamics etc
Place for adam, layernorm, grad clipping, LR scheduling, EMA, …

### The Early Days

1. [The Unreasonable Effectiveness of Recurrent Neural Networks](https://karpathy.github.io/2015/05/21/rnn-effectiveness/) (2015) - Karpathy's great blog post on character-level RNNs.

2. [ULMFiT: Universal Language Model Fine-tuning for Text Classification](https://arxiv.org/abs/1801.06146) (2018) - Demonstrated transfer learning for text. "Pretraining" becomes a thing.

### The Rise of Transformer-based Models

3. [Attention Is All You Need](https://arxiv.org/abs/1706.03762) (2017) - Introduced the Transformer architecture for translation.

4. [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://arxiv.org/abs/1810.04805) (2018) - Bidirectional training of Transformers.


5. [T5: Exploring the Limits of Transfer Learning](https://arxiv.org/abs/1910.10683) (2020) - Unified text-to-text framework.

6. [Improving Language Understanding by Generative Pre-Training](https://s3-us-west-2.amazonaws.com/openai-assets/research-covers/language-unsupervised/language_understanding_paper.pdf) (2018) - Introduced GPT. "We demonstrate that large
gains on these tasks can be realized by generative pre-training of a language model
on a diverse corpus of unlabeled text, followed by discriminative fine-tuning on each
specific task"

7. [Language Models are Unsupervised Multitask Learners](https://d4mucfpksywv.cloudfront.net/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) (2019) - Introduced GPT-2. "We demonstrate that language
models begin to learn these tasks without any explicit supervision when trained on a new dataset
of millions of webpages called WebText."

8. [Language Models are Few-Shot Learners](https://arxiv.org/abs/2005.14165) (2020) - Introduced GPT-3. "Here we show that scaling up language models greatly improves task-agnostic, few-shot performance"

9. [Scaling Laws for Neural Language Models](https://arxiv.org/abs/2001.08361) (2020) - Empirical analysis of scaling relationships. 

10. [Training Compute-Optimal Large Language Models](https://arxiv.org/abs/2203.15556) (2022) - Chinchilla gave better scaling laws for how to get best performance at different scales (without considering inference costs).

I like how the GPT series of papers show the progression from unsupervised pretraining to few-shot learning, as we realize how much this paradigm can do.



### Efficient Fine-tuning and Adaptation

11. [LoRA: Low-Rank Adaptation of Large Language Models](https://arxiv.org/abs/2106.09685) (2021) - Efficient fine-tuning method. After this there was a flurry of LoRA variants since it is something people can research on an academic budget. Most can safely be ignored. I like 'DoRA' as a better-performing version and LoftQ for quantization-aware LoRA stuff (see also FA-LoRA I think it's called).

12. [QLoRA: Efficient Finetuning of Quantized LLMs](https://arxiv.org/abs/2305.14314) - Efficient fine-tuning with quantization. By the kegend Tim Dettmers, made fine-tuning with quantization practical for so many more people. Check out the answerai posts on this topic for more on scaling and quantization.

### Instruction Tuning and Alignment

13. [InstructGPT: Training language models to follow instructions](https://arxiv.org/abs/2203.02155) (2022) - Instruction-following using human feedback.

14. [Constitutional AI: Harmlessness from AI Feedback](https://arxiv.org/abs/2212.08073) (2022) - AI-assisted approach to alignment.

15. [Direct Preference Optimization: Your Language Model is Secretly a Reward Model](https://arxiv.org/abs/2305.18290) (2023) - Simplified approach to RLHF.

16. [Zephyr: Direct Distillation of LM Alignment](https://arxiv.org/abs/2310.16944) (2023) - A good recipe for making 'aligned' models based on synthetic data from big models.

17. Tulu and [Tulu 2](https://arxiv.org/abs/2311.10702) applying this recipe and exploring what data works well. Decent emperical papers, lots of insights about things like length skewing LLM-judged scores.

As with LoRA, there was a flurry of DPO variants. See [this video of mine](https://www.youtube.com/watch?v=YNOIyvUCpAs&t=14290s) for a chat about some of the modifications and why some at leat are useful.

### Multi-Modal

18. [Flamingo: a Visual Language Model for Few-Shot Learning](https://arxiv.org/abs/2204.14198) - early good VLM. Idefics is open source version.

19. [PaliGemma](https://arxiv.org/abs/2407.07726) - shows the approach of glueing a pretrained vision encoder (siglip in this case) to an existing language model (gemma in this case) to get a multi-modal model. Not the first to do it but a nice decent recent paper.

20. [Chameleon](https://arxiv.org/abs/2405.09818) (and [MoMa](https://arxiv.org/abs/2407.21770) - the efficiency upgrade with MoE of Chameleon). From Meta, good look at how early fusion models might end up looking.

