# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Team USA vs. Brazil: How to watch the USA Men's Basketball Quarterfinal game at the 2024 Olympics today**

You can read more about it [here](https://news.google.com/rss/articles/CBMi1wFBVV95cUxOQkFLVFVFbzM4NDV6ZEhuUURDUjFpZGFjS0VZdDFuN2ZYajFVVG1KNWxlekVBeUZKdk1MVEpDWnloSGY4bC1aZUJVckQ4LUhzVWQzcDhiUHR0ajBfZFM0RVA1Vkt0bTFRVERYNFVwSm1JbVBUMVN5MC1xWXFQc3RYc25jSTRBNUJyUC1OeG1MUnhPbVk2ZVhFVmc5MGo0cE9OSm9BQlYxOFFrV1VXc05xTmZGbzB1NGkwWlJNSTU1cFpseHFpNjRSUkh4Z1BIUFhLRmtEOC1OVQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
