# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Hurricane Ernesto makes landfall in Bermuda, weakens to Category 1**

You can read more about it [here](https://news.google.com/rss/articles/CBMipwFBVV95cUxOM2psUDY5ZllLd1ZJMkxWNDdwbmVOWVlSb0prYVU5azBNcDZMNjctTWswWG5YWW44VXBYeGlvTnRLeVBaMmdyUjBqVHpRaGswQ2FZNnpvTXNCdFduN3lwWXp3eVVOVlVHSFJ3QXhiN1ZTamRCNFRWV3VEWHhlN2VKQ01wUVhJcFJXNE96TEtpU3NtQzhyWkxtZExibEV3WHdyVVQtTmwwY9IBrAFBVV95cUxQYUtfdkRJcUlsVHdvRXBLcmVkVHRSZENNQl9SOFlZVXJibXc5bHBGdWJSeUVrdDVkeXhIRE9aN25ZQXhCV3o3cHZwNFAwUGtlWEdHUmpDYzdwekxtcDFtMHgyWDdXbHlDcDk4QkJ5Mm5uT1NVWDE4RE5JdXoxRjE5NGNDZjRVRV85X2dZekF5cGZMb0hhYmJnQWRvR281Q3BUQU1rcDZPalNwRG1I?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
