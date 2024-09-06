# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**These are the top 10 highest-paying college majors — two have six-figure starting salaries**

You can read more about it [here](https://news.google.com/rss/articles/CBMiogFBVV95cUxPRHpQSGgwZHlGVmlTZHEwazVrd3VPejFqcVZKSE9KS3E4N255SEdMSUxoLWFjNzh2dUtGU1VGU2p4aXRtYlNrX3JrUEh3aWtBSVAweHFaY01VVUp1ODVoLTZTVU9VNUxSZThDanhjWFZwcjBFdFJUaGhpREJvcWtLUm1CZGstM09VWDZ6TWtneGtXRjhEZTAzbVEzVkZheHFwaGfSAacBQVVfeXFMT1hFZEQxU042akRvZjhqdVJUNF9NWWNVM1VHSi12TzN1ckY3dy1pOUlvckxBZmVJbkhsVmFNMXFzTkVSUDhiMmFma0c5WXQxWmpuNmhyVnFlbGpaWFBaSGluaUxaYmVkVUkyLWJTZUpyS2RVYzgzLTk0V2l4U2k2UVdpT1ZuYXVLaVlxeHdaQ3BIT0xGQkVUd1ZmemlJSmFEa3JNQ3g0eXM?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
