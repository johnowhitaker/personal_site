---
title: "Packaging a classification model as a web app"
date: "2019-09-12"
categories: 
  - "blogs"
---

[![](https://datasciencecastnethome.files.wordpress.com/2019/09/screenshot-from-2019-09-12-13-03-18.png?w=1024)](https://zebra-vs-elephant.onrender.com)

My shiny new web app, available [here](https://zebra-vs-elephant.onrender.com)

In my [previous post](https://datasciencecastnet.home.blog/2019/09/06/pothole-detection-aka-johno-tries-fastai/) I introduced fastai, and used it to identify images with potholes. Since then, I've applied the same basic approach to the [Standard Bank Tech Impact Challenge: Animal classification](https://zindi.africa/competitions/sbtic-animal-classification) with pretty decent results. A first, rough model was able to score 97% accuracy thanks to the magic of transfer learning, and by unfreezing the inner layers and re-training with a lower learning rate I was able to up the accuracy to over 99% for this binary classification problem. It still blows my mind how good these networks are at computer vision.

![](https://datasciencecastnethome.files.wordpress.com/2019/09/screenshot-from-2019-09-12-11-36-03.png?w=840)

Zebra or Elephant?

This was exciting and fun. But I wanted to share the result, and my peer group aren't all that familiar with log-loss scores. How could I get the point across and communicate what this means? Time to deploy this model as a web application :)

## Exporting the model for later use

![](https://datasciencecastnethome.files.wordpress.com/2019/09/screenshot-from-2019-09-12-16-32-31.png?w=399)

Final training step, saving weights and exporting to a file in my Google Drive

I knew it was possible to save some of the model parameters with model.save('name'), but wasn't sure how easy it would be to get a complete model definition. Turns out, enough people want this that you can simply call model.export('model\_name'). So I set my model training again (I hadn't saved last time) and started researching my next step while Google did my computing for me.

## Packaging as an app

I expected this step to be rather laborious. I'd need to set up a basic app (planned to use Flask), get an environment with pytorch/fastai set up and deploy to a server or, just maybe, get it going on Heroku. But then I came across an exciting page in the fastai docs: '[Deploying on Render](https://course.fast.ai/deployment_render.html)'. There are essentially 3 steps:  
\- Fork the example repository  
\- Edit the file to add a link to your exported model  
\- Sign up with Render and point it at your new GitHub repository.  
Then hit deploy! You can read about the full process in the [aforementioned tutorial](https://course.fast.ai/deployment_render.html). Make sure your fastai is a recent version, and that you export the model (not just saving weights).

The resultant app is available at [zebra-vs-elephant.onrender.com](https://zebra-vs-elephant.onrender.com). I used an earlier model with 97% accuracy (since I'm enjoying that top spot on the leaderboard ;)) but it's still surprisingly accurate. It even get's cartoons right!

- ![](https://datasciencecastnethome.files.wordpress.com/2019/09/screenshot-from-2019-09-12-12-08-38.png?w=496)
    
- ![](https://datasciencecastnethome.files.wordpress.com/2019/09/screenshot-from-2019-09-12-12-08-57.png?w=403)
    
- ![](https://datasciencecastnethome.files.wordpress.com/2019/09/screenshot-from-2019-09-12-13-00-29.png?w=352)
    
- ![](https://datasciencecastnethome.files.wordpress.com/2019/09/screenshot-from-2019-09-12-13-00-43.png?w=414)
    
- ![](https://datasciencecastnethome.files.wordpress.com/2019/09/classify2.jpeg?w=270)
    
- ![](https://datasciencecastnethome.files.wordpress.com/2019/09/classify3.jpeg?w=281)
    

Please try it out and let me know what you think. It makes a best guess - see what it says for non-animals, or flatter your friends by classifying them as pachyderms.

## Conclusion

There seems to be a theme to my last few posts: "Things that sound hard are now easy!". It's an amazing world we live in. You can make something like this! It took 20 minutes, with me doing setup while the model trained! Comment here with links to your sandwich-or-not website, your am-I-awake app, your 'ask-a-computer-if-this-dolphin-looks-happy' business idea. Who knows, one of us might even make something useful :)

![](https://datasciencecastnethome.files.wordpress.com/2019/09/screenshot-from-2019-09-12-16-56-03.png?w=386)

Yes, that is apparently an elephant...

UPDATE: I've suspended the service for now, but can re-start it if you'd like to try it. Reach out if that's the case :)
