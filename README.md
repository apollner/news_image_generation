# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Thousands of activists expected in Chicago for Democratic convention to call for Gaza ceasefire**

You can read more about it [here](https://news.google.com/rss/articles/CBMiqwFBVV95cUxPX3VSQllBYngtSWVXa3dLSEJ1SWgtZkVUNkZleXR2d0ltMF9TVjlic19yNVBZQWpfSDgzNkJMd0dBNEN0a3ItZEJiTW9uX3J5SEZObmNnNmRpSmpIbVNTQ1JuX3BKT1JLTC02eDRIaWRmdVdtUlBIUDc1R0kxb0ZKVnJqeTNDN2tRLWVqU08yS1p4T2tzNGh6ajlwOU84aFFEbHFBNnZFeGJ5UVk?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
