# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Trump Staffers Allegedly Involved in Arlington Cemetery Drama Named**

You can read more about it [here](https://news.google.com/rss/articles/CBMingFBVV95cUxOSUtIeEZVS0VZSjcweUt0Y2NiYXRWaEFkM2J3VnFHdW1HMjA4S1ZPZElCelRfWi1YT2tfRUp2MkFvRGI3MTdLV1NkVWdZSVBHRXpJa1ExV1c5M1lVei03eFpZbmdqWjl3OFM1dHduWnNOYnNYMk8tUF9CN3hBb1A5UXFjV2NzQ2NPd3VZQ29HeUhHbXpTZllJV3l2UUo3QQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
