# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Neighbor arrested on murder charges in deaths of missing couple at nudist resort, police say**

You can read more about it [here](https://news.google.com/rss/articles/CBMilAFBVV95cUxPSVZ6VmlRY2FOQWgxRE5nU2hOamJNX3VrNS1xOWZaNDRfSzNYcmVrVUdnN2tnd3ZMZ25vTnI5YXlFcGFYSlBoTjJuRE93SGctSGxoTzFVbHNaZFphdjhPcGd2aXV2dnlqaWNqXzdMWVRKTmZYdk5jNms0RjZsQVNOMFJJMmp6bFdzX2puRVNvNGNfRWdt0gGLAUFVX3lxTE90WV9GRk9wZ3JRMFB0XzhISVdJcXZjMGlBUUNTZ1NPVHBTMW5KSlZQX3drbXVLckE5ck9qM1kyMlJUV1NpRWNya0ZuM2MtbU5RZHRRcjUxdFhQT3VSdDVNaWhXOWhWUW9ZQnVkbUtIRnByXzhvY243elZFcEhjZGxDTzRmWC16d3pFeE0?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
