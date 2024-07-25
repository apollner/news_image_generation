# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Timothee Chalamet sings Bob Dylan in A Complete Unknown trailer**

You can read more about it [here](https://news.google.com/rss/articles/CBMiWkFVX3lxTE1NYUtnV1RPeXhxR0VQS1RESjBCQjc4RkUwakhNWnprQUpaM1B5b2NiTnNPUEFWYWtMNkp0Z1M0aEx2YXJwaUNBbnNCWlgwZ2otVklkaVJPWlV3d9IBX0FVX3lxTFAySWxBNWVSSTVKWUd6OXU0U0NuTDY2NEZzMW1HWi1DSll4Zm1ueTZGX09EUzNpam1pOFJubjhuaGU1ZDlMNDZaaldDVVIzMHBNZ2Izb1FReGJ4a05kc0ZN?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
