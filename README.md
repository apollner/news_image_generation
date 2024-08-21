# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**George Santos reaches plea deal, pleads guilty to wire fraud and identity theft**

You can read more about it [here](https://news.google.com/rss/articles/CBMid0FVX3lxTFBhdVdfYXJFWk91TXVjdENrUkdvOHZNWGVUNVU2aG4xY1JYa3VTN2dsZFdpdFFVSldPQ1k5cVpMUk5lQzRMWEh5ckNkSncyWnNLQnByaEwzNkVKbjJ6MUFOYWZyZURjS0U5dWVrVTNJakZiS0YyUGFJ0gF8QVVfeXFMTnRJbU9xamI0SkhYQmVmRlRYLUZYbG9JZzVsTHRQaUg0Rm5Fc0RwbFdxdWZUay1pZVY3MlBDR2EtRUhpNm83Z0F4b1Z6Q1Vta1hhcVJONS1qRHl3YjRaSnRyNHZNQ0dxcXo3ZXZZT3k0YWVQYVlaMmJIOW9weQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
