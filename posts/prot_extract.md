---
title: "Hunting for Miracles in the ESM Protein Atlas"
date: 2026-06-02
categories:
    - misc
    - bio
    - video
description: "Idenitfying some miraculin-like proteins, extracting them and tasting them (null result)"
image: "images/prot_extract-Cover.jpg"
---

I has messing about exploring the newly-released [ESM Protein Atlas](https://biohub.ai/esm/protein/atlas), and since I'm working on a construct for miraculin expression I though I'd take a look for miraculin-like proteins using the similarity measures made available through the biohub team's models + SAEs. 

{{< video https://www.youtube.com/embed/mwGZb8zw83I >}}

I was able to use both the impressively helpful integrated agent and my own code w/ codex to find close matches. Turns out, a few edible plants had proteins with high similarity scores, so I set out to extract and taste the protein from some of these to see if I could detect any noticeable effects. The video summarizes the workflow. Alas, no taste changes I could notice, but I did get to taste some weird clover extract and misc proetin mush so, there's that :)

Protocol:

- 5g leaves, pulp or other plant material
- Chop up in ~20ml water with NaCl added to ~0.6M (e.g. 1.5g salt)
- Filter, add 80ml cold ethanol and leave it to sit (protein will precipitate out)
- Spin down the precipitate, add more eth to wash, spin down again (ditch supernatant)
- Resuspend in water to taste

I did a blind taste-test in one case where I though maybe there was an effect, but could tell no difference between the heated (and presumably denatured) version and the plain extract.

It is possible that

- The extraction process was too harsh
- The proteins of interest were too low concentration to detect
- I was using the wrong parts of the plant
- (most likely) the proteins tagged as similar to miraculin share structural similarities but have a different role

Anyway, fun excuse to mess about with protein models and do some crude salt extraction + ethanol precipitations.
