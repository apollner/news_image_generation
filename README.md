# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Michelle Obama belittles Trump in starry convention turn**

You can read more about it [here](https://news.google.com/rss/articles/CBMiWkFVX3lxTE1CV3ZwZnNxQW5RU1hjcXpVNUQ3Y1RjVW5ud0plNC11OXhUWEh3Y050aTI4MTJCSjVxdWNMUFNoS2VTcFU0TnRyV3hwazVOaEwzZjJ4bkVobzBZUdIBX0FVX3lxTE9QSTIzOGxreTIxVWMydzMzMlpCczZSZFpXVDFyVTNmaXQ4cE5vMDI1Y2s1UHprdHkwQVhnNjVHb1JrbHhSWUw3VGVoSFAzaW5qZ055dWJodElLQm42ZVgw?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
