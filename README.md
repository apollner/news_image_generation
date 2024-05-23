# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Nathan Vasquez has sizable lead over Mike Schmidt in race to be Multnomah County district attorney**

You can read more about it [here](https://news.google.com/rss/articles/CBMidmh0dHBzOi8vd3d3Lm9wYi5vcmcvYXJ0aWNsZS8yMDI0LzA1LzIxL211bHRub21haC1jb3VudHktZGlzdHJpY3QtYXR0b3JuZXktbmF0aGFuLXZhc3F1ZXotbWlrZS1zY2htaWR0LXBvcnRsYW5kLW9yZWdvbi_SAYUBaHR0cHM6Ly93d3cub3BiLm9yZy9hcnRpY2xlLzIwMjQvMDUvMjEvbXVsdG5vbWFoLWNvdW50eS1kaXN0cmljdC1hdHRvcm5leS1uYXRoYW4tdmFzcXVlei1taWtlLXNjaG1pZHQtcG9ydGxhbmQtb3JlZ29uLz9vdXRwdXRUeXBlPWFtcA?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
