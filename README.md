# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**A photo captures what Harris’ nomination could mean for young girls**

You can read more about it [here](https://news.google.com/rss/articles/CBMimAFBVV95cUxPS056a0N6a3I1MXVPdE9YQnZoTjBWR3cwTWxPa3hyX0ctZXVWbXF5dS1Ka1hWR2RfbERDZVNzdWlWWUhYenRBb0UxYjdMMnF1enlFS3VMVm9VVEhLSm5hN0w3NGpuSlozTGV5cVVVS250VExaTUNzNmpCN3JXbW5vbEJNVEZlOXkzT1N3MGEzRlJwMVJ4WkZEV9IBjwFBVV95cUxPai1FLWhKQkZqOXFoTmo3RkptT1JQVHRnMWh6aWNSaDdpOU0zU21XbkpTSG9fcHdjR2NaeVFxYU1mUzFsUm1VTktGRHJLSlpxWUZFUW12WU9GOXNRREVQdUlIMjdQaGlSOWh1bnNSRHoxT2FGWjZhYmh3cU05Y0otQUtGT3BlSUJBM0FJT3o0dw?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
