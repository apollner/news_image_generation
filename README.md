# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Potential Tropical Cyclone 5 forms in Atlantic, system may be a tropical storm by Monday**

You can read more about it [here](https://news.google.com/rss/articles/CBMivwFBVV95cUxPVllha2JsVDhHRmdpZ0tjSmpHeWpaN1R6dXlLa1VQZHhBNDBIWHhNckxKeDM5aGk1VTAyQVVvTkVlNnNJNWNWRjlmQzYzWVhzb3duTXd4MW1tcVB5eUVvMW9zRUFaWTloOW9Eem8wbUJkXzhmbWlHX250Q0c0TkVFVkdXYnBNX2s2QWJSYW9GMmJ4eVVRampINThMa2ZxYWRuajd0NVpXNUJKMFNMWU9tUXVkbDZsbDFiREZmODhLcw?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
