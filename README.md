# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Harris’ whirlwind search for running mate enters final hours as she prepares to take new Democratic ticket on the road**

You can read more about it [here](https://news.google.com/rss/articles/CBMikAFBVV95cUxOeTc1QkQyWFdkTkxEcDZDT3JjWnJrUDB0TVhDZXNZM1k4RXJ2OG9rNGNnbFlCXzE0cV8zQ3YwTTI1ZFFzVlgwZ2RaaWhtcHI1dHBrbzRlR2R6cFVVR0I4bzR4NnI3djdwVHphM3FhVHQxVWtjZy1mbVotMHFwVFVpMGUtMFIyeU8weXIzSFdwV0PSAYcBQVVfeXFMTkF0cnd6VS1iemFxS3FIUGZtYThKUjF3T1pkTFpUUk15UXJCVDdNUmRaLWF6SHE4S3lBd3Fyay01b2dWQVgtOTliZ2taWTByc1Z2aFU1cG54dW8xN2wxNVhud0JUNzQ1LW9vdV9KY1VZRE9JZDJmeTkxa3gyQ2FjZmlnTVlhcnRn?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
