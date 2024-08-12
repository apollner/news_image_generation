# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Céline Dion Joins Trolls Condemning Donald Trump for Ironically Playing Her Smash Hit at His Rallies**

You can read more about it [here](https://news.google.com/rss/articles/CBMiygFBVV95cUxQWVppSlZjaktTM3o4OWhHWkt1OXRvNUY3UWhvb1ZadDlXM3RpM3g2cGV0Y3JqYnRILVlpUGlkRFpNRGRmVi1fNXdHZEV5QTdMai0teHc3c29zRy1BR1lXOWNyaV9xa3ZRV0hndVE4aUVHdlVKOWVGX0l0ejVGU0R0Rnk0N1RxbXduWU1oZmpRZnl0MUxtVzF0eDZJMGJwWmFCU0E2cXQ5XzJUUGtEeXFXbXhxQWhtZlFyQWRPQlozLW5tWWNvb1lhZkV3?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
