# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Black Myth: Wukong continues its dominance with new milestone**

You can read more about it [here](https://news.google.com/rss/articles/CBMijwFBVV95cUxQQllTclVJT1BLS2dZaHVJOFZsYkl0RmoxX0dLWm1qUWJDZGlDMVdqSkdOUFI4MU9oZ0tEME5taUQ5X3VITDdPSzZVQWJVZmRvXzRWU3lycHVsRHZHZWpGcm1OQ3FNaURjRVU1WjlKWE9NdEI3LWV3VE1wR2dNbklYVlphbzUza05XTVpFbVNUdw?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
