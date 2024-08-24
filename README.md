# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Volgograd: Four officials dead in Russian jail hostage-taking**

You can read more about it [here](https://news.google.com/rss/articles/CBMiWkFVX3lxTE9oRzg0VkwwYTNpSUl4Mmk2N2M4eGN5V3FKZkxXbHEyTnF4aVY3cGc5NlZIUGI2M3FkT3hXWlU0SmtnZ3Vld0lDajJnbzNXZFFSOHlxVHRScmJpd9IBX0FVX3lxTE1VX1Q5M0szU2IzSjltWEZwamFXODVXTDUzVF9OWTc0Y2NRaFlXVUFxTm9fZTI4MXBqakk2T3BQNE5IcC11S3BaUW9RYTE4X0JWaXF1cmJSN2J5TkxqTXVR?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
