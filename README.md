# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Red Sox Outfielder Jarren Duran apologizes for using homophobic slur**

You can read more about it [here](https://news.google.com/rss/articles/CBMiqgFBVV95cUxOVy1MUWo1bVI1dlZXM2U5M1h3b3BBMzF0eGJpMUNwTnJJVkx2S0NiRk9idXp4ZVF5cThZY2dIWEstZmxpRHphbVhsNFJsOGNxanlOVkFYVEp4VFlocTdzU09KZUwxWUc4bW80aW1xajFCU19kSDkxQ0c2SEVJdWYxQU5wR3g2Z3Z0UmZSRnhxZHUwZnVaczZ3eUdzdFFtQ1lsR3dfRTlvTnAtUQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
