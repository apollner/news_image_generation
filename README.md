# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**George Santos expected to plead guilty in federal fraud case in New York**

You can read more about it [here](https://news.google.com/rss/articles/CBMiggFBVV95cUxPeXVRQzVpcmtFRUVTbVUzeGtPM1A1SVF2MENFYXhGQ2xWcGZJb3g4NmQ0cG1XaEp3WXJqMHh2eUJUVVVEYXJ2WGZ0NllfX1JsQk9jQTI3VUpGdzdJaW1PdGpmd2NHd0ZKeWdjcWRiTXl1SkpfUVRlbWxyWEpmejBCMm9n0gGHAUFVX3lxTFBpUDlGSExocWxtOXlJQUNWYnY3OFFuemkxOHEtUDZNLWVVRUxMVFE2NnNXY215OXhwM1pwOVAxeUVOOUdXQVg5QmVpU1ZVR3daUEhwRzFlbG9HT3VUS3RlUEI4LThuTFh4eW02VnczekxOTzFZNzFfQ2pBY0U1UUVDdXM0dWNacw?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
