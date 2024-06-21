# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Putin arrives in Vietnam as Russia seeks support in face of Western isolation**

You can read more about it [here](https://news.google.com/rss/articles/CBMiUmh0dHBzOi8vd3d3LmNubi5jb20vMjAyNC8wNi8xOS9hc2lhL3ZpZXRuYW0tcnVzc2lhLXB1dGluLXZpc2l0LWludGwtaG5rL2luZGV4Lmh0bWzSAUtodHRwczovL2FtcC5jbm4uY29tL2Nubi8yMDI0LzA2LzE5L2FzaWEvdmlldG5hbS1ydXNzaWEtcHV0aW4tdmlzaXQtaW50bC1obms?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
