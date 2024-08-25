# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Ex-Alaska Airlines pilot who tried to down flight while on magic mushrooms trip wants to fly again**

You can read more about it [here](https://news.google.com/rss/articles/CBMi6wFBVV95cUxPWDZsWlpxd1Y2dFRuWS1oNmF2VGJ4eGRWTnl1MXpBMm50Zm5RX0lLSXdUaTViNzVqZ1k3dlNsTnl2eVBIN2dLX2drZm1fV2tsVW1vNzdkWEFrY1lhWW8zM1dGZVp2akJQZXBTNklkZDRadW1NbUlDQTRKS05uSnUxVHNsY0JOejhMVWlGaE9raHFaX0dOYlVNT2l2STR3Rm1NQm9KQWdEckZZbVk2UExWYUp2d21hUEd1eVNTcXBneGtzS2NXUUQ4WnJiS3hSYW10UjEydVhTWHNqRDhoa1I2VWp5ay0wR0oyVEVN?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
