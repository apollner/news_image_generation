# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**TikTok asks Supreme Court to block law that could ban popular app**

You can read more about it [here](https://news.google.com/rss/articles/CBMirgFBVV95cUxOcjJkbkpNTGVFZjJSaFpkNTB5dFRYOTYtX01EQXFqcUJhZEkxLWM4aE9haXFZaTczd2ktSGtKMWI3TnJZYkhPVnlGZmpHMzR6LU9FaVctWVRMU3NSb3Jqb291ZGpVS1JWQ1NrTFIwRWQzUmxfa2ZWMmVtX0pyNVAzeHcxN0FTSjZCTUI4a1VIMlpuQVpPZG9wZ2c5MEJrMmlkTWEwMi1obmZ1b1N0VkHSAVZBVV95cUxQOFllQWpBOEp3TW91RnpRRG9RdmhaRmhIXzI1cVV4SE9PNkh0QWt4YTZ0SnZjWHNEdHZWY2hobGZxdGJYUl9MTTRlUmprVTVMYWpyUTJCQQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
