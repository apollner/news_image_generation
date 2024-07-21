# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Listeria outbreak linked to deli meat leaves 2 dead, 28 hospitalized: What to know**

You can read more about it [here](https://news.google.com/rss/articles/CBMiamh0dHBzOi8vd3d3LnVzYXRvZGF5LmNvbS9zdG9yeS9uZXdzL2hlYWx0aC8yMDI0LzA3LzIwL2xpc3RlcmlhLWRlbGktbWVhdC1vdXRicmVhay13aGF0LXN0YXRlcy83NDQ3ODQyMTAwNy_SAQA?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
