# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**NBA Cup: Thunder advance to semifinals as Shai Gilgeous-Alexander scores 39, Luka Dončić sputters**

You can read more about it [here](https://news.google.com/rss/articles/CBMi0AFBVV95cUxPTjZkOE9sS2ZRLUFSbG9Cb1RsU055M0pseHY5endwcUhqTEVMUmdPRU5vcVNlaFlhWHZScmNISl9GNTU1WWhPeWhMaExjMTYzUGE5aHNMS082bmZIc0NJdnFVc0o2NVhWTXBtWUtLcEUtcEpiM2dVOGxGT3lQVER0ZDQ4Vl9yZGw0dGFqZXdSb3MzWThOSFdUMGw2UUM5RXY3VzRZRnNMWWV0cVRjT0hfTnY2NU85X09LUjBoNzJXcEF6TUhjck9jTHNBaE1RQTl6?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
