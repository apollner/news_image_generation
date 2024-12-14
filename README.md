# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Up and over! NASA's Mars rover Perseverance reaches rim of its Jezero Crater home (video)**

You can read more about it [here](https://news.google.com/rss/articles/CBMi1AFBVV95cUxPOFRRQ0oycnZiTmVtYUtiY25TV2FLdjA1TkM1LTkwUmp5THpVZThWNXhnYWh4RnUtd3V5ZzFiTUphTGt1d3pJR1RNZW4xMThhNzB6OThCc2VKM0RGeGthSk9pX0hZRFlUQ0g3MDRLcVhLSkdHbkxwNGpOVDRFT3ZvV1pSbC1hWGRvdl9mZ19sblBKS3NNdGx3UkNpTXNZVFU2LXo4WXJ0bjBNQWxxNFZIa19BTTlQSnJVMVpYMElyQlNuekRFcFdaamU4R05hMmNuYzI2Yg?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
