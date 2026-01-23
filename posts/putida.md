---
title: "Sequencing Pseudomonas putida + Bioinformatics & a Novel Pyoverdine Variant (DRAFT)"
date: 2026-01-22
categories:
    - bio
description: "I sequenced the genome of the pyoverdine-producing Pseudomonas from a previous post, and had some fun digging into the genes to figure out what molecule exactly it makes"
---

In my [previous post](https://johnowhitaker.dev/posts/pseudomonas.html) I showed a bacteria isolated from the water around the roots of a Jade plant on our windowsill, which secreted something that fluoresced a lovely blue under UV light. My best guess was that it was some species of Pseudomonas, and the blue was from pyoverdine. But how can we know for sure? Well, I put it off because money, but since I like working with this bacteria and want to do more with it, I figured I'd bite the bullet and pay the ~$120 to get my answers :) It turns out that the closest match is P. putida, and that the pyoverdine variant that this makes is probably different to anything documented in the literature. Exciting stuff!

## Sequencing with Plasmidsaurus

I went with Plasmidsaurus' 'Standard Bacterial Genome Sequencing with Extraction' [service](https://plasmidsaurus.com/genome). I sent the sample (~15mg cells suspended in Zymo DNA Shield) off on Tuesday morning and by Wednesday evening the results were ready. 

Species ID (Mash)

- Best match: Pseudomonas putida NBRC 14164
- Identity: 95.6% (1946/5000 shared hashes)

Genome Quality (CheckM)

- Completeness: 99.88% — excellent!
- Contamination: 2.15% — very low
- Lineage marker: Pseudomonas

Assembly Stats

- Genome size: 6.54 Mb (typical for Pseudomonas)
- Total reads: 66,830 (398 Mb total)
- Estimated coverage: ~58x
- Longest read: 88.4 kb
- Read N50: 9.7 kb

![](images/pseud_contig.png)

They give you [lots of data](https://drive.google.com/drive/folders/1p8dQGtGOjfowySz2ltuYEjhGZroxdjUh?usp=sharing), including annotating the genome for you with [bakta](https://doi.org/10.1099/mgen.0.000685). Great stuff! We can see right away that our guess was right - this is a Pseudomonas species (P. putida is the closest match) and are ready to dig in further to see what we can learn.

## Pyoverdine Investigation

Pyoverdines vary but all come with three key parts: a dihydroxyquinoline core, a peptide chain, and a side chain. The peptide chain especially varies strain-to-strain - see [here](https://en.wikipedia.org/wiki/Pyoverdine#Structure) for some examples.

Step one was looking for the pyoverdine Biosynthetic Gene Cluster (BGC). A [Deep Research](https://chatgpt.com/share/697294ce-6a40-8010-bb23-a7047045b8cb) run gave some promising genes to start the hunt with. Some hits let us narrow in on a key region between 4.71 and 4.76M bp, with a number of promising-looking genes. A tool called antiSMASH likewise identified a region (4,696,705–4,796,912), labeled as 'NRP-metallophore' - this is our BGC alright :)

![](images/antiSMASH.png)

We also got a predicted structure in SMILES format, and with some wrangling get a final predicted structure (and a pretty picture):

![](images/pyoverdine_precursor_pred.png)

::: {.callout-note collapse="true"}
## AN AI SUMARY OF 

🧠🧠🧠🧠🧠🧠🧠🧠🧠🧠🧠🧠🧠🧠🧠🧠🧠

### From Genome to Siderophore: Characterizing a Novel Pyoverdine from *Pseudomonas putida*

### The Starting Point

We began with a high-quality assembled genome from a *Pseudomonas putida* strain isolated from a houseplant root system (sequenced by Plasmidsaurus). The assembly was excellent: **99.88% complete**, only 2.15% contamination, and a 6.54 Mb genome at ~58× coverage. Species identity was confirmed via Mash (95.6% to *P. putida* NBRC 14164).

### Finding the Pyoverdine Biosynthetic Gene Cluster

We searched the Bakta annotations for pyoverdine-related genes (**pvd** genes, NRPS, siderophore terms) and identified a cluster spanning **~4.7–4.8 Mb** containing:

- **pvdT** — pyoverdine exporter
- **Two large NRPS genes** (~14.7 kb and ~6.4 kb) — the peptide assembly machinery
- **PvdA-like monooxygenase** — hydroxylates ornithine
- **Formylglycine-generating enzyme** (likely **pvdF**) — formyltransferase
- **argD** — makes diaminobutyrate (Dab), essential for the chromophore
- **TonB-dependent receptor** — likely the ferripyoverdine receptor (fpvA)

Notably, **pvdA** was located separately at ~3.99 Mb — this split arrangement is common in pyoverdine BGCs.

### antiSMASH Analysis

Running the genome through antiSMASH confirmed Region 10 as an **NRP-metallophore** cluster (siderophore NRPS). The top KnownClusterBlast hit was **Pf-5 pyoverdine** from *Pseudomonas protegens*, but with only ~49% NRPS identity — indicating a related but distinct peptide.

### Predicting the Peptide Sequence

antiSMASH provided **A-domain substrate predictions** for each NRPS module:

| Module | Substrate | Configuration |
|--------|-----------|---------------|
| 1 | Glu | L |
| 2 | Tyr | D (E-domain present) |
| 3 | Dab | L |
| 4 | Asp | L |
| 5 | Ala | L |
| 6 | Asp | L |
| 7 | OH-Orn | D (E-domain present) |
| 8 | **?** | — |
| 9 | OH-Orn | L |

The mystery at position 8 was annotated as **"NH₂"** by the Minowa predictor — initially puzzling.

### Resolving the Unknown Residue

We explored two hypotheses:

1. **Lysine** — has a terminal -NH₂ on its side chain
2. **Glycine** — essentially just an α-amino group with no real side chain

After deeper analysis (including literature review of other *P. putida* pyoverdines), **glycine emerged as the more likely candidate**:
- The "NH₂" prediction could mean "minimal/no side chain"
- Glycine is common in mid-chain positions of *P. putida* pyoverdines (KT2440, GB-1 both contain Gly)
- Prediction tools are known to have difficulty with Gly vs Ala

### Determining the Side Chain: pvdN vs ptaA

Pyoverdine side chains come in two main types:
- **Succinamide** — produced by strains with **pvdN**
- **α-Ketoglutarate** — produced by strains with **ptaA**

We BLASTed known pvdN (*P. aeruginosa* PAO1, NP_251095.1) and ptaA sequences against the genome:

- **pvdN: 83% identity match** → gene LDMLEE_03614 at ~3.99 Mb (near pvdA)
- **ptaA: No significant match**

**Conclusion: Succinamide side chain**

### The Final Predicted Structure

```
CHROMOPHORE PRECURSORS          VARIABLE PEPTIDE
        ↓                              ↓
┌───────────────────┐  ┌─────────────────────────────────────┐
 L-Glu → D-Tyr → L-Dab → L-Asp → L-Ala → L-Asp → D-OHOrn → Gly → L-OHOrn
                  ↓                                    ↓            ↓
           cyclizes to form                      Fe³⁺ binding  Fe³⁺ binding
        dihydroxyquinoline                       (hydroxamate) (hydroxamate)
           chromophore
```

**Key features:**
- **9-residue peptide** (longer than typical *P. putida* pyoverdines)
- **Two hydroxyornithine residues** — provides two hydroxamate groups for Fe³⁺ chelation
- **Succinamide side chain** on the chromophore
- **Novel sequence** — no match in SIDERITE database (best similarity only 0.35)

### SMILES (with stereochemistry)

```
NN[C@@H](CCC(=O)O)C(=O)N[C@H](Cc1ccc(O)cc1)C(=O)N[C@@H](CCN)C(=O)N[C@@H](CC(=O)O)C(=O)N[C@@H](C)C(=O)N[C@@H](CC(=O)O)C(=O)N[C@H](CCCNO)C(=O)NCC(=O)N[C@@H](CCCNO)C(=O)O
```

### What Still Needs Confirmation

This is a **bioinformatic prediction**. To definitively confirm the structure:

1. **LC-MS/MS** — will reveal the exact mass and fragment pattern, confirming each residue (especially Gly at position 8)
2. **The hydroxamates** — could be N-formylated (if pvdF is active), which would add +28 Da per residue
3. **Cyclization** — the C-terminal OHOrn likely cyclizes with the chromophore, which MS/MS should reveal

### Why This Matters

This appears to be a **genuinely novel pyoverdine variant** — it doesn't match any characterized *P. putida* pyoverdines in the literature or databases. Discovering the diversity of siderophores in environmental isolates helps us understand:

- Microbial competition for iron in the rhizosphere
- The evolution of NRPS systems
- Potential for novel iron chelators with biotechnology applications

## END AI SLOP
:::

Here's [a notebook](https://gist.github.com/johnowhitaker/8659d6f38c799e9d4d8e417e1641e6e0) running over the final steps, with some light annotation.

## Future Plans

It's one thing to poke at a genome and predict a structure, it's another entirely to verify it. I'm hoping to work with a local university to run GC-MS on this to answer a few remaining questions and nail down the final structure exactly. Will require dusting off and improving my organic chemistry and learning a lot more! Stay tuned for that in some future blog post hopefully :)

Also, it's probably obvious but worth stating explicityl: I AM OUT OF MY DEPTH HERE AND EVERYTHING IN THIS POST SHOULD BE TAKEN WITH A GRAIN OF SALT, ESPECIALLY WHILE IT IS MARKED 'DRAFT' :)

For the curious, raw data [is on Google Drive](https://drive.google.com/drive/folders/1p8dQGtGOjfowySz2ltuYEjhGZroxdjUh?usp=sharing), I'm open to questions @johnowhitaker. [This solveit dialog](https://share.solve.it.com/d/7584c91e2c239ff2c01ecd5fb270a3c7) has the key code in a nice rendered form.

## PS: Molecule viewer test

Here's the molecule, copied from the output of [this code](https://gist.github.com/johnowhitaker/81ed1c6eb4496556cca9792107c85832):

<div class="space-y-3"><div id="3dmolviewer_1769122862701931" style="position: relative; width: 400px; height: 300px;">
        
        <canvas id="undefined" width="1000" height="750" style="width: 400px; height: 300px; padding: 0px; position: absolute; top: 0px; left: 0px; z-index: 0;"></canvas><canvas id="undefined" width="1000" height="750" style="width: 400px; height: 300px; padding: 0px; position: absolute; top: 0px; left: 0px; z-index: 0;"></canvas></div>
<script>

var loadScriptAsync = function(uri){
  return new Promise((resolve, reject) => {
    //this is to ignore the existence of requirejs amd
    var savedexports, savedmodule;
    if (typeof exports !== 'undefined') savedexports = exports;
    else exports = {}
    if (typeof module !== 'undefined') savedmodule = module;
    else module = {}

    var tag = document.createElement('script');
    tag.src = uri;
    tag.async = true;
    tag.onload = () => {
        exports = savedexports;
        module = savedmodule;
        resolve();
    };
  var firstScriptTag = document.getElementsByTagName('script')[0];
  firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);
});
};

if(typeof $3Dmolpromise === 'undefined') {
$3Dmolpromise = null;
  $3Dmolpromise = loadScriptAsync('https://cdn.jsdelivr.net/npm/3dmol@2.5.4/build/3Dmol-min.js');
}

var viewer_1769122862701931 = null;
var warn = document.getElementById("3dmolwarning_1769122862701931");
if(warn) {
    warn.parentNode.removeChild(warn);
}
$3Dmolpromise.then(function() {
viewer_1769122862701931 = $3Dmol.createViewer(document.getElementById("3dmolviewer_1769122862701931"),{backgroundColor:"white"});
viewer_1769122862701931.zoomTo();
	viewer_1769122862701931.addModel("\n     RDKit          3D\n\n136136  0  0  0  0  0  0  0  0999 V2000\n   -6.6151   -0.7552   -3.4462 N   0  0  0  0  0  0  0  0  0  0  0  0\n   -7.0017    0.2169   -2.4168 C   0  0  1  0  0  0  0  0  0  0  0  0\n   -7.7288    1.4440   -2.9763 C   0  0  0  0  0  0  0  0  0  0  0  0\n   -9.0112    1.1321   -3.7521 C   0  0  0  0  0  0  0  0  0  0  0  0\n   -9.6584    2.3947   -4.2537 C   0  0  0  0  0  0  0  0  0  0  0  0\n   -9.1281    3.4847   -4.3971 O   0  0  0  0  0  0  0  0  0  0  0  0\n  -10.9498    2.2082   -4.5886 O   0  0  0  0  0  0  0  0  0  0  0  0\n   -7.8521   -0.4792   -1.3316 C   0  0  0  0  0  0  0  0  0  0  0  0\n   -8.6439   -1.3865   -1.5735 O   0  0  0  0  0  0  0  0  0  0  0  0\n   -7.6574    0.0198   -0.0633 N   0  0  0  0  0  0  0  0  0  0  0  0\n   -8.5164   -0.3636    1.0610 C   0  0  2  0  0  0  0  0  0  0  0  0\n   -9.8384    0.4264    1.1240 C   0  0  0  0  0  0  0  0  0  0  0  0\n   -9.7679    1.8828    0.7053 C   0  0  0  0  0  0  0  0  0  0  0  0\n   -8.9777    2.8041    1.4016 C   0  0  0  0  0  0  0  0  0  0  0  0\n   -8.9042    4.1326    0.9787 C   0  0  0  0  0  0  0  0  0  0  0  0\n   -9.6240    4.5477   -0.1345 C   0  0  0  0  0  0  0  0  0  0  0  0\n   -9.5082    5.8499   -0.5194 O   0  0  0  0  0  0  0  0  0  0  0  0\n  -10.4428    3.6590   -0.8184 C   0  0  0  0  0  0  0  0  0  0  0  0\n  -10.5132    2.3273   -0.3991 C   0  0  0  0  0  0  0  0  0  0  0  0\n   -7.6878   -0.2979    2.3608 C   0  0  0  0  0  0  0  0  0  0  0  0\n   -8.0723    0.2481    3.3912 O   0  0  0  0  0  0  0  0  0  0  0  0\n   -6.4952   -1.0011    2.2854 N   0  0  0  0  0  0  0  0  0  0  0  0\n   -5.6185   -1.1581    3.4492 C   0  0  1  0  0  0  0  0  0  0  0  0\n   -6.2188   -2.0839    4.5248 C   0  0  0  0  0  0  0  0  0  0  0  0\n   -6.3963   -3.5288    4.0464 C   0  0  0  0  0  0  0  0  0  0  0  0\n   -6.9688   -4.3442    5.1118 N   0  0  0  0  0  0  0  0  0  0  0  0\n   -4.2015   -1.6477    3.0755 C   0  0  0  0  0  0  0  0  0  0  0  0\n   -3.3292   -1.8373    3.9236 O   0  0  0  0  0  0  0  0  0  0  0  0\n   -4.0019   -1.9044    1.7326 N   0  0  0  0  0  0  0  0  0  0  0  0\n   -2.7034   -2.3975    1.2685 C   0  0  1  0  0  0  0  0  0  0  0  0\n   -2.8950   -3.3536    0.0900 C   0  0  0  0  0  0  0  0  0  0  0  0\n   -1.5946   -3.7673   -0.5302 C   0  0  0  0  0  0  0  0  0  0  0  0\n   -1.3548   -3.7718   -1.7260 O   0  0  0  0  0  0  0  0  0  0  0  0\n   -0.6690   -4.1212    0.3846 O   0  0  0  0  0  0  0  0  0  0  0  0\n   -1.8323   -1.1885    0.8523 C   0  0  0  0  0  0  0  0  0  0  0  0\n   -2.3118   -0.1884    0.3252 O   0  0  0  0  0  0  0  0  0  0  0  0\n   -0.4840   -1.3560    1.0838 N   0  0  0  0  0  0  0  0  0  0  0  0\n    0.5460   -0.5463    0.4382 C   0  0  1  0  0  0  0  0  0  0  0  0\n    1.4120    0.1456    1.4762 C   0  0  0  0  0  0  0  0  0  0  0  0\n    1.3962   -1.5073   -0.4244 C   0  0  0  0  0  0  0  0  0  0  0  0\n    1.3456   -2.7339   -0.2921 O   0  0  0  0  0  0  0  0  0  0  0  0\n    2.2357   -0.9102   -1.3381 N   0  0  0  0  0  0  0  0  0  0  0  0\n    3.0789   -1.7397   -2.2056 C   0  0  1  0  0  0  0  0  0  0  0  0\n    3.5303   -0.9925   -3.4633 C   0  0  0  0  0  0  0  0  0  0  0  0\n    4.5496    0.0402   -3.0881 C   0  0  0  0  0  0  0  0  0  0  0  0\n    4.3977    0.8650   -2.1953 O   0  0  0  0  0  0  0  0  0  0  0  0\n    5.7134   -0.1104   -3.7411 O   0  0  0  0  0  0  0  0  0  0  0  0\n    4.3018   -2.3108   -1.4473 C   0  0  0  0  0  0  0  0  0  0  0  0\n    4.8576   -3.3478   -1.8052 O   0  0  0  0  0  0  0  0  0  0  0  0\n    4.8370   -1.4907   -0.4639 N   0  0  0  0  0  0  0  0  0  0  0  0\n    6.1396   -1.8296    0.0968 C   0  0  2  0  0  0  0  0  0  0  0  0\n    6.4054   -1.2404    1.4926 C   0  0  0  0  0  0  0  0  0  0  0  0\n    5.8851    0.1736    1.7937 C   0  0  0  0  0  0  0  0  0  0  0  0\n    6.4956    1.2673    0.9227 C   0  0  0  0  0  0  0  0  0  0  0  0\n    6.0387    2.6005    1.3279 N   0  0  0  0  0  0  0  0  0  0  0  0\n    6.7366    2.9043    2.5687 O   0  0  0  0  0  0  0  0  0  0  0  0\n    7.2660   -1.4847   -0.9093 C   0  0  0  0  0  0  0  0  0  0  0  0\n    7.2494   -0.4972   -1.6470 O   0  0  0  0  0  0  0  0  0  0  0  0\n    8.3267   -2.3618   -0.8948 N   0  0  0  0  0  0  0  0  0  0  0  0\n    9.3494   -2.3715   -1.9370 C   0  0  0  0  0  0  0  0  0  0  0  0\n   10.5717   -1.5281   -1.5723 C   0  0  0  0  0  0  0  0  0  0  0  0\n   11.7192   -1.9478   -1.7134 O   0  0  0  0  0  0  0  0  0  0  0  0\n   10.2854   -0.2356   -1.1853 N   0  0  0  0  0  0  0  0  0  0  0  0\n   11.3126    0.6002   -0.5724 C   0  0  1  0  0  0  0  0  0  0  0  0\n   11.1216    2.0813   -0.9180 C   0  0  0  0  0  0  0  0  0  0  0  0\n    9.8109    2.6920   -0.3987 C   0  0  0  0  0  0  0  0  0  0  0  0\n    9.7221    4.1810   -0.7540 C   0  0  0  0  0  0  0  0  0  0  0  0\n    8.5066    4.8221   -0.2402 N   0  0  0  0  0  0  0  0  0  0  0  0\n    7.3957    4.2118   -0.9549 O   0  0  0  0  0  0  0  0  0  0  0  0\n   11.3203    0.3602    0.9403 C   0  0  0  0  0  0  0  0  0  0  0  0\n   10.4579   -0.2116    1.5958 O   0  0  0  0  0  0  0  0  0  0  0  0\n   12.4089    0.8703    1.5479 O   0  0  0  0  0  0  0  0  0  0  0  0\n   -7.4240   -1.3231   -3.6980 H   0  0  0  0  0  0  0  0  0  0  0  0\n   -6.3168   -0.2721   -4.2919 H   0  0  0  0  0  0  0  0  0  0  0  0\n   -6.0742    0.5621   -1.9441 H   0  0  0  0  0  0  0  0  0  0  0  0\n   -7.9745    2.1237   -2.1557 H   0  0  0  0  0  0  0  0  0  0  0  0\n   -7.0413    2.0007   -3.6261 H   0  0  0  0  0  0  0  0  0  0  0  0\n   -9.7258    0.6166   -3.1045 H   0  0  0  0  0  0  0  0  0  0  0  0\n   -8.8014    0.5009   -4.6229 H   0  0  0  0  0  0  0  0  0  0  0  0\n  -11.2422    3.0698   -4.9501 H   0  0  0  0  0  0  0  0  0  0  0  0\n   -7.1668    0.9029    0.0276 H   0  0  0  0  0  0  0  0  0  0  0  0\n   -8.7787   -1.4245    0.9436 H   0  0  0  0  0  0  0  0  0  0  0  0\n  -10.2870    0.3702    2.1227 H   0  0  0  0  0  0  0  0  0  0  0  0\n  -10.5526   -0.0835    0.4583 H   0  0  0  0  0  0  0  0  0  0  0  0\n   -8.4217    2.5109    2.2901 H   0  0  0  0  0  0  0  0  0  0  0  0\n   -8.2870    4.8438    1.5186 H   0  0  0  0  0  0  0  0  0  0  0  0\n   -9.9747    5.9667   -1.3639 H   0  0  0  0  0  0  0  0  0  0  0  0\n  -11.0310    3.9804   -1.6735 H   0  0  0  0  0  0  0  0  0  0  0  0\n  -11.1552    1.6421   -0.9427 H   0  0  0  0  0  0  0  0  0  0  0  0\n   -6.4017   -1.6561    1.5147 H   0  0  0  0  0  0  0  0  0  0  0  0\n   -5.4964   -0.1581    3.8823 H   0  0  0  0  0  0  0  0  0  0  0  0\n   -7.1919   -1.6920    4.8523 H   0  0  0  0  0  0  0  0  0  0  0  0\n   -5.5659   -2.0769    5.4085 H   0  0  0  0  0  0  0  0  0  0  0  0\n   -5.4314   -3.9631    3.7575 H   0  0  0  0  0  0  0  0  0  0  0  0\n   -7.0566   -3.5698    3.1756 H   0  0  0  0  0  0  0  0  0  0  0  0\n   -7.8757   -3.9706    5.3915 H   0  0  0  0  0  0  0  0  0  0  0  0\n   -7.1387   -5.2901    4.7738 H   0  0  0  0  0  0  0  0  0  0  0  0\n   -4.4537   -1.2402    1.1064 H   0  0  0  0  0  0  0  0  0  0  0  0\n   -2.2108   -2.9248    2.0947 H   0  0  0  0  0  0  0  0  0  0  0  0\n   -3.4940   -2.8662   -0.6903 H   0  0  0  0  0  0  0  0  0  0  0  0\n   -3.4410   -4.2526    0.3977 H   0  0  0  0  0  0  0  0  0  0  0  0\n    0.1879   -4.0867   -0.1123 H   0  0  0  0  0  0  0  0  0  0  0  0\n   -0.1762   -2.2691    1.4186 H   0  0  0  0  0  0  0  0  0  0  0  0\n    0.0786    0.1899   -0.2260 H   0  0  0  0  0  0  0  0  0  0  0  0\n    0.8120    0.8269    2.0879 H   0  0  0  0  0  0  0  0  0  0  0  0\n    1.8841   -0.5800    2.1524 H   0  0  0  0  0  0  0  0  0  0  0  0\n    2.2130    0.7265    1.0089 H   0  0  0  0  0  0  0  0  0  0  0  0\n    2.3996    0.0938   -1.3059 H   0  0  0  0  0  0  0  0  0  0  0  0\n    2.4703   -2.6042   -2.5136 H   0  0  0  0  0  0  0  0  0  0  0  0\n    3.9814   -1.7008   -4.1694 H   0  0  0  0  0  0  0  0  0  0  0  0\n    2.6922   -0.4957   -3.9710 H   0  0  0  0  0  0  0  0  0  0  0  0\n    6.4124    0.2136   -3.1233 H   0  0  0  0  0  0  0  0  0  0  0  0\n    4.5844   -0.5089   -0.5171 H   0  0  0  0  0  0  0  0  0  0  0  0\n    6.1581   -2.9216    0.2138 H   0  0  0  0  0  0  0  0  0  0  0  0\n    5.9355   -1.9057    2.2267 H   0  0  0  0  0  0  0  0  0  0  0  0\n    7.4807   -1.2694    1.7025 H   0  0  0  0  0  0  0  0  0  0  0  0\n    6.1051    0.3840    2.8471 H   0  0  0  0  0  0  0  0  0  0  0  0\n    4.7928    0.1904    1.7048 H   0  0  0  0  0  0  0  0  0  0  0  0\n    6.1797    1.1327   -0.1133 H   0  0  0  0  0  0  0  0  0  0  0  0\n    7.5882    1.2151    0.9461 H   0  0  0  0  0  0  0  0  0  0  0  0\n    6.4469    3.2816    0.6749 H   0  0  0  0  0  0  0  0  0  0  0  0\n    5.9941    3.1631    3.1515 H   0  0  0  0  0  0  0  0  0  0  0  0\n    8.2435   -3.2077   -0.3454 H   0  0  0  0  0  0  0  0  0  0  0  0\n    9.6664   -3.4118   -2.0625 H   0  0  0  0  0  0  0  0  0  0  0  0\n    8.9299   -2.0093   -2.8807 H   0  0  0  0  0  0  0  0  0  0  0  0\n    9.3196   -0.0623   -0.9284 H   0  0  0  0  0  0  0  0  0  0  0  0\n   12.2878    0.2740   -0.9538 H   0  0  0  0  0  0  0  0  0  0  0  0\n   11.1603    2.2030   -2.0083 H   0  0  0  0  0  0  0  0  0  0  0  0\n   11.9648    2.6547   -0.5065 H   0  0  0  0  0  0  0  0  0  0  0  0\n    8.9621    2.1560   -0.8385 H   0  0  0  0  0  0  0  0  0  0  0  0\n    9.7528    2.5742    0.6890 H   0  0  0  0  0  0  0  0  0  0  0  0\n   10.5797    4.7025   -0.3140 H   0  0  0  0  0  0  0  0  0  0  0  0\n    9.7872    4.3239   -1.8375 H   0  0  0  0  0  0  0  0  0  0  0  0\n    8.3401    4.5252    0.7269 H   0  0  0  0  0  0  0  0  0  0  0  0\n    6.9409    4.9959   -1.3276 H   0  0  0  0  0  0  0  0  0  0  0  0\n   12.3044    0.6155    2.4895 H   0  0  0  0  0  0  0  0  0  0  0  0\n  1  2  1  0\n  2  3  1  0\n  3  4  1  0\n  4  5  1  0\n  5  6  2  0\n  5  7  1  0\n  2  8  1  0\n  8  9  2  0\n  8 10  1  0\n 10 11  1  0\n 11 12  1  0\n 12 13  1  0\n 13 14  2  0\n 14 15  1  0\n 15 16  2  0\n 16 17  1  0\n 16 18  1  0\n 18 19  2  0\n 11 20  1  0\n 20 21  2  0\n 20 22  1  0\n 22 23  1  0\n 23 24  1  0\n 24 25  1  0\n 25 26  1  0\n 23 27  1  0\n 27 28  2  0\n 27 29  1  0\n 29 30  1  0\n 30 31  1  0\n 31 32  1  0\n 32 33  2  0\n 32 34  1  0\n 30 35  1  0\n 35 36  2  0\n 35 37  1  0\n 37 38  1  0\n 38 39  1  0\n 38 40  1  0\n 40 41  2  0\n 40 42  1  0\n 42 43  1  0\n 43 44  1  0\n 44 45  1  0\n 45 46  2  0\n 45 47  1  0\n 43 48  1  0\n 48 49  2  0\n 48 50  1  0\n 50 51  1  0\n 51 52  1  0\n 52 53  1  0\n 53 54  1  0\n 54 55  1  0\n 55 56  1  0\n 51 57  1  0\n 57 58  2  0\n 57 59  1  0\n 59 60  1  0\n 60 61  1  0\n 61 62  2  0\n 61 63  1  0\n 63 64  1  0\n 64 65  1  0\n 65 66  1  0\n 66 67  1  0\n 67 68  1  0\n 68 69  1  0\n 64 70  1  0\n 70 71  2  0\n 70 72  1  0\n 19 13  1  0\n  1 73  1  0\n  1 74  1  0\n  2 75  1  1\n  3 76  1  0\n  3 77  1  0\n  4 78  1  0\n  4 79  1  0\n  7 80  1  0\n 10 81  1  0\n 11 82  1  6\n 12 83  1  0\n 12 84  1  0\n 14 85  1  0\n 15 86  1  0\n 17 87  1  0\n 18 88  1  0\n 19 89  1  0\n 22 90  1  0\n 23 91  1  1\n 24 92  1  0\n 24 93  1  0\n 25 94  1  0\n 25 95  1  0\n 26 96  1  0\n 26 97  1  0\n 29 98  1  0\n 30 99  1  1\n 31100  1  0\n 31101  1  0\n 34102  1  0\n 37103  1  0\n 38104  1  6\n 39105  1  0\n 39106  1  0\n 39107  1  0\n 42108  1  0\n 43109  1  6\n 44110  1  0\n 44111  1  0\n 47112  1  0\n 50113  1  0\n 51114  1  1\n 52115  1  0\n 52116  1  0\n 53117  1  0\n 53118  1  0\n 54119  1  0\n 54120  1  0\n 55121  1  0\n 56122  1  0\n 59123  1  0\n 60124  1  0\n 60125  1  0\n 63126  1  0\n 64127  1  6\n 65128  1  0\n 65129  1  0\n 66130  1  0\n 66131  1  0\n 67132  1  0\n 67133  1  0\n 68134  1  0\n 69135  1  0\n 72136  1  0\nM  END\n","mol");
	viewer_1769122862701931.setStyle({"stick": {"colorscheme": "greenCarbon", "radius": 0.15}});
	viewer_1769122862701931.setBackgroundColor("white");
	viewer_1769122862701931.zoomTo();
viewer_1769122862701931.render();
});
</script></div>