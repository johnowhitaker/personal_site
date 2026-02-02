---
title: "CNC Pipette, Misc Project Updates"
date: 2026-01-19
categories:
    - mini-hw-projects
    - bio
description: "Moving small drops of liquid around under computer control, updates on the biolistics projects, bulk glowy gelatinous blobs, friction welding, beer brewing."
---

I had a productive weekend, and should write it all up! Many projects are simmering away with long waits before they resolve, so I'm dumping them all in this post :)

## CNC Pipette

I've enjoyed hearing [Jason Kelly](https://x.com/jrkelly)'s take on why bio should abandon the lab bench and let automated labs (like the ones his company Ginkgo makes) do the work of moving liquids and things around, freeing up the smart minds to actually think about cool experiments rather than spending all their time on menial lab tasks. Sounds good, although I simultaneously think far more people should do a little lab stuff to open their minds to the realities of the real world, and worry how much might get missed if you only see what you set out to measure!

Anyway, with all that discussion fresh in my mind, one of the things I did this weekend was whip up an attachment for my 3D printer that holds my pipette and can suck up and dispense small amounts of liquid. End goal: agar art with colorful microbes, of course :D A Dynamixel servo that I had on hand pushes the plunger thingee on the pipette, with both it and the printer controlled by a raspberry pi or laptop (the latter after I ran the wrong G-Code and spilled colorful water on the former!).

![](images/cnc_pipette.png)

The [CAD](https://cad.onshape.com/documents/42cf135ce4b1a1a34746c4ee/w/bec91f2a6df1f3690807754b/e/2f528fdceb0af6a3583d11d3?renderMode=0&uiState=696e7b486f2ab6c24a30a134) and [code](https://github.com/johnowhitaker/pipette) are still WIP, contact me if you're interested in this or wait until the next weekend I feel like tidying it up + making a more thorough video documenting the project. My favourite result so far comes from the first test, before I dialed in liquid dispensing:

![](images/cnc_p_heart.png)
![](images/cnc_p_heart_result.png)

I've since done some agar art with my pet blue fluorescent Pseudomonas sp. that is growing out nicely - will upload pics once I make a few more artworks.

Update: I made a short with it in action: [https://www.youtube.com/shorts/He5VJz9E1lQ](https://www.youtube.com/shorts/He5VJz9E1lQ)

## Biolistics - ASGG tests

I haven't managed to find a way to get genes from addgene. A friend has kindly stepped in to help, and I might also cold-email some local profs in case any want to collaborate. But that means than for now, I don't really have a way to test the gene gun idea and won't for a few more weeks at least. Still, I did muck about a bit, starting with: carriers and DNA adhesion.

In regular gene guns, DNA is precipitated onto gold nanoparticles, which are then washed in ethanol and then mixed with something called PVP, which let's them then stick to plastic tubes or disks. The result is an even spread of DNA-coated gold balls. I'm planning to try a few things differently. One carrier I'm looking at is diatomaceous earth - sharpish fragments about the right size, high surface area. I've been putting little droplets of DE slurry on film (cling film or parafilm) and firing them without even waiting for the droplet to dry. 

One test was thus, can we stick DNA to DE? Both are ~slightly negatively charged, so I tried one test with DE slurry + plasmid soln (my ~failed BLY_GREEN) w/ methylene blue to stain the DNA + water, and a second with the same but 50mM CaCL2 solution instead of water. The CaCl2 contributes +ve calcium ions which might (the theory goes) form a bridge. Indeed, it seemed like the DE that settled out in the CaCl2 version was bluer than the whiteish version with just water. (A better test would be to use a better DNA stain to check the water bit to see how much DNA is left). In another test, DE mixed with DNA + MB both with and without CaCl2 was added to lots more water and then spun down in a diy centrifuge - the pellet in both was blue, but the water-only pellet rapidly disperse on handling while the CaCl2 version was stable - my suspicion is that it causes clumping (pro gene gun prep involves sonicating to break up clumps). If that's the case, then skipping the CaCl2 might be better - the DNA is still likely to coat the carrier if e.g. we let a drop evaporate and it is left with tons of surface area of silica DE vs a relatively small area of hydrophobic cling-film. More testing to do :)


![](images/blue_de.png)

I also explored penetration. My first attempt just had a wide attachment after the barrel, with film stretched across it. You had to get close to get much penetration, which also seemed to cause damage to the agar at least (using it as a transparent stand-in for plant matter). Testing it on onion it mostly penetrated only the 1st layer of cells. So, I modelled up a converging-diverging nozzle, with the film placed in the throat, and got much nicer results - less damage from air, more even penetration of the (presumably faster-moving) particles. In onion it sent some particles 5-10 cells deep on the first try :)

![](images/pen_test_mb.png)

## Biolistics - W wire tatoo approach

I did more tests with my mini tatoo gun concept, using a bundle of flame-sharpened tungsten wires (50-micron) to poke at an onion with some MB as a dye just to see what happens. The dye wipes away except where the wires (attached to an electric toothbrush) stabby-stabby stabbed the tissue.

![A bundle of tungsten wires, partially flame-sharpened](images/wneedlebundle.png)

![Most of the effect is in the top layer of cells](images/wneedle_results.png)

The wire is perhaps too flexible, and rapidly gets bent without penetrating much beyond the first layer - perhaps I should have started from thicker wire. Still, with some fiddling it seemed to eventually yield a setup that got some poki-ness happening. We'll see how it goes when I can try it with some actual DNA.

## Tissue Culture

As for what we'll actually transform, and how we'll grow out plants from a few transformed cells, I've been exploring tissue culture a little. Most of my experiments so far ended in contamination - some from an early media test just heating the media up to 96C rather than microwaving or autoclaving (which left one or two live spores or something per tub, nothing if you're doing a petri dish of bacteria for a few days, a dead pain if you're wanting to grow a piece of plant matter for months) but most from the explants themselves; it turns out you need really aggressive sterilization with bleach etc to kill everything but the plant tissue (and in the process you usually do kill a fair bit of the plant tissue too). Might try some other options soon.

![Sterilizing TC media in an Instapot](images/tc_update.png)

Anyway, now that I've switched to media sterilized in an Instapot and started being more aggressive with the explant sterilization, I feel like I'm slowly taming the beast. It's all super slow though - aaaah my poor software brain is spoiled from same-second results :D

## Glowing Gelatinous Blobs

I grow some of the [Pseudomonad I isolated](https://johnowhitaker.dev/posts/pseudomonas.html) in ~500ml of 'marmite broth' in a flask, with parafilm cover and occasional stirring. Then I added 1g CaCl2 to it, and dripped it into some water with sodium alginate - something the molacular gastronomy folks call 'reverse spherification'. The result is gooey blobs, which (thanks to all the pyoverdine the bacteria made) glow bright blue under UV light. I pictured cool fluorescent spheres I could sprinkle around the base of our plants, to provide them with a bacterial iron boost (but mostly for aesthetics). What I got was more of a congealed mess, but it was fun nonetheless.

![](images/glowgoo.png)

Handling the containers (post boiling + alcohol steriliation) stained my hands a lovely fluorescent yellow-green, some cool modification of the blue-fluorescing molecule(s) this makes. Neat! Invisible under regular light, and now mostly gone after a day of occasional washes and a shower. 

## Misc Updates

- Ran some Thai Tea concentrate (low C) and Puerh (very high C for tea) through caffeine TLC process

- Tried friction welding 3D prints with a dremel, cool technique!

![](images/friction_weld.png)

- Made a batch of beer from a kit - turned out extremely well, fermentation was stalled in my cold basement until I warmed it to 22C. Friends all agreed it was tasty, but none of us really like beer so I threw out most of it - sorry! Now the brew tank is destined for more exotic projects :D

OK that's about enough typing for now, apoligies for a lower-effort post but I figure better to document some stuff now rather than try to remember it all in months time when I start getting more final results on things.