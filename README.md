# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**'Knocking On Our Door': Experts Warn Of Bird Flu's Pandemic Threat**

You can read more about it [here](https://news.google.com/rss/articles/CBMiowFBVV95cUxNTEI2TG8wZlZiM09pdjZybzNCclhHU3QtWmt6TjNHZHhoLWRVVDRZTndZM204Ry1Gb004SXM4bC14RERhN1I0aVJEZ0JQWlVZM1p2QjgxLTZxTF9BbUFRb0xrdnhBTm14a1V3bkxNemE2Z0hJbTktWVhrUXdtMkZFMkZGQjJGSC13YkhNV0xrWE1YTVFBcVpyQy1mVnNaSkZOalhr?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
