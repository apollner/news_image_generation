# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**The suspected UnitedHealthcare CEO killer planned his attack well – but made crucial mistakes, experts say**

You can read more about it [here](https://news.google.com/rss/articles/CBMikgFBVV95cUxQWjVla2M2YVdTelktNm5xR2IzdDhVbUhxcUR4WjRPdjhOQmtBQUtIU1dxVy1VQ01CWEZENjFERXhVX3dQM2dDZUZFQXBOaGtqQVhtbW5TTU9ZQW9kR3RjanZjVWFpYWd4d1hTQmI4c0x5TTRWM3pEalZCWWQteDNEdXRWU29jS0s3bVhyaWlLTDdRZ9IBiAFBVV95cUxQT21wdEhfdndHVUh3aDRPZndhYzRXOVpieFVBbHNXM2xDUnN5Ym03MnNHS2Z6NjZuSWFtRGNXZzBxcEh2ZkhTYW5GZ0dSNWN3WGoybk5XRWMtdjNJcVM5WUpVTm5aZ3k1MHh4ZTlHaTlwZUJDSDFCV3RrMFJlZldkTGp3T0JGYjU2?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
