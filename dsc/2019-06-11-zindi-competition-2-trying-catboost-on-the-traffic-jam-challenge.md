---
title: "Zindi Competition 2 - Trying CatBoost on the Traffic Jam Challenge"
date: "2019-06-11"
categories: 
  - "blogs"
tags: 
  - "catboost"
  - "jupyter"
  - "ml"
  - "python"
  - "uber"
  - "zindi"
---

Zindi ran a challenge predicting bus ticket sales into Nairobi. It is now closed, but we can still make predictions and see how they would have done. This was a very quick attempt, but I wanted to try out CatBoost, a magical new algorithm that's gaining popularity at the moment.

With a little massaging, the data looks like this:

![](images/screenshot-from-2019-06-11-11-05-03.png)

The 'travel\_time' (in minutes) and 'day' columns were derived from the initial datetime data. I'll spare you the code (it's available in [this GitHub repo](https://github.com/johnowhitaker/catboost_traffic_solution)) but I pulled in travel times from Uber Movement, and added them as an extra column. The test data looks the same, but lacks the 'Count' column - the thing we're trying to predict. Normally you'd have to do extra processing: encoding the categorical columns, scaling the numerical features... luckily, catboost makes it very easy:

![](images/screenshot-from-2019-06-11-11-13-48.png)

Training the model

This is convenient, and that would be enough reason to try this model first. As a bonus, they've implemented all sorts of goodness under the hood to do with categorical variable encoding, performance improvements etc. My submission (which took half an hour to implement) achieved a score of 4.21 on the test data, which beats about 75% of the leaderboard. And this is with almost no tweaking! If I spent ages adding features, playing with model parameters etc, I have no doubt this could come close to the winning submissions.

In conclusion, I think this is definitely a tool worth adding to my arsenal. It isn't magic, but for quick solutions it seems to give good performance out-of-the-box and simplifies data prep - a win for me.

This was a short post since I'm hoping to carry on working on the AI Art contest - expect more from that tomorrow!
