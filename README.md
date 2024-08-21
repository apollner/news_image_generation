# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Stellantis says union can't strike over Belvidere, claims it hasn't violated commitments**

You can read more about it [here](https://news.google.com/rss/articles/CBMixwFBVV95cUxQSHNYRlJHamZLazdOX1dvanVGUVRsSDM4c0pnRFl4WjBQVjFtdm5hTU5sVmZNWi0zVVdsUzdFa0xWdEJJOXdFTGY5bWNWZFp3QnFRTTByMnk5ZU5MMEEwbE1nV1Nod2UxOTIzemJPeXA4OGlwU0pneWdiQS1MQUFZZjZzc0luS0hhd21RUnZNTUM1Q0k3c0czNGlCZFBmNm81YWpQRkZaZmdndV9xZDY3WDZLLUg4REZDYlh3SVFYdFJsOTg5enow?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
