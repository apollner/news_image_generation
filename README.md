# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Cubs to acquire Rays third baseman Isaac Paredes in trade deadline move for offensive power, per report**

You can read more about it [here](https://news.google.com/rss/articles/CBMiigFodHRwczovL3d3dy5jYnNzcG9ydHMuY29tL21sYi9uZXdzL2N1YnMtdG8tYWNxdWlyZS1yYXlzLXRoaXJkLWJhc2VtYW4taXNhYWMtcGFyZWRlcy1pbi10cmFkZS1kZWFkbGluZS1tb3ZlLWZvci1vZmZlbnNpdmUtcG93ZXItcGVyLXJlcG9ydC_SAY4BaHR0cHM6Ly93d3cuY2Jzc3BvcnRzLmNvbS9tbGIvbmV3cy9jdWJzLXRvLWFjcXVpcmUtcmF5cy10aGlyZC1iYXNlbWFuLWlzYWFjLXBhcmVkZXMtaW4tdHJhZGUtZGVhZGxpbmUtbW92ZS1mb3Itb2ZmZW5zaXZlLXBvd2VyLXBlci1yZXBvcnQvYW1wLw?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
