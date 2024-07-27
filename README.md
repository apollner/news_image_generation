# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**New Corvette ZR1 revealed: Inside the car's 'mind-blowing' specs**

You can read more about it [here](https://news.google.com/rss/articles/CBMiowFBVV95cUxQSlRzQ1c0djR5YnIzdmlROFNLUGhpb1A4YWxhd1ZUTG0xeWRxd3Blb3R1ai1NdzBYUnczdUNYSzNHLV80RmNFM3oxLXRmZUphdUh2b2xrY21Ra3J6bEx6VENOSlNfR2Z0ZDFzZHhlMGVnOXhiTVpvWHFQRDFwVUtfOFBUWTJZX0Q1aUtjbDIySU95N004eWpIWlBWZklPcnRZVXEw0gGoAUFVX3lxTFBFUVJOMEJiamF5al81TU5aRndNek5Gb2dRRExBVVBaek5LMl8yZm53RFlJZ05GS0ZSRGZ0Q3JueWc5dGdUOGZuY1hwaWZSR0w4aF8xbGZZdHhhVVB1aFVkM3I3UXVIM3lNSExSOWxNTjBvOXRHVGFVR0xoZFExd21qX2ZCa0lyMVMwUmhhNGVtcFdqd1dvU0JLQ2RmV1ZLTFlvWENWZGwzSg?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
