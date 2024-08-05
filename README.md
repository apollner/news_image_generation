# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Group of ancient stars spotted near the sun could rewrite the Milky Way's history**

You can read more about it [here](https://news.google.com/rss/articles/CBMi2AFBVV95cUxPd0NkSnBrLWxGN1VkRUFvazR3UjBZMDNBQUR0eFJCbmV2bU91ZHo0M0hETWxYRTVlazR0RzktemRKSW1ULUk1R0dCQUxpOHRvMHZBTVhmcnpJTEhsVXA1X2UzN2Y5SVAwM3V4U0xHX3E2Z0tXTlI4eUFJTVpMWUxzc3dwYV9CWnhtYklVTHV1b0pHWjRidURXRVEzNFRwNXNTZ2NKM2RocjE1MTRXU1cyT1RnWk8xWWdxczdjRk5YcFk5VUo2ZjdSdnRoWldDb0U1ZWNkbEVMZzg?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
