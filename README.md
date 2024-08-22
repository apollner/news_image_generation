# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Jennifer Lopez has filed for divorce from Ben Affleck**

You can read more about it [here](https://news.google.com/rss/articles/CBMilAFBVV95cUxOZkd5eEp1Z2FiZ2Nrdjk1bW5HTm8yMlBUOGo2S21mTU5qUHdxTzl6NFd6aUlpZzVpMUxZM0dGN3M1OVBfc2NYSl9fVzNwZk1lYUJVT09kOVRXT19Fd0hISXdBbmVRQS1FQVFpYzlDRm96SFdrWUhLei1Kd2JCbUd2SGlsbGFZREJUUDZ6TjJGcHNraGh30gGLAUFVX3lxTE5FMEJld1BIZS1lQnZqSE55LVctQnpJdnZ0cG9oWElmd05jRVZPRjIwbFFQa3ZuUGNEWjgwajJGMlhCSTRjRU9aYkMtNFpVMFNyNURCOU5sVE41ZXdHSTRKSG9GRWVtMGQ5Zzd2RlBmNUR3LXhWRWxha3ZOWnFCWFJkSndhVEF0bFprMEE?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
