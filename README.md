# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**The Scandoval Never Stops: Ariana Madix Now Sued By Tom Sandoval Over Explicit ‘Vanderpump Rules’ Video**

You can read more about it [here](https://news.google.com/rss/articles/CBMiX2h0dHBzOi8vZGVhZGxpbmUuY29tLzIwMjQvMDcvc2NhbmRvdmFsLWxhd3N1aXQtYXJpYW5hLW1hZGl4LXRvbS1zYW5kb3ZhbC12YW5kZXJwdW1wLTEyMzYwMTMxOTAv0gFjaHR0cHM6Ly9kZWFkbGluZS5jb20vMjAyNC8wNy9zY2FuZG92YWwtbGF3c3VpdC1hcmlhbmEtbWFkaXgtdG9tLXNhbmRvdmFsLXZhbmRlcnB1bXAtMTIzNjAxMzE5MC9hbXAv?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
