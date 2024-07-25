# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**What we know about the deputy charged with killing Sonya Massey in her home after she called 911 for help**

You can read more about it [here](https://news.google.com/rss/articles/CBMiZ2h0dHBzOi8vd3d3LmNubi5jb20vMjAyNC8wNy8yNC91cy9zZWFuLWdyYXlzb24taWxsaW5vaXMtcG9saWNlLW9mZmljZXItc2hvb3Rpbmctc29ueWEtbWFzc2V5L2luZGV4Lmh0bWzSAWBodHRwczovL2FtcC5jbm4uY29tL2Nubi8yMDI0LzA3LzI0L3VzL3NlYW4tZ3JheXNvbi1pbGxpbm9pcy1wb2xpY2Utb2ZmaWNlci1zaG9vdGluZy1zb255YS1tYXNzZXk?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
