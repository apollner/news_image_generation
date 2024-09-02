# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Israel-Gaza war: UN agencies start rollout of Gaza polio vaccines**

You can read more about it [here](https://news.google.com/rss/articles/CBMiWkFVX3lxTE5EOXdNU3dIVUVIS0U0S3JrQXB4WEhxR2xzbFB3LVRGTS03Nmt1VFlMMWVkaXcyUzNweGF0VXJHRzdIMHprNE1Ja21CT0t2VmxTZW5wWFJJSXZIUdIBX0FVX3lxTE1PclV4M2Nxb3dXWFZ5Vngxc2xGaWpFSTc5WjFzMWVtckFiNVctajNXNFh3ZmItUWoySzRXSHNMRVlydUdZS25vZXRzeC1JTmYwRzM3VU5vajZNRXJIR1Yw?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
