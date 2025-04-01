---
title: Can AI Models Rhyme?
date: 2025-04-01
categories: 
    - mini-projects
---

Which word in ['Buoy', 'Employ', 'Decoy', 'Corduroy'] rhymes with 'Ennui'? I went looking for an online quiz with questions like this and figured it would make a good mini LLM eval. Without further ado, here are the results:

![images/rhyme_eval.png]

I put the full code in a gist [here](https://gist.github.com/johnowhitaker/b1ca1ac7e1814bf84aa52dde6d174277). It's pretty easy to knock together little evals like this! To make extracting the answers easy I used function calling, with TogetherAI for the open-source models and OpenAI for theirs. Since they all use the OpenAI API it was trivial to swap between them. As you can see if you skim my gist, I got AI to write the bulk of the code BUT did it in small enough pieces that I could check and tweak as needed.

For ease of replication, here are the questions (alas, this probably poisons this eval for future AIs but we can always make more!):

```python
qs = [{'question': 'Tough',
  'options': ['Chaff', 'Tariff', 'Cliff', 'Bluff'],
  'answer': 'Bluff'},
 {'question': 'Sigh',
  'options': ['Achy', 'Alloy', 'Fussy', 'Awry'],
  'answer': 'Awry'},
 {'question': 'Ennui',
  'options': ['Buoy', 'Employ', 'Decoy', 'Corduroy'],
  'answer': 'Buoy'},
 {'question': 'Ballet',
  'options': ['Gaffe', 'Cafe', 'Chafe', 'Strafe'],
  'answer': 'Cafe'},
 {'question': 'Marshal',
  'options': ['Impartial', 'Lethal', 'Patriarchal', 'Substantial'],
  'answer': 'Impartial'},
 {'question': 'Ignore',
  'options': ['Comport', 'Transport', 'Rapport', 'Purport'],
  'answer': 'Rapport'},
 {'question': 'Aisle',
  'options': ['Smile', 'Fuels', 'Spies', 'Else'],
  'answer': 'Smile'},
 {'question': 'Hymn',
  'options': ['Climb', 'Limb', 'Comb', 'Thumb'],
  'answer': 'Limb'},
 {'question': 'Stray',
  'options': ['Levee', 'Spree', 'Melee', 'Emcee'],
  'answer': 'Melee'},
 {'question': 'Bottom',
  'options': ['Solemn', 'Damn', 'Column', 'Autumn'],
  'answer': 'Autumn'},
 {'question': 'Deuce',
  'options': ['Mousse', 'Lacrosse', 'Posse', 'Finesse'],
  'answer': 'Mousse'},
 {'question': 'Subtle',
  'options': ['Hustle', 'Committal', 'Rebuttal', 'Acquittal'],
  'answer': 'Rebuttal'},
 {'question': 'Ukulele',
  'options': ['Oily', 'Icily', 'Daily', 'Lily'],
  'answer': 'Daily'},
 {'question': 'Spaghetti',
  'options': ['Sweaty', 'Reality', 'Dirty', 'Bounty'],
  'answer': 'Sweaty'},
 {'question': 'Queue',
  'options': ['Meow', 'Escrow', 'Straw', 'View'],
  'answer': 'View'}]
```