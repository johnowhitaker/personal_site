---
title: "Reading Genomes thanks to Plasmidsaurus"
date: 2025-11-06
categories:
    - misc
description: "Learning how easy it is becoming to sequence DNA and explore the results, via a case study on something goopy I found growing in my lab and an even stranger contaminant in Sebastian's Triton-X surfactrant solution."
---

When I encounter an organism, I like to know what it is. My wifge once asked me, puzzled, why I have this drive. I stand by my first answer: I want to know if I can eat it! Naming something allows us to cross-reference information about that thing - from recipes to life histories :) Birds are easy - they sell books with pictures. Same goes for mammals, mushrooms, plants etc - at least the common ones. Bugs and spiders are harder - for some, you have to look at their naughty bits under a microscope (annoyance at this fact prompted me to put lots of working into making photo guides!). When you get to bacteria, there's really no hope in most cases... at least, that's how I felt until recently! Turns out you can find out 'what is this' these days for a relatively modest sum of money, thanks to the magic of gene sequencing. In this post I'll share my first experience answering one such question, then dig into a case study with data from a friendly internet biologist to show how far one can explore with some free tools (and a bit of specialist know-how).

## What the floc is that?

TODO: picture of the flocs

Towards the end of my [duckweed experiments](https://johnowhitaker.dev/posts/dwebench.html), I noticed some things floating in some leftover stock solution of hydroponic nutrients I had made up. White, goopy blobs about a cm long. Was this some sort of weird precipitate? Some bacteria or yeast growing in there? A look under a microscope revealed a dense, tangled, squishy mess. A few tests ruled out mineral/chemical suspects, and after a bit of poking around my best answer was that these were probably biofilm flocs: mixed environmental microbes embedded in EPS (extracellular polysaccharide). That's *an* answer, but how do we narrow it down to something more specific?

Enter [Plasmidsaurus](https://plasmidsaurus.com/welcome). They offer a number of services. In this case, I went for their "Microbiome 16S Amplification & Sequencing with DNA Extraction" service. Following the guidance in the [sample prep](https://plasmidsaurus.com/sample-prep/microbiome#16S-extraction) docs, I suspended ~0.1g of the goo in a product called 'Zymo DNA shield' (after a quick wash + spin down in 0.9% saline) and shipped the result (in a tube in a tube in a bag in a bag just to be safe) off to their lab in the nearby town of Eugene.

TODO picture of the results

The 16S gene is "highly conserved between different species of bacteria and archaea" and gets used to tell what somethig is without reading the whole genome - perfect for analysing environmental samples, gut bacteria etc. Plasmidsaurus will give you the raw reads, but they also do some processing to tell you some relative abundances of different species present (see above). In my case, it turns out these flocs are not a siongle species but instead a whole happy community of microbes! It's fun to start researching and figuring out who might be doing what. Preliminary poking tells me this is not an unusual mix for a watery, nutrient-rich environment. Cool to see some [Methylobacterium present](https://x.com/allisonmegow/status/1983048944432353532) - wonder how they're getting food.

So, there you go. A much deeper answer to 'what is that', provided you're willing to ship off a sample of goop and pay $60 + reagents and shipping. Is this as far as we can go though? No! [Raw results here for the curous](https://x.com/johnowhitaker/status/1983004377318326522). To dive even deeper, I'm going to switch to exploring the example that inspired me to go down this rabbit hole: the case of the mysterious triton X infiltrator.

## Sebastian's Mystery Bug

![](images/tritonx.png)

Sebastian S. Cocioba🪄🌷 [@ATinyGreenCell](https://x.com/ATinyGreenCell) is an amateur biologist who is continually doing amazing science stuff. He noticed a contaminant growing in his surfactant solution - a rough environment to be a bacteria! We sent it off for sequencing, but this time being a pro the approach was a little fancier than the one I showed in the previous section. For one thing, he guessed that his contaminant was mostly one organism, a bacterium, and so went with the bacteria genome sequencing with extraction option on the friendlty dino site. This was a bit of an informed gamble - the kind of shortcut one can take with experience. 

He's been sharing [the data](https://drive.google.com/drive/folders/1VRWijxODY-tEz_SEpgFz_OVNyNp6obG4) and his explorations on X.

The main result from the run this time is a file with the reads: `K9P4V9_1_CONTAM-1.fastq`. 

TODO
- SHow code to read genome, BLAST, download or assemble a complete genome, annotate, explore.
- Talk about how many are just hypothetical proteins
- https://x.com/ATinyGreenCell/status/1981428984832278974, 
- Talk about the next phase of his plan https://x.com/ATinyGreenCell/status/1981806002975719504 namely culture, confirm ID with plasmids, play with bug
- Reference genome size and overlap needed to assemble
- Play with genomes available for download
- Pick a protein or 10 and visualize
- ...
