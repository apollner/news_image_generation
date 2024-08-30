# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**FBI releases new photos and details of Trump shooting probe, finding gunman had "mixture of ideologies"**

You can read more about it [here](https://news.google.com/rss/articles/CBMilwFBVV95cUxOdzdEM1Z1eUhaLWhfTmxlZTFpWnZFcmVhNFlYQ1oydXpaamQ4bHZDeEtoZ0JUUE1jS1FMLUZ5UTI1X3FscUZUVlE2RkdJOHdSS0ZrTTRhZk1ORzdkRGZUbXhSckREcHRpal8tYTZYUFptYUhhaVh4ZVJ4SzRQbTdSRUVDRWFLNWQ2Q2xmYkk5OVBVOHZmX2Uw0gGcAUFVX3lxTFBQNHE1eDdXczRyVnl4RlRLNTQ0VzI3ejJiV3c0YXVkQl9wRDY2RkVTRTlCbzhtVTZocmRYQVl1SzdQV0NuVzBicjFZQ2J6dzJyQ0ZjSldKY2YyczdyT3FNN1VYT0daaEJmMzBVblZRM09YcGpJQUdoRVRfTjZPNDA3QlRZYUFXT1RFZk4xV3c1OGxvZ2VCNUNaNXBGTg?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
