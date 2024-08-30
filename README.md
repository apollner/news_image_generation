# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Taylor Swift concert terror plot intended to kill ‘tens of thousands of people’: CIA official**

You can read more about it [here](https://news.google.com/rss/articles/CBMi0AFBVV95cUxQQ0d0cHBvM1NoYmVYOWM3T2VrRUF0M0ZrM2Y5UWZvWDkzeFlBMnotdHRVQnJXaDVSSllDUHhQLXFIZFpJbFhUYWRLeGdlQ2IxZzRDNUd0eGs3QjJmSXdkVnlqR3RHc05pVk9sQnFkaHFuVndfbGlkQWllSzZxb085S3JwbzdhNlFweHgyU0RXYmZIS3diNmNMZWFpZGZibktOb1VvVUZxUFdBd1Y4OUZOUlZqaVdYc2I4NUlMYXNFMWpUMm9KZnhtYm1TNEQ0VmN2?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
