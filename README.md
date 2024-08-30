# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Former Stoughton police officer charged with killing Sandra Birchmore while she was pregnant**

You can read more about it [here](https://news.google.com/rss/articles/CBMimgFBVV95cUxNMUt3S3I2U0ltZk12UkRDY2RCNmFVMUg1dktiRUdMYUxSNE9qSGIyQXlpZ1RlV2k4bV9XNGZHZVlkZ0p1SllZWUlzb21kTkI0em9MbHJFdVhhRUJsTkNaQmNLTnNjM1EycXB2RTlnR3Zkel9jV09xeUNxSFh4c1FuZGtBRElycW1qYlNLWVhYa2xNYWVVVUozTnlR0gGfAUFVX3lxTE9MeVdWZTJYQ2RMb1ZQTnFMVEJGRjVPZ3VEUHk3bS1icUZuU3EyNUNzUVhMYlJJU3dDdFlGMnNvcWhlSk5WM2t3eS0ybzk4dDcyZ3daYWhJd0NWc2VoT1Vmd2ktRDZPMHQ3cF9pWkZJYmtqM3ZFVXpzc3k3d3k2aE9oSDVWd1pPZVJ5bEw4WXA1emltMGQ4ZUVxNzFOYnZaOA?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
