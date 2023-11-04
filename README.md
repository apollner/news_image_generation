# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Clippers' James Harden -- Can 'fit in with anybody' for title run - ESPN**

You can read more about it [here](https://news.google.com/rss/articles/CBMiWGh0dHBzOi8vd3d3LmVzcG4uY29tL25iYS9zdG9yeS9fL2lkLzM4ODA0NzU2L2NsaXBwZXJzLWphbWVzLWhhcmRlbi1maXQtYW55Ym9keS10aXRsZS1ydW7SAWVodHRwczovL3d3dy5lc3BuLmNvbS9uYmEvc3RvcnkvXy9pZC8zODgwNDc1Ni9jbGlwcGVycy1qYW1lcy1oYXJkZW4tZml0LWFueWJvZHktdGl0bGUtcnVuP3BsYXRmb3JtPWFtcA?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
