# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**2024 NFL Preseason Week 1 rookie grades: No. 1 overall pick Caleb Williams shines in Bears debut**

You can read more about it [here](https://news.google.com/rss/articles/CBMiuwFBVV95cUxPWEZvWVZzY0FxVmNyZThDVURfbEZOTnBLY2FsZDJuRFF6d2FxNHZuLUhyQ0NEMGJheHJtMWV3RktmcGNkX2pqUDN3b05vRlVmeElNb3NsSE43NTNZQlVjMVpQT3ozcTdTUFpscTE1bW9UOWxxT2Q5NEEyRUdFVjdPcjdTelNQRDBaX3VSb2dycGRmbklFeWJXaV9UTGd4bW0zaXNhZDBKVjRlXzBPQjNHOU1nLW9TM2xwVGJV?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
