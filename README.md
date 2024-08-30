# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**‘We are afraid’: East Africa struggles as mpox spreads amid vaccine delays**

You can read more about it [here](https://news.google.com/rss/articles/CBMitwFBVV95cUxQZUx4b01RLUstUk5ad1pINFFpWGVtd3hNeFFoSTVYRkpYUFk4ekRSSkMwZGw0V3VxbnZ5Q0dha190TldwS1hoWWNLVVlPVkQtTlJ2b29BcnBFYk5fS2lObm1BN2EwTG9aR0F5TW5EelltbG14WGhpekZSY3B4LVo2dXhqbHZPc0dVTnJIZW1maHZUcXV0RV9FVUZMUVB5MGdHT2pIenAtcEdUN1dWb25lUGhOUmdxS0XSAbwBQVVfeXFMUFV6UnBrMWg2ZTF6YWQzdnFiMHk1MjJieGc3bFFfdFdhYzBqMTRQZzZSWlFsV2U0WU1tbUtLa1d1OUY4VUUyN0IzZmF4SFpvbUlkd1dxMlRWZGN6ZDJybElUcXN5QWlJZWpwTmNZbzdmZ0pfdUVhaU5MaEtfemY4WVFkckEtYWdXZXd1cXFwVjlsY1lqOWNTU216ZWdITnN4aXF2TzlYbmJIaGsxZllvMzMzRTFQcFprUU1zT2g?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
