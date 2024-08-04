# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Stray Kids Took on Lollapalooza and Emerged Triumphant**

You can read more about it [here](https://news.google.com/rss/articles/CBMifEFVX3lxTE9fN2lsdkFMUlRuYnpBSGo0LWRRZmVHZk1tMGk4QVVyWU82dWNFcllPYnZ4eVV1X3RqR3dBem9xa2dfb2V3OUxneFlEVG92OWhXOTdUTmY0UjIyekdLeExvaFg4S3lxbGNmeWV1TzFVOWQzc2dsYXBkQ281cjTSAYIBQVVfeXFMUElzUXJQNEt0Q0VGZTQ4VGNsY01iY0dJT094bHBmSUt0WkV6TVN6dVNmM09FdzBmcVBQNEJBUkVwRk12ZnozM3N4dkpTNGdpcm1mYks2TGhGNElEZHNIZDk3NFlORy1YRFd4cC1UWlFuY04tMTUySHFPX094Y2lseDZhUQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
