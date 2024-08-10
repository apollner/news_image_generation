# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Artificial sweetener erythritol could elevate heart disease risk, preliminary research suggests**

You can read more about it [here](https://news.google.com/rss/articles/CBMiwwFBVV95cUxOTUNMdFQ0WEc3QXVkdFJUTURZM0tPQWJGUTNJMDlvN1pxMXpWVWJ5MGRiLWRxZXBUSThrQ2thZFplWmlCa0dsOHpHeDJEeXo3M29UQ2tVd2w4eXhkYVhaMm1KdGNTQXdYelRDVFpveUpKUW9zY21Kcm9KV0pXOUtBZmstNVBKd251RGxZUlpqNUNKSUZoSF9RcXFtOEJINnBIcDNVZ2xzLVp6MzZDMkREb3o2UFhDcGVGX1lSak5hekZXYlnSAcgBQVVfeXFMUFBtZHVwRlowdlhDMTVoT2VuSFVYUFRKRlM0T0dUUTJaeHdHVDR6WG9UV1ZiWE9fTDZWYk1CQnV4VHRyMl96eXRncVNjakVoVTM3eUZZcHU4Z0RZeW1Bajh5d0hLYmdhVkhET1VxenJMdm92b1ZSNXNSSERhQi1TcFdqanBxcE5EcG12SUdrU3ZzY3NyMEwtQ1RjcjhaMDh6T0VpWVpRQ2hKWkpnVzNmMFgtZjVCcW1oSTlCY3c1d1RvbEZ5OTQ0ZXE?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
