# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Sabrina Carpenter addresses rumor she had to ask Taylor Swift's permission to do Kim Kardashian clothing ad**

You can read more about it [here](https://news.google.com/rss/articles/CBMilgFBVV95cUxPYXBGVTR0WW5WcHZraHdDMmZCV2VNekxDOHZfNm5JcDEtSnpSY0RXVUgtVnA1alRIem5PZldWS3B3Y1dVaXdRTUZEN1RYT0hXUkpBMVdGZUFUZGhtaVlDZ09LX3ZPM1RLY2txWnRpdy1lemlDd3RjakFBOXh5WDFfYTJjaFE2WnFEOWExbWpRWl9Tb3dFWkE?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
