# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**French woman allegedly drugged by husband, raped by dozens of strangers appears at his trial**

You can read more about it [here](https://news.google.com/rss/articles/CBMivAFBVV95cUxQYThnRG9xcmRXYUZMMDYxZEctLUpnN2lmOThfZEdaTU51VFRKZ1BTc2pOZm9WeDFoeXZqX0RfQUJab19ZQzA3c0k4TTRtYmlmTnNFcGhXYnFsakRGSnRQZzg3OV9LSThMLUhmRkZmWGhkZF9HSzEwTnNsN1hjWjVBXzhsY3hDc0dHRVU5T0xmaEpBeG95azQtY2k5QmtubkQ2TWd5ekdZRkhjekJEOW9Ra0lWdnY1UGFRQXRyMQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
