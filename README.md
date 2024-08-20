# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Gay man says he was assaulted by Shake Shack employees after kissing his boyfriend at D.C. location**

You can read more about it [here](https://news.google.com/rss/articles/CBMivgFBVV95cUxNTGc1dkJXQ0pXbWYyWHAwdEIyTnprOHFYNmRiT0h2QmVwZVE3VDZIdzJzQ0FwUEF4T1JSSUxOV2xZZkVuMHpQdFoxcHVXdkM3Z05CU2diekpBWHVnX3psYU96MXdXWTZUeml0WlpmZThPbGV1Q0hYRlFXSkZpVnpoYlBDTHc3eWpfRERONjBFVkVfRlF3NzRhcG5UZ0sxV01PVzd5cnl2T0dWWV9VZkpSUExYdW1fWnBqci1aeXN30gFWQVVfeXFMTVYyOGxVYzZvZE12bzlfYTJaQVl2S1NMM1lkLXdYd0xENmQ5YkxkU2ZuMnAtb2dsaXFoRWRPQUJHV2ZqeW41UEdWY0Q1T0hfSE1LZmNXeHc?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
