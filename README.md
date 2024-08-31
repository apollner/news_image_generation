# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**North Carolina QB Max Johnson Undergoes Season-Ending Surgery on Broken Leg**

You can read more about it [here](https://news.google.com/rss/articles/CBMikAFBVV95cUxQZ1FOR3FxRUhkdGhsZVY3VUYxRkVCV0ZYZ0NCZGtVLTVSUEducU5yUDJKdFBNdDJnS2F0OWU1ZE5nYXk4eXpxT1NoSHhDTlA0REVRRENGVTQzWnoydFpYbGY4czZxZ2Z3YzIxcG44WDJ0TFlGMkpCeFVWSjZlSW05SURMVG91ZGo1WmhEYUF5WXU?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
