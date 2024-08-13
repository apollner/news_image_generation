# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Adani Group shares shed billions after Hindenburg allegations against regulator**

You can read more about it [here](https://news.google.com/rss/articles/CBMiqwFBVV95cUxQREEwbG55RlVQRk8tUlF6MTNvbzZUeGp3aXdHVXRSMWs5R08tbTJSblJlU1pkLW9sS1BNLWQ5bkpCam9zdGlWaThIQkVTZGZCN2dhSGxzcVlYZFpIQlNENE1RUVlRSk1HWFZLRmFRZ1hWMk10SFM4UUhHaS16QzRwRThsS0F5elMyUFdrN21ISDVFYXBDNjEta2RWYjNpd1FPcnhPQ3NaVWRkZzTSAbABQVVfeXFMTlFiWDBObXJUUHNEN3ZUVWZnNUhTUUdoM05FUVZUWTRSVWIxb0Z1aC1kMVFYUmh3d1dXc1lxYW9PSzRqSDZST1hiUTRlZmpJeWFuVWNYNEZzQ3dmTVBmVGZJaGZGb29TaXBaTEVJdDJRbjZlOVRTZnFiY1A2VzhROV96anB2TXloSnJnMGRSU3BTNU1BSEJLSFJNY212Y3hOaHA3bjJaRDJyMnVGMHhPM2I?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
