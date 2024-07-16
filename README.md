# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**The RNC starts today. Here’s what you need to know**

You can read more about it [here](https://news.google.com/rss/articles/CBMiU2h0dHBzOi8vd3d3Lm5wci5vcmcvMjAyNC8wNy8xNS9nLXMxLTEwMzA5L3JuYy1yZXB1YmxpY2FuLWNvbnZlbnRpb24tbWlsd2F1a2VlLXRydW1w0gEA?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
