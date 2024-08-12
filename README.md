# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Walz in the National Guard: A Steady Rise Ending With a Hard Decision**

You can read more about it [here](https://news.google.com/rss/articles/CBMidkFVX3lxTE5NYklBTHFqVFpOMWZ1NE1sUENvcTI1a3ZOY1dsdVgzVkh5TTdlbkM4MDJJd2dCTmY5TlFYR2VHbnZYZDN5SEdETG9LRmlwX25tdjhaR0VmdF9lSjN3THZiWU9PcG0yUEtIdW41QV9lZHFobmVrT3c?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
