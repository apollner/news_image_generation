# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**REVEALED: Full list of Red Lobster restaurant closures as popular chain considers bankruptcy - find out if YOUR favorite is affected**

You can read more about it [here](https://news.google.com/rss/articles/CBMiZmh0dHBzOi8vd3d3LmRhaWx5bWFpbC5jby51ay95b3VybW9uZXkvYXJ0aWNsZS0xMzQxNjcyMy9MaXN0LXJlZC1sb2JzdGVyLWxvY2F0aW9ucy1jbG9zaW5nLWF1Y3Rpb24uaHRtbNIBAA?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
