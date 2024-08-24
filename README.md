# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Nestle replaces CEO Schneider with company veteran Freixe**

You can read more about it [here](https://news.google.com/rss/articles/CBMixAFBVV95cUxOU1RWSlp2b0dlajVlR05tLS13WDl2RjNrRnRXSU5rRzNfeHp4U3VYZjFZRWZyOGtudk50WEd6MzRnMEc0MGl1V2VWdDh5aFFicVdzNHFlMklyV0kzc3FxY2VmQktlbnJ5c01XNTQ4SUlBNE9HZWd4OUU5bG83bUFhelNNNDhwdl9iQXRBUXU0a3ZJZDBQOU5oVE9kYW5hUGdOUV9Ddm9QWUxNd3JRQ0dOR2FGVERBdFJqMkY5OWhreGg5cXdU?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
