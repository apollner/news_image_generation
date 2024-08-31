# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Fact-checker examines Harris' position on fracking**

You can read more about it [here](https://news.google.com/rss/articles/CBMiwAFBVV95cUxOYVBQU1ZyVW1xUEtaNjVJSTViR2YxMTczTHVmbXczLTlPUS1OOVNDdEZ0d3Eyc0FjMy1INjk3NklueU02aHRUaGQ1ZkRFZHZIVHA5NmhkbGVqUzFpR2V5WTNhX0t0RFNQbnNYQXRfREViR0d0VkZWVXd2T0FUeEV4QWVQYXNQT3E5OEVnYjBpcDV0TlQ4a0dKNXFybFdFSG9ibEc5QUpvRmRUZUdsZUJGVkI4bW5vS1kyd0xrdWJMcmI?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
