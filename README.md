# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Two dead and several trapped after hotel collapses in Germany**

You can read more about it [here](https://news.google.com/rss/articles/CBMigwFBVV95cUxQUVF5R1oyZE51NlptVUF6dTFmakd6RVJUcDY3akVxLUo1X3ZUUEM0cDJwb2M1UExHMnZuZ2htVUhZRnpyZEdSalpvbHB3VDgyNjFOU0ZPVFdmSE1GZk11Vk5QSlNQVVJKdmxON1RMYnIzZDdUT2JKOXM1OWdBdHljZF9GY9IBekFVX3lxTE5xMFFMX0dpLUVWZDRCbUpJWUNyVDlPVHVjZHA3YkR2di1OT09vVm1admJNVW5zTlZEZnI4c1J6cFdSMGR5eDRXQnhUTHdJZTBfTWFyMnJuY2lKUURjUlFJc1NaRlBRTkhSZ09LTjRIeFJfWjdGTER5aVV3?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
