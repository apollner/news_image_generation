# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Gus Walz broke the internet with his tearful love for his dad. Then the bullying began**

You can read more about it [here](https://news.google.com/rss/articles/CBMihgJBVV95cUxQWjJYTi10bTJSMkU3RUVGUm1lX01YWnB0US1oSHJ1UlNxWGxfTjdsMXhTQnk1OFRZdElLakh3WE4wZVBxc2N5QTBkZTRLekdVRENxZkVjdUFnTjZWT0lrVGtCdUZzdWNyeEoxcUNRMEE3SXp3YmpfOGNyTEppaGIxb2pBN0xNR21aRjBMNW8xWWlZcU9FTWZ5VzRtTjFobmJUaEpSWFJocW9XYVpTSmtDM3BsYWkwZktodWZYWjRlSkVNTEdleVRUa2hSRDNyRXB0dGhiZzFVaG1meTNhTWJybzFDM2RDNFNjdmZINW5KSUlRaEVvdUZzUE9EMWJmZElvNEpwa3NR?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
