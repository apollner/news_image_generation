# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Amazon joins Google in investing in small modular nuclear power**

You can read more about it [here](https://news.google.com/rss/articles/CBMipwFBVV95cUxQNmVQSnFqcEU5WGgxNVh6eEYyeEV6ZXRBOHZCRmJWQmQ2TmM5c1JIS3NTbjN6blVvV19ieDE1aFVnVmdiTnNTazZCeWFmdFJiWl91dGd4Q1JrVUtlb0JQSDZEOVZfUmkzVDBYenhIZjRKN3B5TlU5amx2Szl0M1VfbHdYaVo4aUViWC1XWVNFSkFZQV85LVBlNVA1QjdFeExQdlhVVkh0TQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
