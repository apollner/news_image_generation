# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Biden to call for major Supreme Court reforms, including term limits, at Civil Rights Act event Monday**

You can read more about it [here](https://news.google.com/rss/articles/CBMiTWh0dHBzOi8vd3d3LmNubi5jb20vMjAyNC8wNy8yOS9wb2xpdGljcy9iaWRlbi1zdXByZW1lLWNvdXJ0LXJlZm9ybS9pbmRleC5odG1s0gFGaHR0cHM6Ly9hbXAuY25uLmNvbS9jbm4vMjAyNC8wNy8yOS9wb2xpdGljcy9iaWRlbi1zdXByZW1lLWNvdXJ0LXJlZm9ybQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
