# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Ben Affleck On Wife Jennifer Lopez Amid Divorce Rumours: "She Is So Famous..."**

You can read more about it [here](https://news.google.com/rss/articles/CBMic2h0dHBzOi8vd3d3Lm5kdHYuY29tL2VudGVydGFpbm1lbnQvYmVuLWFmZmxlY2stb24td2lmZS1qZW5uaWZlci1sb3Blei1hbWlkLWRpdm9yY2UtcnVtb3Vycy1zaGUtaXMtc28tZmFtb3VzLTU5MzgwMzjSAXlodHRwczovL3d3dy5uZHR2LmNvbS9lbnRlcnRhaW5tZW50L2Jlbi1hZmZsZWNrLW9uLXdpZmUtamVubmlmZXItbG9wZXotYW1pZC1kaXZvcmNlLXJ1bW91cnMtc2hlLWlzLXNvLWZhbW91cy01OTM4MDM4L2FtcC8x?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
