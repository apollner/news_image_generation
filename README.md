# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Crew of Titan sub knew they were going to die before implosion, according to more than $50M lawsuit**

You can read more about it [here](https://news.google.com/rss/articles/CBMihwFBVV95cUxOOWNHZE5VUjNrSlc2bE93TWw4ZEV1ZndqdVNRX2UzTGZKY2d5anc2ZE55U3pSMWlaMVlwZ2FNU2xMVWlwa2ttbkhvVTBGR1RoRktmaVpvSGNwVFR5QjA5SmNwNGFjc0RSWllnNWI1QzRXTDAzclJrQ3FtU1VlRTFUaGd0dThZYnfSAX5BVV95cUxPWXJGWEM4R2lmZkp1dkpYU1BXR1dIOTVnSTJaRjBPQ0tzeG10TUllcnJfQnkzNE1scUZBbHg5SUdlQ0xsOEhUTEZhMGRoWFU3dk1sQ2lIam9DbUVtcnFpbWFGdUVqR2ZJNjgzeEQ4cHBMbGhZTWN1N1F4Zms3WVE?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
