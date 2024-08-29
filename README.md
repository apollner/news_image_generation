# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Oasis reunion latest: Liam and Noel Gallagher confirm 2025 tour with Manchester, London, and Dublin dates**

You can read more about it [here](https://news.google.com/rss/articles/CBMiwwFBVV95cUxPcDFESkJFd0hVTVJFelpFTmFkVXA4Nm1OVkVCNnVUdDhPZW9zLU9ZQ0ZSRGdxV19NUHhTVnd0MUpJZ0tyX2ZRUExWaFB5S0JPMUhISDF4dXhkdDdORGFiZFdCY3paMDZrWXVHNkZCakZveEsyTUItSTk0cUI2ak1EcjVjY1ZHWVdicmQyc1ZpcDVfYkwwOVJDY2ptM09WNm03NUNXWE9ka3ZyY2ttb3NiYnMxSGlkaldhRkg5bVZ4SzdnOFE?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
