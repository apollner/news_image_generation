# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Watch: Patrick Mahomes makes behind-the-back pass after Travis Kelce messes up route**

You can read more about it [here](https://news.google.com/rss/articles/CBMivwFBVV95cUxPa0cyQVFGLWlnWjl0cnBIYnBMdjZZdUV3NXF0WmZfNjY3alBiWWpHcEQtN1k4UUdzQnJaMzdWb2g1TDhDRHZFWV93OTd5WGctdktVeHlnZS1RUjFNX0pqRzItWFp2ay13dzY5X3d5UEdhVFdmcmJENGV5ODZwRFp6cy16TjU5ZktRU2tMZHg5Q3d4OENyT0NpM0ZqME00enE2Y2hQZDB6MkNIaUVwWDUzNkYtMEJiYjJwRWMzM19YOA?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
