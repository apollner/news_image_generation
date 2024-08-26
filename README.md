# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Sinking of a super yacht adds to questions billionaire Mike Lynch wanted to put behind him**

You can read more about it [here](https://news.google.com/rss/articles/CBMilgFBVV95cUxOamVLc2pxVENkRjVzOGRtV0dQcXlCa2NvMjBFa0RpTUVuR1ZOZGVxa01pYzdaNU1zbWZyNHpYeVZGRGhfelVKSXc0NUlzWXVqekh3NG1LX1BrcmM0V0U3Yl9iNFRJaG9RUVlXWWZOcVdKYURCSTFaa1JCYzlWc2hIbE43aE0tMmhGUmowS21pN3Jzcl9Ocnc?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
