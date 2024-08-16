# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Hidden-camera video captures Project 2025 co-author talking about plans for second Trump term**

You can read more about it [here](https://news.google.com/rss/articles/CBMijAFBVV95cUxNenJqVlJZenpTLTB1emlKOEFSYjRTRkhqLWt2UHo4YlVmVjRfZl9wSE5IWGx6WVNSVWZLN3ptREU3MVpsRk02RUF1Sk5kZjlDZVRrVHcydVBJNnlTVld2LTM3c3UwUnR1Mi1fdjJDS2o5SUVLZGRmemxzSXpHTnN6WnNNckN6aVV3Qi1kOQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
