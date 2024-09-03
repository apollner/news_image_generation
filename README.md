# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**UK announces partial suspension of arms exports to Israel**

You can read more about it [here](https://news.google.com/rss/articles/CBMingFBVV95cUxPdGxES0x3dmVHbzFlY0RaVVNmVnV5cVBqR3dBZENDS0NhOTNwdUIzVDFpeTdiajRJQTJ0UG9TdEs2SGpnNkZTTlprVm9xNXBIQXlVM0FBSTF0MUh0WnJ1bnlwN1RJald0VlZqMmtDeVdlWjh5QWctVG40Wmk4azNiR3FnMHVMS3puREtVeFI1WHptWS1RVWxEWVpvZHVUd9IBowFBVV95cUxOYUtuX2I5ZWQzc2FJOUxMOTN2SzlLXzl6emM0XzZuT0JHbkVKYkVwTzJJd2RYQzhDQW15aVFWMVIzSUZTOUlNZjlQcnBraEtiTmtQaTRqWjlwZ2l3VlNzVlhKOHpmVEVXNE5SUldYdVJHQV9mT2lqSGxxSWI4LTVZWE9BSGNEY29BT2pRODMtNVdjRFhhc2NoNElpUmRQLUZBcFdZ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
