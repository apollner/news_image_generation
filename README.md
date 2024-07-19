# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Travis Kelce Attends Taylor Swift's Eras Tour Show in Germany**

You can read more about it [here](https://news.google.com/rss/articles/CBMiXGh0dHBzOi8vd3d3LmV0b25saW5lLmNvbS90cmF2aXMta2VsY2UtYXR0ZW5kcy10YXlsb3Itc3dpZnRzLWVyYXMtdG91ci1zaG93LWluLWdlcm1hbnktMjI5Mjk40gFgaHR0cHM6Ly93d3cuZXRvbmxpbmUuY29tL3RyYXZpcy1rZWxjZS1hdHRlbmRzLXRheWxvci1zd2lmdHMtZXJhcy10b3VyLXNob3ctaW4tZ2VybWFueS0yMjkyOTg_YW1w?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
