# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Google withdraws its heartcooling "Dear Sydney" AI ad**

You can read more about it [here](https://news.google.com/rss/articles/CBMilAFBVV95cUxNYnFlNXMyUUl0SkRYaVNJZVNoSUN1SXFXZXVSSHhHc2xVQW1fY05Ha0ZLLTg5dUhBUkpTWHRXM245cm9rSFFKcG1uNW9FMDQzOGdfWXZzcDBLWlREZmdKcUtCcEQ1cUVXMDQ0VUdBeFduWmJtVlFZV2U2ODN5V3E3MmxfaUFEdUFLdnhpOHNXN2RFVm1q0gGaAUFVX3lxTE1SWEN6ZmVlSG5zc1pvYjQtcnllVFZ4Z1N3UnI1MzhEUjJGVDQzRzExRHdhMmg4aE1hSHpwRldudTJyWTM5d092Tm1qenFISVgzX2VCakNUeHFwMG5oRUFXOHNlOXlaV3ZQQmE4V2lxRVhKZXNwdlE5bEpkc3pOdWYxdUJ0a3pHQWNiS0k5V1ZKMGV2NzRlZGRhYlE?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
