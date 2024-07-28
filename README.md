# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Rocket attack on town in Israeli-controlled Golan Heights kills at least 10, rescue official says**

You can read more about it [here](https://news.google.com/rss/articles/CBMicWh0dHBzOi8vYWJjbmV3cy5nby5jb20vSW50ZXJuYXRpb25hbC93aXJlU3RvcnkvaXNyYWVsLWhlemJvbGxhaC1maXJlLWV4Y2hhbmdlLWtpbGxzLTMtbWlsaXRhbnRzLWluanVyZXMtMTEyMzMyODYy0gF1aHR0cHM6Ly9hYmNuZXdzLmdvLmNvbS9hbXAvSW50ZXJuYXRpb25hbC93aXJlU3RvcnkvaXNyYWVsLWhlemJvbGxhaC1maXJlLWV4Y2hhbmdlLWtpbGxzLTMtbWlsaXRhbnRzLWluanVyZXMtMTEyMzMyODYy?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
