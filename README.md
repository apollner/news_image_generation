# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**From villains to Indiana Jones: Everything we learned at Disney’s parks panel at the 2024 D23 Expo**

You can read more about it [here](https://news.google.com/rss/articles/CBMipAFBVV95cUxPQWpucE9aWjg4QlNGUTJwM0htUFJJZnl6M1owUEt1bFNUWGxYc0VPUENkbXdYNU5lRmowY0pMX3hIazFvb2NjYVpEbW5mcm9GNWloSkptbEt3aFNHTmN4RU9iZUEzR184X1pZb2V3OGJzZG9rQUxuM0VXXy1XeUY2ZEFxWFVwMEg5ZF92dGRicW16UGFvTUh2eTVyVm80eWJBbnNZZNIBqgFBVV95cUxOZUJ5VWh0ZzM3ZUZ0cmNYU3RsYXdGcTlIRjJFbTNOaUM3V3FZV1I4RU1oWXlrUTJ5dDVnNWJCMXRsVjlpQ2ZxVlFscjRWc2NsSUEwY283MVVBVHExcV9mRWNRYkwxd21RbGJBNnZKRnFCMGRIOHlWY0xyU2ZXTzh1RWszZzNrTGZUWkt1djZsa3V4SFg1UzFGVDk2OVFUNE9QUGg4YUxLMnU1dw?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
