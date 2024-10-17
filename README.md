# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Russell Wilson takes first-team reps, is not on injury report**

You can read more about it [here](https://news.google.com/rss/articles/CBMivwFBVV95cUxQYU1rdmNlYjFVcFkwME9XVjYxTlhzYlNjN0Nic2tkRG1nUkxYYmFVd2Y4dXJ3OFdTT0dHX1RkQkpEbzJFdzdoYzBwZW1IU0V4WFV0LXpPWTZuNC05bnJwNDVENUVpQThaT0FOSnlHQzJvWXdBYlQ5SEE3ZGstNTE0dDc4QnhDVmMzMjliV2pSZUo2ZEY3N0FuMExhYzVaYlEyeGlGb1llVUUwOVc5SGRzRW5tUTY1MUI4QTdDeXRyYw?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
