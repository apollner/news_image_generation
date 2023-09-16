# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Trump says it’s ‘very unlikely’ he’ll pardon himself if he wins 2024 election**

You can read more about it [here](https://news.google.com/rss/articles/CBMiaGh0dHBzOi8vbnlwb3N0LmNvbS8yMDIzLzA5LzE0L3RydW1wLXNheXMtaXRzLXZlcnktdW5saWtlbHktaGVsbC1wYXJkb24taGltc2VsZi1pZi1oZS13aW5zLTIwMjQtZWxlY3Rpb24v0gFsaHR0cHM6Ly9ueXBvc3QuY29tLzIwMjMvMDkvMTQvdHJ1bXAtc2F5cy1pdHMtdmVyeS11bmxpa2VseS1oZWxsLXBhcmRvbi1oaW1zZWxmLWlmLWhlLXdpbnMtMjAyNC1lbGVjdGlvbi9hbXAv?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
