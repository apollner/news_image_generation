# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Netflix Tops 277 Million Subscribers With Strong Q2 Gain, Beats Earnings Forecasts**

You can read more about it [here](https://news.google.com/rss/articles/CBMiYmh0dHBzOi8vdmFyaWV0eS5jb20vMjAyNC9kaWdpdGFsL25ld3MvbmV0ZmxpeC1zdWJzY3JpYmVycy0yNzctbWlsbGlvbi1xMi0yMDI0LWVhcm5pbmdzLTEyMzYwNzY4NDMv0gFmaHR0cHM6Ly92YXJpZXR5LmNvbS8yMDI0L2RpZ2l0YWwvbmV3cy9uZXRmbGl4LXN1YnNjcmliZXJzLTI3Ny1taWxsaW9uLXEyLTIwMjQtZWFybmluZ3MtMTIzNjA3Njg0My9hbXAv?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
