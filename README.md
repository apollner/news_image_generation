# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Robert Telles, former politician, found guilty in killing of Las Vegas journalist Jeff German, sentenced to life in prison**

You can read more about it [here](https://news.google.com/rss/articles/CBMiggFBVV95cUxOdWJybzh1RXQ3NjJ3MVVRTGVTWjZESnZSeUhlaDBZUnNIenpnS3hocEdYZkdrSzItcExMcUxYd0JlaGt3aGtxYk9waDNFWXNwdTVJRDBrSWRxV1dGTlQ1S3c3VXJwMUV0ZnhPZk5KQWxvYlk0a1E4bUdobnBlSGlFOUZR0gGHAUFVX3lxTE1JWWRQY0lLZmhRcVh6RWtGWXE0THFNcUZKNG4zMDRFekFxeXJIRnJDM3dfUDJXYW11XzN2N19qUlZZMDZfTDN0SEl3dnZiV21QcDJ0WmN0eUZhNi1DVXpmQTV0NF9hZVpnUld4Y2dwTnIxX0MwTlJVUlIySjlrTDBHQmhaWVVGUQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
