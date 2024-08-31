# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Leah Remini and Husband Angelo Pagán Break Up After 21 Years of Marriage - E! Online**

You can read more about it [here](https://news.google.com/rss/articles/CBMirgFBVV95cUxQdTRiOEpkYkNUbGNIaFFmS0NRQ1kxS0xoelZEQzNSazREbXZDQ0s0SWMzXzllZy1nX3BGeWxvTjBSREZIRjlXa2hvN0tmZGw3OTI1bmJ0THUyT2o5ZFRKam11WkV0VnBBdzdqZ0xES3lxeWNLd1lra0xFOUhhUkxyb1hkUzU2U09Mc3Ryc0YzNENHV3Y0NXFfUm5oNWxidWNNZERtWEo1ay05N2R0UkE?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
