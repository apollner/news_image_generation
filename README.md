# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Paris Olympics live updates: Scottie Scheffler wins gold; Suni Lee medals**

You can read more about it [here](https://news.google.com/rss/articles/CBMiqgFBVV95cUxNbEhqTXZRaENZMW5kbjRpcnY0Q3V4TTgzTWpvbTRYSEFhbFo2R28yc094VXpyNXktdEd4Z1psNlBFcmZqLWF5b0NpVXN4U3B5dkMyYURncklDanZtQ2JRaGE4Z0JnUUxIY3A2ZzcwN1ZYTmdRSXZaWU9iNGpzY19qNlVYODhUS1FQX242WlowOXBxNVRwdk1GclBISnV0ZVl2aFZIZUtmc3ppUQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
