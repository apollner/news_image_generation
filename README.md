# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Russian and Chinese bombers intercepted off of Alaska**

You can read more about it [here](https://news.google.com/rss/articles/CBMilgFBVV95cUxNWWxnZWhUNGxWbU16dEFFODliS25TMzRPY2pRZW9qWFBPUXEwaFZQaEJYQTlNOVJVX2ItQ0Nha29yYUp2RE5TMXFyRzloSl8yNGFQY25XOUw4NDhtVnlmZnQ4SjZwa0RzSFNxX2x6Q0ppano2bXlhZl9UM2hHS3lyX2dWYktvWjZWSGhSU0phMzV4N2I5c3fSAZsBQVVfeXFMT1ZvdGRQZGxsRjhNZ0tnZ2c4dnlsTEw0Um9jNHJpb0tzUjhLdFdhZmxqU1Q3T21lVnhWbmJLd0FfUkN4bHpiZGt1aWNSNndUeHpYZXo4ZlRibHdaUXJWNVg4SVh5VHJJM3p4QlRNeFUzZzF1WmpPMmwwWEFzS3BJVUxPdmpTZFlCcDREVi1ud2tmeXpwQ292MndQZjA?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
