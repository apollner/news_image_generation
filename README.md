# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Team USA vs. France: How to watch the USA men's basketball gold medal game at the 2024 Olympics today**

You can read more about it [here](https://news.google.com/rss/articles/CBMi1AFBVV95cUxNRkxxT0N2UFY4b1VYVXRqRktnQXZFOHM3Y1ZZYVFQOFRjc0dqd0t1UTNBd3F6UjNnT1FDQWFtMkF6ZHJCeG1keV9mSkV2eXIzNzdJRmF3UzQ0TDE0ZlF0SlhXeXVxNTRtbGhPZm9QTERTSWdpWS1kSGVURFd5V2dZRVZxRjF2WDBqM09lSjhzb2NJbjNrVVF3bUlGZ3BJWTZtXzJxZ0w2bjB6QkNldUpFYkgtMzlOdlQ4T3RENEhzbGZHQ18zeXd4NklvWnZVY2xPNG4ySQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
