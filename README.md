# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**What does Bitcoin smell like? AI startup wants to ‘teleport’ digital scents**

You can read more about it [here](https://news.google.com/rss/articles/CBMimgFBVV95cUxQQkdxVG9jZ3d1Q282WFlTaXIzQUVEZ1RabThPUkJQWG1oWDNwcVROUWY5UUdDVFFoT3NGX2FlcGhtcTN3dlM2SHVUY1VjaUFmZUhYSG1RYXp0Z0FNX0ZyUFE4eG9mVkg2WnNaZUp6eTNqQTdxSGttV1RKTnZReXQzVTJlaGdPdWc1LWxVUDdsY1UwMDNLVnNtaE93?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
