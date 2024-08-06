---
title: "Tab Clearing"
date: 2024-06-27
categories:
  - Blog
---

# Notes as I clear my browser tabs / reading list

Writing down quick takeaways/impressions as I clear up some of my reading backlog

![](https://j.gifs.com/mLlYoY.gif)

## Diffusion/Image Stuff

[AuraSR](https://blog.fal.ai/introducing-aurasr-an-open-reproduction-of-the-gigagan-upscaler-2/) is a nice, GAN-based super resolution model that does 4x upscaling. Based on Adobe's GigaGAN but released under a open source license. This is a really nice image upscaling model.

[Noise schedules considered harmful](https://sander.ai/2024/06/14/noise-schedules.html): Fantastic posts from Sander. Diving into noise schedules and why it might make more sense to instead look at relative noise. Waiting during training and choice of timestep/ noise level during sampling as two independent things and stopped focusing on this. Needless abstraction of time steps or noise schedules. Fantastically written clare lines up with exactly how I view this. No City math. Definitely a recommended read.

[DiffRast](https://srush.github.io/DiffRast/): A fun expiration of some of the things you can do with differentiable graphics, by Sasha Rush. This is exactly the type of thing that I would spend weeks playing with. If I was in my tinkering with AI art face. It is using Jax. I want to come back and give this a proper look at some point.

[MimicBrush](https://xavierchen34.github.io/MimicBrush-Page/): They have nailed reference-based in painting. Amazing results. The trick is to construct training data from pairs of video frames. Learn to fill a masked region of one frame with info from another -> learn to use a reference image to fill gaps, without copying its structure.

[Hallo](https://fudan-generative-vision.github.io/hallo/#/): yet another audio-driven face animation thing, ok I guess. Controlnet-style way to feed in the reference image, "temporal attention", bla bla bla

[Flash Diffusion](https://gojasper.github.io/flash-diffusion-project/): A diffusion distillation method that has the students predicting One step what the teacher predicts in multiple and also uses an adversarial loss. Seems like a decent diffusion distillation paper, but nothing particularly novel just skimmed

[RB-Modulation](https://rb-modulation.github.io/): Impressive results on custom content and style via reference images with diffusion models. Nathaniel Ruiz of dream Booth and ziplora among many others supervised. The results are amazing but the paper is almost impossible to understand. Far too much technical jargon and acronyms. I did not bother trying to go deep on it. The tldr is something like 'we mess with the attention to include features from the style or content images and we have a way of disentangling the two. The features are somehow persist separately and then combined allowing us to reweight things or adjust how and where the influence from content or style applies'. But there is also lots of nonsense about optimal control and stochastic bloody blast.

## LLM stuff

[Prism](https://thesephist.com/posts/prism/): very fun work that is similar in some ways to anthropics sparse Auto encoders work. It identifies vectors or directions in feature space or in embedding space. If you will that are that that represents atomic concepts around language and then explores using these to edit text. So for example, they identify some semantic directions like casual/formal or becoming a question or whatever, and then have a auto encoder style thing that can take in some text and produce a vector and then produce text from that vector and then they find ways to edit the embedding based on these identified features. So you could for example, make some text more formal or make it a question instead of a statement. There's a lot in the post that I didn't go into too deeply, but it seems like a very nice exploration of practical applications for the kind of mechanistic interpretability stuff we looked at with andthics paper. I look forward to his future work

[Gemma 2](https://blog.google/technology/developers/google-gemma-2/). [Technical report](https://storage.googleapis.com/deepmind-media/gemma/gemma-2-report.pdf) the Gemma 2 model is a sizable improvement over the original Gemma model. The 9B now seems like the best in its weight class beating out Llama 3 8b. The 27b version is almost as good as llama 70B on some measures the best in its size class, but also unclear if it is with it to move from Llama 3 70B for the kinds of applications, this would be used for. Interestingly, they explored distillation as a training process for the smaller models. At least they found a substantial boost compared to normal pre-training. They also did model averaging where they took the SFT version and the RLHF version and averaged the weights. Overall the model looks pretty decent. Nothing too crazy. Architecture wise they used grouped query attention, mix of local and global attention. It seems like a pretty efficient and performant model.

[Sakana's LLM Squared](https://sakana.ai/llm-squared/): Using llms to evolve codes to train. LLMs sounds very fancy and futuristic, but I was a little bit underwhelmed by what they actually did. Even though it was still pretty cool. They are using llms as code mutation to "evolve" the loss function for something like DPO so preference optimization. They generate lots of candidate algorithms and evaluate them and pick the best and then show that sure enough and it also does well on other similar evals. The whole thing is a little iffy since I know these algorithms can be finicky and it's all preference-based with MT-bench and alpaca eval, but still cool that they were able to improve over DPO. We'll see how it goes and if they can evolve code for other parts of the stack which seems a lot harder to optimize for and measure, but still cool to see people trying fun things like this. I can never resist evolution or computation.

[DigiRL-Agent](https://digirl-agent.github.io/): Learning the hard task of controlling a device via vision. They do offline RL based on annotated actions. This is what many others do and it does pretty poorly on real life. Benchmarks. But then they further train "online" RL with rewards based on vlm scoring. In other words, they have agents actually interact with a virtual device to carry out tasks. This translates to a huge improvement in performance on the "Android in the wild" data set.. they set a new state-of-the-art. I am not sure how well this generalizes outside of this specific task set/ domain. But it is very cool to see agents actually taking action even if it's in a simulated environment and using that to improve versus just trying to use an off the shelf vision language model that does not have as much understanding as is needed to operate real world devices based on pixels only.

[Charachter AI post 'Optimizing Inference'](https://research.character.ai/optimizing-inference/): Amazing post with a bunch of tricks from Noam Shazeer and crew. Key ideas they use when serving 20k qps:
- Multi-Query Attention to reduce KV size
- interleave local attention vs global attention (only 1/6 global) to speen things up.
- Cross-layer KV cache sharing (between 2 or 3 consecutive layers) to reduce memory usage
- Fancy caching to match as much as possible. All the focus is on keeping as much KV cache in mem as possible it seems. 
- They use int8 quant on weights, activations and KV cache, with fancy kernels. Train in int8 too. 

[The Many Ways that Digital Minds Can Know (Moultano)](https://moultano.wordpress.com/2023/06/28/the-many-ways-that-digital-minds-can-know/): A fun way to look at some different axes we might care about re: LLMs. Interesting framing! 

[Musings on typicality](https://sander.ai/2020/09/01/typicality.html): A 2020 post from Sander Dieleman, helping explain why beam search isn't ideal - linked from the recent review paper "From Decoding to Meta-Generation: Inference-time Algorithms for Large Language Models". 

[Finding GPT-4’s mistakes with GPT-4](https://openai.com/index/finding-gpt4s-mistakes-with-gpt-4/): Using a model to spot the mistakes of a model. Duuuuude. Cool work, having humans review outputs for RLHF seems like a spot where bugs could be missed, this appears to help a bunch with that (and will likely be a useful model for them to have lying around too!).