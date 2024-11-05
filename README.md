# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Asia stocks rise with China stimulus, US elections in focus**

You can read more about it [here](https://news.google.com/rss/articles/CBMitgFBVV95cUxOMWEwbjJlRWtGSjRScnlIUFRheDBzWF9NMmtPYW1TTlR3ZkNhUlRKNC03SzF1dkVlUzRPNEt2dko5ckJhd1pROGxlV1RpZGJWSkhydWZqQ19uYlM4c1BLYk9RYTZCbUp3ZV9NZFg2aE1BNld6VnNlSHM4cXVocHpxU3ZoM3puNXU3b3pKV1dwZ2pkV1ZnZFhabkhYWFo5cWNlazZDcTgzSkZWY2I2UHg3ZjB4OEcxUQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
