---
title: "Tab Clearing (April 9 2025)"
date: 2025-04-09
categories: 
  - "misc"
image: "https://i.pinimg.com/originals/40/fe/86/40fe863b3ccf9ceb56cbef670cf6bc41.gif"
description: Clearing out my open tabs
---

- [Web synth](https://synth.grantkot.com/) - great sounds, easy controls, works on mobile. Big fan. Think they use adventure time sounds, in some kind of library? I want to emulate this at some point.
- [Seeking the Productive Life: Some Details of My Personal Infrastructure](https://writings.stephenwolfram.com/2019/02/seeking-the-productive-life-some-details-of-my-personal-infrastructure/) - revisiting this inspiring piece from Wolfram on how he optimizes bits if his life. He's shockingly productive, I think a lot of us could learn from him.
- [Command A: An Enterprise-Ready Large Language Model](https://arxiv.org/abs/2504.00698) - interesting paper with lots of detail on their enterprisey post-training.
- [Dream 7B](https://hkunlp.github.io/blog/2025/dream/) - 'Diffusion reasoning model' continuing the trend of diffusion language models starting to look impressive at 7Bish scale, building on smaller-scale PoCs from the past. Watching this space with interest :) It is initialzed from Qwen which is an interesting tidbit.
- [Together AI announce DeepCoder](https://www.together.ai/blog/deepcoder) - speaking of things initialized with Qwen, this 14B reasoner does extremely well thanks to good, open work on RLVR for coding, ft their 'GRPO+'. Good-looking work!
- [70 DIY Synths On One Webpage](https://hackaday.com/2025/04/02/70-diy-synths-on-one-webpage/) an inspiring collection for if I ever feel like building HW synths
- [The Hidden Cost of Our Lies to AI](https://www.lesswrong.com/posts/9PiyWjoe9tajReF7v/the-hidden-cost-of-our-lies-to-ai) - DNF, but I do like peeking at what the LW people are talking about, and I do have a string sentiment against lying to AI that the author shares.
- [Simone's all-edge puzzle](https://yetch.studio/products/edge-piece-puzzle) - A nice idea I'm getting for my puzzle-loving wife (shh it's a birthday secret)
- [https://docs.perplexity.ai/guides/pricing](https://docs.perplexity.ai/guides/pricing) - Their deep research API looks nice, I saw a colleague using it in an internal tool and want to copy that so I don't have to break flow to head to openai/google for deep research style questions.
- [AI2027](https://ai-2027.com/) - I enguaged a lot with this, listening to the Dwarkesh podcast and skimming the research. They're nothing if not thorough. I'm not sure I quite buy the foomish takeoff stuff still, but I also don't think you can dismiss these ideas out-of-hand. 
- [3D Print (and Play!) The Super Mario Tune As A Fidget Toy](https://hackaday.com/2025/04/04/3d-print-and-play-the-super-mario-tune-as-a-fidget-toy/) - I'm going to print off some rick-rolls and leave them lying around
- [VAPO paper](https://arxiv.org/abs/2504.05118) - I've been meaning to look at DAPO, VAPO and other GRPO variants but not had the time+inclination recently, feels like the DPO or LoRA fevers as everyone tries out minor mods that work on some benches...
- [Google's Ironwood TPUs](https://blog.google/products/google-cloud/ironwood-tpu-age-of-inference/) look like inference beasts...
- [OmniControl](https://arxiv.org/abs/2411.15098) and this [OmniControl Art](https://huggingface.co/spaces/Yuanshi/OminiControl_Art) space (the latter replicating 4o's stylization trick with Flux) look like an interesting modern controlnet alternative. I want to take a closer look at some point.
- [Model Extrapolation Expedites Alignment](https://arxiv.org/abs/2404.16792) - fun: train DPO model, interpolate between base SFT model and that, with scale > 1. CFG but it's comparing preds from DPO model vs base, giving a boost on some tasks haha. Not sure it'll hold for more carefully trained models but neat to see. Reminds me of a paper that did something similar but using early vs late layer predictions instead of two model variants. Have also seen small vs large models. ALl these hacks feel likely to get bitter-lessoned but fun for now. Another in this veign was:
- [Thoughts Are All Over the Place: On the Underthinking of o1-Like LLMs](http://arxiv.org/abs/2501.18585) - which supresses thought-changing tokens like "alternatively" until the model has thought for long enough on that topic (some settable threshold) which is a funny hack to encourage longer thoughts. They do see some improvement!
- [Rethinking Reflection in Pre-Training](https://arxiv.org/abs/2504.04022) - looking at how much 'reasoning' is learnt during pre-training, and identifying a measure that grows steadily, which seems very relevant to the discussion over whether reasoning is all RL or is motly elicitation of latent capabilities learnt during pretraining.
- [Learning to Reason for Long-Form Story Generation](https://arxiv.org/abs/2503.22828) very neat idea: RLVR on reasoning hains with the score being how likely the model is to generate the gold standard output after said reasoning chain: "Our reward uses a reference model to get the
improved likelihood of the true next chapter.", "🎯 Verifiable Rewards via Completion Likelihood Improvement (VR-CLI) evaluates reasoning by the "improvement" in downstream perplexity of the gold completion (the next chapter)."
- [Compression Represents Intelligence Linearly](https://arxiv.org/abs/2404.09937) - "we find that LLMs' intelligence -- reflected by average benchmark scores -- almost linearly correlates with their ability to compress external text corpora. These results provide concrete evidence supporting the belief that superior compression indicates greater intelligence." - nice to have more empirical evidence for this, I think it's a good heuristic to keep in mind.
- [Inference-Time Scaling for Generalist Reward Modeling](https://arxiv.org/abs/2504.02495) - TO READ
- [On Vibe Coding](https://www.ethansmith2000.com/post/on-vibe-coding) - TO READ
- [Taking a responsible path to AGI](https://deepmind.google/discover/blog/taking-a-responsible-path-to-agi/) - TO READ
- [Deep site](https://huggingface.co/spaces/enzostvs/deepsite) - TO TRY
