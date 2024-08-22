# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Target will report earnings before the bell. Here's what to expect**

You can read more about it [here](https://news.google.com/rss/articles/CBMickFVX3lxTE1pYi1sekFIbHdYWG5fUHJleUx2THpNTEZsallJbnYwc0xicEczWUxKMDhwbzBsRkdoeWVidWI3Vk44VzdwYzZ0TUJhMnpJUThLWVBUTkJVa1Z0RWsxa0E5YW5nNEVWNVdOZmR0X2JoWk5jd9IBd0FVX3lxTE1KLVhNbWlMNXA4Y2JfNHlDczd3LTRkbVRtcG0tcEZLRUFWVDIycDktUGw0a3hlSkdkS3JUZXl5dG4xaVNnTUg1Y0Q5V3k1Rm1JekFpVkdkMXREOHpqeElscERNZ3lCU0pfQjVPb3FNeFhBRlo5RGY4?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
