# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Moldova's pro-Western Sandu claims election win after meddling allegations**

You can read more about it [here](https://news.google.com/rss/articles/CBMivAFBVV95cUxPM0JTZ3NHUlI4QWJiREZ0NmJ2c1BPZXRxaE9rc3U5NTY4M3FBblF4OWpGNC1TcFliaFhmbGQ5UTd5SGxxSlFRNWJSaXkyNkowUDNydGhNN0RleVdyQkpLbzBiUTR4MktfNnB3eHByR2dCem5lZHMxNjRCM244bjBkZ1dTeks1UDdTY3lSZm1rOVlwSHRNN21sMjVyQ0ZBbGpVSTR0Z0tHNjJ1QVJibF9EenVmeFJtaHdlNzYyaw?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
