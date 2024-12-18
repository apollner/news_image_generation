# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Wisconsin school shooting latest: Attack happened inside classroom, police say**

You can read more about it [here](https://news.google.com/rss/articles/CBMirwFBVV95cUxNeTdCb3UycEZEREtUT3dtY2JGdWFMU2VlYzJvam5ETER5Q2kyVG5LTjZ4YWlEdmVpN1hpVXU3aFZoZmt6N2lLZ3Z5ekdiWGRYSWhBN0g3bWVyMEZqWlQwRlk5MVk2Nmd3VlVzWGZydGRpS2lTNmtCNHJid1dZZDdNUmZxRE5uZnRkTk5KemZkMkpzd2hWOXp6ajRKTzF3andvTjJkSDF4YjdkOGI4SDJj0gG0AUFVX3lxTE9XLWlpYm93LW5hMnRlNldRTWkyRGI0QVNHbm9kMXhEZG1vVmw4LUxfcEY5aVNZWlloM1lKa2c3ZGJCbHNWaWxMOWlTczNEeGQ1LXFzTURDM3Z1bTVsOThtUzh4NUd6QmJ2UlUwWkhiODRjWUdQZXNrMUs2bjUwMV9tVFgwTjVNVUdwMlppZm1LaFZkdFdLRkx3bHpUbkRmb3BGMGRTcG5RQ2U5N3FxM3JoUWlIbQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
