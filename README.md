# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Who's performing at DNC Thursday night? Pink, The Chicks are set. What about Beyoncé, Taylor Swift? Surprise guest?**

You can read more about it [here](https://news.google.com/rss/articles/CBMi4wFBVV95cUxNMl9hSk5JUlNHTll5dmJKSlBXQXJkdmlVRTFZdllnZWhRNDBOR0JhNlJJMUpQalZJQzNPRGh5OXpkOXlDRE9OWDVoZ3owbWlYU1V4RTlGSjExbmxjTnlSLUE0NkNjcUN3VEJSN1VXOFh2bmRiRzBpZFdaMUNsaHU0Zi1WVzFmTHJlbWNDaGNyWi1xZWQ5MGlxYkI0eEVUcmtRNWtGbUJiV1B0MUdTQzlaTXotYlhQbVplNEJ6Sml1ZGhSUFhTU0tYLXY5NjFmY1Q5Z3QtNnZldnhyVjJfaG9zb2ZOTQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
