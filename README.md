# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Moldova’s pro-Western president wins 2nd term in runoff overshadowed by Russian meddling claims**

You can read more about it [here](https://news.google.com/rss/articles/CBMiswFBVV95cUxOYmx0cWhKOVhjbUY5YTQ0LWROSXkwR3k3U2VhenpoX200c0xBX2llMzJONUFZYUFZb3RzTlNadkMxTUhPd3JwbWVuWjczZzg0cjlGb2dzNU5Kc0FkdUpZeTdTZUhRMGNuVXJvQ195NWUzNzN3QUVGSUZnYW1PXzdJVjhJZUhoTTBnMDR4TEkwZXZNbU5VUC01X2U4SFBKZGtOTGE4VmNpQkViU0pLWGVWdFFGOA?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
