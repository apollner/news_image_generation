# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**How Syria’s rebels toppled the Assad regime, in 7 maps**

You can read more about it [here](https://news.google.com/rss/articles/CBMiggFBVV95cUxOeHFQeGlGaVNrcGo4LXpsd0Nnd0lLTXJka0NURjJwYmZ4Q1MwN21PX1NxWkJuNmItWHBKSUItSTJJay1BTFFJNnRIWlllU0dnY2RtRDlLN2xFczJrUEVPUUhFWHpQZ0pQNWFkYVR3enN0WXgzenlIalhNME43dGxiM1pR?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
