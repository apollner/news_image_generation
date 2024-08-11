# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Israel strike on Gaza school kills more than 100, Palestinian news agency says**

You can read more about it [here](https://news.google.com/rss/articles/CBMiwAFBVV95cUxQLXZxNXlPSWZfaEI5MFZZSVYyOTd5bmpVY3F5Zk9OWG9DSVJIZVE4OVdMWC1vdzFUUDJrbmRHWnp1SlNsZEVlX0ZBbm9vSG5WQ3BFamh1dWlaSnpLdXBRTG16clAxdzZtaEdSU2xtUFdkeWptNUdlUUE0cmdrMEk0UTcyOGhfaHg0cXJfZXdnWWtsalU1TFRsZzZ5YUQ1TTVkZjE3dkxMaTFJeEEwV0FJWUU2YUFIZUQ0eGxiTENRUDU?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
