# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Apple iPhone 16, iPhone 16 Pro Release Date Proposed In New Report**

You can read more about it [here](https://news.google.com/rss/articles/CBMiugFBVV95cUxQcFhtVFhJd1VVR1gzdVR4aHg1S2dIWVRySDhkQWpUR1EwenRkc0tZZExISmM3WGJYMkJzLWRRLW9IMTdaRHJVcFd2OXFBYi0yVTF4WVVyNjJ3ZVdGRGVSUW5XQ0JPal9lUmJ3SnczZ1NqbWNtZENwZy1ZRDNNM1lCN3lYS2toVEtHbjBFQU1YbVhTaHU2eDFRYnJtamlUdjdLY0l2eTJ3X2pvRVRZSW9zX0c1VGp2LWV5amc?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
