# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Isaac Hayes' Family Demands $3 Million From Donald Trump Over Song Use at Rally**

You can read more about it [here](https://news.google.com/rss/articles/CBMiggFBVV95cUxOQjg4M0JRZUkwMkNqLV9jMmF3RHJsOVdFekl6akpRR1hHZHNHbFZhSm5rQk9VeUVhM3VCVnoyVDVULXpzMy1CcjNMamR2LWZDQ1NMMmJrOXhVcHVPZEMtLUFERHkxNTVMQW9Na09TYzVtLWt5TnBTTXVpYXpIZkNvWTNR0gGCAUFVX3lxTE1EREc0cG9VWDl2MmZzRVptRWQ3NUREb1hENm1mQldtWlNpQjN4NUNRZXFnYXAzWHRSVnhSZHFrSWFaZFAyQV9IZzRhNDZpeWhySTItTVcxNWhaTDZlekdYWnB2NGxpdUdVODhBbDE4VHlnWEE5MzFkZWp2RXBlN1AyN3c?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
