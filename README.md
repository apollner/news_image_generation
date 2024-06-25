# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Supreme Court to weigh state restrictions on gender-affirming care for youths**

You can read more about it [here](https://news.google.com/rss/articles/CBMifWh0dHBzOi8vd3d3Lm5iY25ld3MuY29tL3BvbGl0aWNzL3N1cHJlbWUtY291cnQvc3VwcmVtZS1jb3VydC13ZWlnaC1zdGF0ZS1yZXN0cmljdGlvbnMtZ2VuZGVyLWFmZmlybWluZy1jYXJlLXlvdXRocy1yY25hMTQyODI10gEraHR0cHM6Ly93d3cubmJjbmV3cy5jb20vbmV3cy9hbXAvcmNuYTE0MjgyNQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
