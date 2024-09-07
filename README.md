# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**S&P 500 futures dip as traders gear up for big August jobs report: Live updates**

You can read more about it [here](https://news.google.com/rss/articles/CBMid0FVX3lxTE4xZVBjaG1SWHYzU1kwNkhUZkZTMFF5Snp3cEJmMGNXM21adnNWOXY2Q1hTNnZsaGFzSVRVZVFibTREeG1MdjdlT3d1WGdvV0NxQ25SZkRmUlp5ak8xLVVNQkRVS2VzdWM0RVZHVEVuSnpkc2JfY1RB0gF8QVVfeXFMT2R3U1RzN3Vra3g3NV9FcUZsak5iZkZ0X0lFRGtCcWxGZkxOVUE3M0FHVlEzNm9PUjJadjk0VnFKSWhyd3V6Y0pzQmFyZzh4ZHdCUUIyT2lWR1FpM0d1Tm80SmZsdXdVeWhTMXZZSGRyV2FsSS1nUk5Cai1ubQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
