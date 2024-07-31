# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Gemini Daily Horoscope Today, July 31, 2024 predicts productive results**

You can read more about it [here](https://news.google.com/rss/articles/CBMijQFodHRwczovL3d3dy5oaW5kdXN0YW50aW1lcy5jb20vYXN0cm9sb2d5L2hvcm9zY29wZS9nZW1pbmktZGFpbHktaG9yb3Njb3BlLXRvZGF5LWp1bHktMzEtMjAyNC1wcmVkaWN0cy1wcm9kdWN0aXZlLXJlc3VsdHMtMTAxNzIyMzQzMjkzMzA5Lmh0bWzSAZEBaHR0cHM6Ly93d3cuaGluZHVzdGFudGltZXMuY29tL2FzdHJvbG9neS9ob3Jvc2NvcGUvZ2VtaW5pLWRhaWx5LWhvcm9zY29wZS10b2RheS1qdWx5LTMxLTIwMjQtcHJlZGljdHMtcHJvZHVjdGl2ZS1yZXN1bHRzLTEwMTcyMjM0MzI5MzMwOS1hbXAuaHRtbA?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
