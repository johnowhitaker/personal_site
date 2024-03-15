---
title: "Mini Experiment: Broken Multimodal Telephone"
date: 2024-03-14
categories: 
  - "mini-projects"
---

# Mini Experiment: Broken Multimodal Telephone

At a birthday party recently we played a game where a pad of paper is passed around a circle, with each person writing a sentence to describe a picture. The next person then draws a picture to match the sentence, and so on. The results are often hilarious, with the original sentence and the final picture often being completely different. Of course, the next day I had to replicate this with an image generation model and a multimodal model ping-ponging back and forth.

![](images/broken_telephone3.gif)

To generate the images, I went with Dalle-3 via the OpenAI API:

```python
from openai import OpenAI
openai_client = OpenAI(api_key="your_key")
response = openai_client.images.generate(
  model="dall-e-3",
  prompt="The dolphins have taken over the world. The dolphin king celebrates.",
  size="1024x1024",
  quality="standard",
  n=1,
)
image_url = response.data[0].url
```

This image URL can then be passed to Antropic's Haiku model, which is fantastically cheap and capable of taking both images and text as inputs:

```python
message = anthropic_client.messages.create(
    model="claude-3-haiku-20240307",
    max_tokens=100,
    temperature=0.5,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "image",
                    "source": {
                        "type": "base64",
                        "media_type": "image/png",
                        "data": base64.b64encode(httpx.get(image_url).content).decode("utf-8"),
                    },
                },
                {
                    "type": "text",
                    "text": "Provide a short description of the image."
                }
            ],
        }
    ],
)
prompt = message.content[0].text
```

Then prompt can be passed back to Dalle-3 to generate a new image, and so on. Here are a few GIFs with some results:

![](images/broken_telephone5.gif)

![](images/broken_telephone1.gif)

![](images/broken_telephone2.gif)

It's interesting to see how long these stay coherent. Previous times I've tried this things have gone abstract fairly quickly, here the theme diverges but does get stuck in attractors that still often make sense. I look forward to repeating this as models improve :) If you try this and make anything fun let me know! Here's how I make the GIFs:

```python
def save_results_as_gif(results, filename, time_per_frame=1):
    images = []
    for prompt, image in results:
        # Create a black image with the same size as the original image
        black_image = PILImage.new("RGB", image.size, (0, 0, 0))
        draw = ImageDraw.Draw(black_image)
        font = ImageFont.truetype("arial_narrow_7.ttf", 20)
        text = "Prompt: " + prompt

        # Add newlines to the text to roughly keep it within the image
        text_lines = []
        max_width = 80
        line = ''
        for word in text.split():
            if len(line + word) <= max_width:
                line += word + ' '
            else:
                text_lines.append(line)
                line = word + ' '
        text_lines.append(line)
        text = '\n'.join(text_lines)

        text_width, text_height = 800, 20
        text_position = ((image.width - text_width) // 2, (image.height - text_height) // 2)
        draw.text(text_position, text, font=font, fill=(255, 255, 255))

        # Append the black image and the original image to the list of frames
        images.append(black_image)
        images.append(image)

    # Save the frames as a GIF
    imageio.mimsave(filename, images, duration=time_per_frame)

# Example usage (results is a list of tuples of prompts and images)
save_results_as_gif(results, "broken_telephone1.gif", time_per_frame=1500)
```