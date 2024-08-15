# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Liquid water detected on Mars — but it's buried deep beneath the red planet's surface**

You can read more about it [here](https://news.google.com/rss/articles/CBMitwFBVV95cUxQd3hPZVZ6RmdlaHRERlhnenZPM1NjMjBtT1VDOG4wZGhKOUZFT25FYzhGOGs1SVNTT00tRE1FYi1HNFhsYTNpZ2VjbU14cjNqTFVLdW5YaXhzd19zRksyNy1UQ0ZEUGVCT2tyOTN2eWRtNDV1TG02ZWFaS1hyM3hLMk9YbFB6YXJxUVVweUFGcS1TYW1JQ2pnSmlEZ1NUdGtvMDBBX1hJTE40UEdOSHhhMm9ZR3hkY00?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
