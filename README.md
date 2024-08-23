# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**How Kamala Harris Is Preparing for the Biggest Speech of Her Life**

You can read more about it [here](https://news.google.com/rss/articles/CBMifkFVX3lxTE5oLUxoSmlfSzBtNkxKcDFGVkV1cGN2RW11Smx2VTlyRjRhVXh1dG1CQ1FrQ0Z0LU1pMm9mZGxRQS1oV20xX0g0S3htSlJXazd2c3lXeWxwSHBmN3dKRU5OVjMxZjRmX1lWbTRxZmx6aHhJU1ZwOEh3TlRYOEFidw?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
