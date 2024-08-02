# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Israeli military says it killed Hamas chief Mohammed Deif in Gaza last month**

You can read more about it [here](https://news.google.com/rss/articles/CBMijwFBVV95cUxNUXZqOER2UURqcGRDelFBYUhsTDFXcjFoVDVNRHBxaW1TU183VTZYdllNajd6Sk1iYXRVZHFpLVJLeF9vbVRMNDh4ZVdQMVpZNDFuOEdiWW9WazgzanU1VFJOVVdRQzE4X3cyZGdLRWdXSl9FNVQzX0Y5MmwyVGYzOUQwRGM0QWRRT2c4aF9pb9IBhgFBVV95cUxQQ19qQWdESEdpXzh6WVI2R29Tc09oT1Q3bTVUTUI0c3pEMTNhQk1LYWdrbDhjVE05WndqcFhqRGpBUWJ0bE5WdVRQaDQ4NkZIUWtLMzE2c2hGTVpNNy1UcDdyOGFuZk5iX3otblU5YmtBdXZwRFM0ZEItYThneDJOOUhCaU5Ndw?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
