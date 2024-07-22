# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**At least 7 in New York sickened in listeria outbreak linked to deli meats. Map shows number of cases across U.S.**

You can read more about it [here](https://news.google.com/rss/articles/CBMiRmh0dHBzOi8vd3d3LmNic25ld3MuY29tL25ld3lvcmsvbmV3cy9saXN0ZXJpYS1vdXRicmVhay1ueWMtZGVsaS1tZWF0cy_SAUpodHRwczovL3d3dy5jYnNuZXdzLmNvbS9hbXAvbmV3eW9yay9uZXdzL2xpc3RlcmlhLW91dGJyZWFrLW55Yy1kZWxpLW1lYXRzLw?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
