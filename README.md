# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Cellphone video shows 49ers Ricky Pearsall after shooting in San Francisco Saturday**

You can read more about it [here](https://news.google.com/rss/articles/CBMiwAFBVV95cUxQWm9lVENXOHE1bnZnRjk3dWJuSG5KTFViN05fZVpXSUtBdTJqdnIzYnJVd29VOWpFSUxzZzV3ZkxSY3l5LTU0NE5nSzZpOGE3LXlNS05yQnFFYXdyWG9vOUV4b2xWeERvc3NyMFJDRlVBeVBHUjhnUnNhbE9OdDRYTkhfS2lFaHJTY1Zha1pxTVQtX3B2c1VvYk1weGk2cjdOYTV6bFBPUlVLSkhwNEZvTUt6Q2E0OG05Sm5Vb09vd0rSAcYBQVVfeXFMTU1WYWhmYldQTHo1blhkaVVGNkstOWtLdS1vVkxaR2t5ejVfV3hVdlJfb1VlSWhsMmVUVFZWTjdKMU9BRk9oTWRfNlVpSjE0dFZJcS1Ua1pVRlpxd0pCOVV5M0VTYzNKMjBxcDVTd0QxU2VQbDdUcEFDOV9Tbnc3TnBnSjlKenhtVElQSEVVNkllSE53U2JIWTVFakphNlFJQXVqNV9kM1VRbGhCYmVxdjBDSDVucU1FWEFGV1ZadkhxaVFIYl9n?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
