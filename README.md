# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Tech consultant found guilty of second-degree murder in stabbing death of Cash App founder Bob Lee**

You can read more about it [here](https://news.google.com/rss/articles/CBMiigFBVV95cUxOUS01dk9NMng2QXlaZlB4emkwNWI4QVhwMHNNWXpfc1NDVVFSdlppdnFvRUVnT3FIcWdsWWs3WWJDOTVWbUJVZ0NfbnUwRE9MRnhVanVSM1ZsblhEYlotWjB3MGpMQVQza0JvUE00RVZVa3B0dzd2ZnBjUmEtUVNmRm9VYW5WM0hULUHSAYABQVVfeXFMTmZiU1Q1eWVKUU04QzRsNnRFN21KbHpSWE1RV2I5dW1kTUNaR0UyQXBRRzdXZThzc2RjUU1od3VPeGhMdkc0akN3NmtQUnhVNC0xdXhQS1o3Zkd1cHRqRkJqa2JqY3RCYzFJWXFkUFlvSWd3b1JEZjFMcVNmRkNMY0g?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
