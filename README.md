# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Ukraine attacks Moscow in one of largest-ever drone attacks on Russian capital as war intensifies**

You can read more about it [here](https://news.google.com/rss/articles/CBMivAFBVV95cUxObDlPTTJRQ2NRWmZZZVpSbkZKS1lDMGJMTVV2MkJEZHl3NE1ydFRmeXI3U050a1MwQWdSbzh3TWlMN1hUOUhzVnVXbUtnVVh0RllPVEtHaDBfSDd3eVZkVkRyb1BsRk5VXy1ZMkNBYmxMQlFaOGVKVjhianNaWVFKbzN4U1gxWC02WWd0akNjak1nN1lIZW9tWkEzQzNHYllDLXZVOExobzdHemVtenNZWG5uZTcxUFd2LW9rSA?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
