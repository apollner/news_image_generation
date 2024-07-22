# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Richard Simmons’ Team Shares His Final Prepared Social Media Post 1 Week After Death**

You can read more about it [here](https://news.google.com/rss/articles/CBMiZWh0dHBzOi8vZGVhZGxpbmUuY29tLzIwMjQvMDcvcmljaGFyZC1zaW1tb25zLXRlYW0tc2hhcmVzLWZpbmFsLXByZXBhcmVkLXNvY2lhbC1tZWRpYS1wb3N0LTEyMzYwMTY3NjQv0gFpaHR0cHM6Ly9kZWFkbGluZS5jb20vMjAyNC8wNy9yaWNoYXJkLXNpbW1vbnMtdGVhbS1zaGFyZXMtZmluYWwtcHJlcGFyZWQtc29jaWFsLW1lZGlhLXBvc3QtMTIzNjAxNjc2NC9hbXAv?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
