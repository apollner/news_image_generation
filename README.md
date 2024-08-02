# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Americans Gershkovich and Whelan included in big Russia-West prisoner swap**

You can read more about it [here](https://news.google.com/rss/articles/CBMivwFBVV95cUxNZzV0bGZDUFlNOTB5VmJnSmNyWWVaTks4ak9fSEZGVEx2MWZXc09OOGNKbW51cGdqVmsxR2JzcGFXSlhubksxRVFNdTV1bTRRcU5RYXFrSktpdUh0UFg0aFZEeXptUW1MSWxPSTJBMEt3RVBuMXlETlhNUzBzbDlRZERSUEdZV19ySE9ZY2N6LWRRakI3R0VjWW9Hc0tFYmwxVFV1T29iRWYwYTZiN1NYRHYwQmlPRk5PY1kzUkN4VQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
