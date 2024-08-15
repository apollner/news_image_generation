# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**MAP: These 27 states at ‘very high’ COVID wastewater levels**

You can read more about it [here](https://news.google.com/rss/articles/CBMiswFBVV95cUxOZmx3bGNVaUppNEkzYTl6Ni1zTEZ0Z1JHLW93ZC1Gb1JYaUVzR2RITE1lX2F2Y3pWMmVTakhpMjNYdERTbHRXak8weUEyOHRsYV8wVU5QX0dLdUU3QXozNENXWlVEbTNydGlwTW1YUEQ4N0JLcmdJdGtpSXZwNk5Jb3ZGNDJIeEpuRm1CT1l2V09qeHBJRF9Rd0pjNU1WV1M0VndnVjVKN1VnNnZFTFhTZkZDZ9IBuAFBVV95cUxQenAtS25udGw2a1ZUVTVJS3pMcVBBeVQxM3ppMWptZk5oWTdVdnpEUy1WNHU4SlpBNGhKOVd4QU9zZ3hmdU5QQXZHakVXWTc2cXljcUZQZzZveXdyWGg0R1FHeG5OWTFQWG01ek96cWpUUzllLUg5R1piTHJhZVo1TkUyZE04WHpmaEt3eHRIUGh4cG9lM2F4aFlidjhVY0lseFlkeUhnT21nQ1lZVUJMaTlQOFZkZ1dq?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
