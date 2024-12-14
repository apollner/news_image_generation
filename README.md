# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**A look at the political storm caused by South Korean president’s martial law decree**

You can read more about it [here](https://news.google.com/rss/articles/CBMiuAFBVV95cUxOWHg5WXRabnhBNHpGM2pZVWRJWTJpM3l1ay0tZTNfU0dab0FnZi1EbjJQX3NDSnhWeVk1UWJhLVJuX21Tb21Cd3FqeUtGVjVhRDFOUnVjNFNkZDNsbVE1Q1VXTHFYQXc1N1Z6c040bGIzUjVpZEtGN3hYOVR6OGM2bDdfQ1FKSTAtWmdzYWtIWHFDSlNVa2xrblpaU1c0YURONDNIUjNLTEp3NEQ0cXEweGhDeXNiZ0dt?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
