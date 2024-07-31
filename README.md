# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**2024 MLB trade deadline tracker: Follow every major move for Yankees, Dodgers, Phillies, Braves, Astros, more**

You can read more about it [here](https://news.google.com/rss/articles/CBMi1gFBVV95cUxQRlREZjNVVVlya0pvY0E3MmExUnpLc3JiSmp3WEM0bVZkbU90S2UwaGoyTUJYdkxtTl9zWkZtODNUbnZQRkJoa0tORzM4cnd3cnlOUTdRc3cxbk1CbnVObFFaakJHeFZYNGNvZVRtbm9WSXB6YmxkUTE5TThKNG9oT2tUYlhQdkFfdktLYkhqNHp4el96OUtFQjdQTWxJR21CYlkzZEJtM2FOb3I4OW9RcTN5cFpBaXVwbTlPd3MxSDUzN19WWDF2N3R4b1J3Q0JkeHloQk1R?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
