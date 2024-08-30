# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Thai court sentences a YouTube chef, who is the son of Spanish actors, to life in prison for murder**

You can read more about it [here](https://news.google.com/rss/articles/CBMiugFBVV95cUxOQ1VkZ1QyemJhN2hiQm90dDc3NG5iOHlxanZpQXBRMWJnM3RySHBRZEozZklWOTZWOWIyTEFqNVI5cUFYWVdabkRoc0hWcUlQRUg1X2liRzNidGF5Z0xOLUxoY1lidkVLd0VSeTlHNV9WOUxoM09WTUkwT0Zpa25ITkFkcDdaaGdNV01CX2xod2dJRUxETFBNRl9KdkxodjVOUUxPY0lWa3VnclBYU2U5RlV5Mm5QVTNOeUE?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
