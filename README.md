# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Nintendo Direct Partner Showcase & Indie World Announced For Today, 27th August 2024**

You can read more about it [here](https://news.google.com/rss/articles/CBMixgFBVV95cUxQUHFYVGhYRU9URnBMcm4tRzBPeWFsRnk3QWFmMGZLOWZvdkVsc1pQb2NySEhSY2xCMTZmWUljZjVaVzZqajFWNEVXWE1NTkVDcXJnc05hbFhSVUxTOFpsOVBEWHh5eXVnRF9Zei1IMGpYWnlwYnNyVWZyTzc4SjRvcjl5cGl0cElSX2ZORTc2T1o5RERTem1YRzFXcnVXU2pBYlpuZzZhMEh1aE5KR3lmbUIzWGdKa2d5R1N2NVB0VkJ0ZHU2TGc?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
