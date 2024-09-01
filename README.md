# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Fatman Scoop dies after collapsing on stage during US show**

You can read more about it [here](https://news.google.com/rss/articles/CBMiWkFVX3lxTFBfZk1PN2FyUmJJTlFrV01ZM2JfTWpFekhHX2hULUc4REVJanB0cVNHbm84b0RnMjFnaURfZmhrdEw0bWtjWWdBNFBIUVkzM19UMDJNalpPX1VvUdIBX0FVX3lxTE5LWVlTRll6RTZ3U1BtSkdLQ21GQU5TWkxKbTdqVVNpLXFGT1ZjRm1yTkhNZXJ3ZjEySlVZSlBvc0U5OTFScnllaFR6UEdJZnZsaU15N3BCTWhNZmlneHkw?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
