# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Trump says civilian award is ‘much better’ than Medal of Honor**

You can read more about it [here](https://news.google.com/rss/articles/CBMie0FVX3lxTE5JRS1KUER2Q3VCV0k1NF9VYXdiZmVTV1VPN3pVNDladUVBbmlyUURmVlo1RTJoN0NMY2dqeTAwYURNRUR2SGxLbU9ydm5GVlBHbFJZZXR3ZF9vR21oWWY4dzVFMmJwdEV1QUExMm9hbzVoZjRweWVPTHhHWdIBckFVX3lxTFA2ZWFsdXJBS2xCbWFkenBDYVhYVzR6LWNMYzZFQmJmZ3F0b0J5Tmo0WHp2YWVlUjFYTWdCekowZWZrQUdWQWVWem5Dek9YMWZBVEFMRXhJY0FLRkpweHZnUXVEeVJfaDNTQ0gxZ1Z1SmkzQQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
