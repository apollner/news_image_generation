# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Secure Boot is completely broken on 200+ models from 5 big device makers**

You can read more about it [here](https://news.google.com/rss/articles/CBMiugFBVV95cUxNRlJzQzhSeTJJemtFSVpERW4tMmtzanNNUEFKMUVpVnJ6QWVpMWx4UUJNc1dkU1MzeUk1MXhETnlaZFNMN29lY016Q1d5X0ZpQ09oZ0JiN3V0RDZNdU15VHBWS0tob0RLQm05ZERHTWJUN0pxcEZzN3lMRkNhRTNLajA3eUxSeW1ua2Q1TzdEWVZCSzBya3VnWUlfV18weHNpVWJqOGtLenF0ZGYzel9OaFh1YVNXUUp5T1E?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
