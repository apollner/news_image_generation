# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Tropical Storm Debby live updates: 2 killed after storm makes landfall in Florida as hurricane**

You can read more about it [here](https://news.google.com/rss/articles/CBMiiAFBVV95cUxPZ2VoZUQzWURIZHBwT2wyeGNCeWZlMmZ0R3JGRHpXeWZjMHM2YzRrMDhianpONWJEN25aaWd1QjRFaldFRlVJSU5OenRlS0hkWjAzTktJWk5pRWllTVVxMlBsVnNaZE1OblA3WkItV003dXNSZVZlcEV1dkVDVjFVNkN1dTVFZmZx0gGOAUFVX3lxTE5TZHpCMnhvMjRLRWR2bnU3dGxNSUVzdFFHX1pGMWI0OWhUX2ppWUdnbXhOeXZnSmpfY0t0eTlsb2lMWXBENUlPRzBfZFVFc2JWVFdzT1B6LUs3bHBpelBrUVpia2hSNHhOdzNkOTczaklMWHoyT1lWOUZiY2lRUHF4WndHelQzOEcwTlYwcGc?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
