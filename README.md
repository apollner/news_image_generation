# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Election 2024 live: Harris, Walz wrap up Pennsylvania bus tour as Trump plans DNC counter events**

You can read more about it [here](https://news.google.com/rss/articles/CBMiuwFBVV95cUxPYWJ5Z2FpcW91R0lQOS1EQ0VjQkY1OFd3c051LUZuYUl3d3JPamxneWRFTEw3NFgySC04d3ZOVGcxT1BqUGVqUlJmdzNCeExFQldvWTZRakxqazZNb2k4M2ROR0JwaklTNFkzTUIxZGNPMkx0cXdSanF0b2RraEk5b05OaTJMN2haQTYzSnlvQUdvVzlFdXliWG0tTERibzgtNGNVUjdXRmlRN2YtenR2eFFxYjFJU1MtV0JB?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
