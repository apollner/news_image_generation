# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Presidential race in Michigan stays tight, new poll shows**

You can read more about it [here](https://news.google.com/rss/articles/CBMingFBVV95cUxPVTBVVmJyMXdiaTZ6ZzVfaExkRFBGMm52ekZwNUNqSk5VMjFPOGlacFF0UGJDMGk3a2dVT2wwUkUyMW0tMzhJU0NKMV80NmFCRzNidlk4b0ZIYXZ2TnpRWERTZGdIVlJuYktEdmE4ZGtHbl92dWw5X2FaYVBfOGFvZXQwSkxOQW9qQS14T1R4cHJGN2w3dUQ0dF9BaWxSQdIBowFBVV95cUxQNlBzdHotRWFuamhBRmRkeGdIbXBwRjVZNjRJQlBpQmhTYk5temhsdGt5TlM2dlp0cDhuMGhWYjhmTlVjcWVKdEs4THpxTXZrV0ZGa1dhZER1d0JILW1TSy1DWS1mOXEwTHRyUFY4YUZSRzl0WFdYTThwdkZFa1VjcjJWanpEbWNvMm5fWXpzdFlmVWJLRTlla0JlZm9PZEVXSkVV?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
