# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**What do marijuana, the death penalty and fracking have in common? Harris shifted positions on them**

You can read more about it [here](https://news.google.com/rss/articles/CBMitgFBVV95cUxPZW1kWklYaDdDRTk3WF9aZklHcV83YkVvbVEwTHp5Ny0xbXdLeWdiM2dkd3c4ckFEVzkzX3laUXFVMmt1WXp2UmxYMHNnU1M5TFFfeGcyMnkxcnRXX1FVeW9wZEpfNGVoaFdxSlBlMGd5OUlEUUEtRm91R2FnOHV6VmhRTHhXNnd4aG9hdTBhVkZpQjV5Nk1zWnZDZGdSOHRjUlUyeG9pUl90UF9NbjBBaERyUGV4QQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
