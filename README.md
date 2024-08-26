# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**The 10 Senate seats most likely to flip in 2024**

You can read more about it [here](https://news.google.com/rss/articles/CBMiiwFBVV95cUxObkRaa0VlVzdOWEpzdVFLamF2M09BVVZUanhDTXNfbG4wdGw4cXZCeUNLNkphVTJVUDlrdVBfWm9PX0I3RjVrQ1VDTzBEUlpTTFRlRVBqOVpXNW81Q0RGRjFiMzBMNlJRQmUxMFF0Q2xMZ2Y4N1pOQUV1NlBSYlp2cUdvUlhBRFVJRVlV0gGCAUFVX3lxTE04Y3ZYbndveTRsQTY2cV9KZElmV1pnRF9zN0szMXpEOHR4eXNpdWhWUDBnbWZaV2hUUVdJbThUamd2UF9mbVJJdEtwMDhLcVFZZ01BMzhLLUFzcGVDbms3c0VoLVI2SzN1a045anhWRlpBQVVXb3NBMFdybkJ3QkFMRFE?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
