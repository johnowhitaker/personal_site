---
title: "Editing Images with Diffusion Models (lit review _ overview of different approaches)"
date: 2022-11-22
categories: 
  - "Video"
image: "thumbnails/zcG7tG3xS3s.jpg"
---

### Editing Images with Diffusion Models (lit review _ overview of different approaches)

{{< video https://www.youtube.com/embed/zcG7tG3xS3s >}}

How can we use diffusion models to edit existing images rather than generating completely new images1) Add some noise, denoise with a new prompt- VQGAN + CLIP paper - https://arxiv.org/pdf/2204.08583.pdf (includes editing with masks, prompt changes, lots of other ideas that have parallels in the newer diffusion model works)- SDEdit - https://sde-image-editing.github.io/- MagicMix - https://magicmix.github.io/2) As in (1) but with a mask- Blended Diffusion - https://omriavrahami.com/blended-diffusion-page/- Mask with CLIPSeg - https://huggingface.co/spaces/nielsr/text-based-inpainting- Get the mask from the diffusion model (DiffEdit, great paper) - https://arxiv.org/abs/2210.11427- John's post on DiffEdit - https://www.storminthecastle.com/posts/diffedit/3) Cross-attention Control- Prompt-to-Prompt Image Editing with Cross Attention Control - https://arxiv.org/abs/2208.01626 (report on this with SD - https://wandb.ai/wandb/cross-attention-control/reports/Improving-Generative-Images-with-Instructions-Prompt-to-Prompt-Image-Editing-with-Cross-Attention-Control--VmlldzoyNjk2MDAy)4) Fine-tune ('overfit') on a single image and then generate with the fine-tuned model- Imagic paper - https://arxiv.org/pdf/2210.09276.pdf- UniTune - https://arxiv.org/pdf/2210.09477.pdfI hope you enjoyed this video! Which method do you think will win out Anything you'd like more information on
