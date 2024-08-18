# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**OpenAI’s new voice mode let me talk with my phone, not to it**

You can read more about it [here](https://news.google.com/rss/articles/CBMimAFBVV95cUxPcEhmODlYdGRkWF9lTDlyRjRnVlZXUklUNzgyS0lfbkRRYmJ4MklSbFIzQk1HclcxZ296RC0xX0k0T2dQUkk0a3I5VFBzdk94eG0tQ2FVRkx2d3Z5STV3NTAyZWtxQnowYXZOX015d2Z1VC1JT0ZGOW9yMTdHTTlWZGUtTlNHYmNXeDQ3Zlh4SmcwdzZKMXd3Zg?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
