# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**US gymnast Jordan Chiles to lose Olympic bronze after court ruling**

You can read more about it [here](https://news.google.com/rss/articles/CBMivgFBVV95cUxOY1JlaWxrQVFEc2ZLcEhGOGtRc1czUm5tS1JvVFlKSWlUdnh5QU1FRzNXR29LUU1Kejc1UlhDbzcxUWZpTDE4UklzdW5XWFM2Ymp3STFmQzhrdWluMjNkbW5HZHptcUUwbWUtdVZiQThsUjBXU0RQREd2QVBqbkF1SlhSR2Q5c25JNHp6X2NTOGc0bjVHS2JrUWFZSjgyd1A3ZDB1WVpwWXdGbUw5R010OGI1QWt3aEFCTzVUMGJn0gG-AUFVX3lxTE55YmxhZEl4bGhQdk5neDk1TVVELW9DUjRkd0hXT1pFSlMzcGg4UXdfbXhDMlExd3h5dWlrMU9MM1p1QTBncDNfaUdjcU1jNXQ4U0dvc2dkbDBjSkFVRUc2UzZ1ZFpjQzV2allOZW14TGtUMFpaaTZJWFlmcWtHS0I4bm1VZDVya2lSakRqZERXbHcwQ211b0pRdVVtZGhSeERKVE1takY0Q3ZoQUhYOVJYT3VpWUhTVC1LYW02NGc?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
