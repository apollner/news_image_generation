# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Travis Kelce’s dad has scathing reaction to Kanye West’s ‘Vultures 2’ lyric about Taylor Swift and son**

You can read more about it [here](https://news.google.com/rss/articles/CBMipwFBVV95cUxQTWs0R0pNSzNOV1R6eWZibFdtcmtSZ1N6Vk14dmUtTnZ4ejJ4bmFkWjZKaTdmaVVJQnNHbWhfaVBwLUI4ZThabTlzLTFOQkN6V2k3ZlFfR1Q2X003eGRMMFFTSW1yeS0wbXVwVHRJMjhGd0hKUUFZenRWM0RHUlhWWlJNX1M3NmVZTnlsX3hCNzZiUzlXZFBfNEFPNkIyVVUxNl9hN2MyNA?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
