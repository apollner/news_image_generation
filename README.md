# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**4 dead, dozens injured in tornado that devastated Iowa town**

You can read more about it [here](https://news.google.com/rss/articles/CBMibmh0dHBzOi8vd3d3Lm5iY25ld3MuY29tL25ld3MvdXMtbmV3cy9kZWFkbHktdG9ybmFkby1kZXZhc3RhdGVzLWlvd2EtdG93bi1zZXZlcmUtd2VhdGhlci1tb3Zlcy1zb3V0aC1yY25hMTUzNDMw0gEraHR0cHM6Ly93d3cubmJjbmV3cy5jb20vbmV3cy9hbXAvcmNuYTE1MzQzMA?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
