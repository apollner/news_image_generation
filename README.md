# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Angelina Jolie’s son Pax ‘stable’ following bike accident**

You can read more about it [here](https://news.google.com/rss/articles/CBMilwFBVV95cUxQblUwVWU4UDE4SDRBcHcxZkhVQ2pLZDBndlUzUXpZZE04T0s0djZrQV9WYk9CTThXYjc5SGp0OHFtajMxYWRhbTczNHpTVXJDdnNPU3NKbnpvRldCa1BaZTg0clU1cDU5M3l6N0FGZkt6SkxPVTZwY0xBMEdqbXlLbkNydmM4VTBZWjE2aWxwQ05EbkV2Z3lj0gGOAUFVX3lxTE9HWnhIOXNrbzYzTS1Gd0pHcjk1WkUwMWJWd2JwSVU4YkpmMXNIblJaMFRlaWN6UDVVTVJ3NUVoZ09PSEY4QXhEVUxTR2luVGhCcHZiSlVRaG1ldkhFX0lieXNLOXZXc3M5RHZoX3N0WFpMYXRsUlpxVUo4S1k3NG5YU3lVQXlWOXlmaVR0eGc?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
