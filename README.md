# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**More Listeria Recalls: What To Know As Nearly 12 Million Pounds Of Meat Recalled**

You can read more about it [here](https://news.google.com/rss/articles/CBMizwFBVV95cUxPQnoxUDRPZ0JfaEdndDhpSk1YSFNrNlZZSXdoUDZTX3kwUXNaQVRJQXRVNS1Xb2dCM2wxVzZCOGFtdlBsUjR0X0VsMGliQm1jWWJrM2psM2lEUFlNdkRvbVl5cW94ZXRVd0F3THJVMlNvazE4bG9KaC1aU2d1dExKcDJ3SVRvQ1lwQlh2Y2xDSFBmSFFWR21DaEZYVnRyZC1hQVduMkc4YWV3aXppdVFUWGFOY0xJdWtQcjdFdmloSVB6N1c5dXdsWHJtMy1LeVU?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
