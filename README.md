# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**American activist shot dead during protest in West Bank, Palestinian officials say**

You can read more about it [here](https://news.google.com/rss/articles/CBMilwFBVV95cUxPdVUtNGtTUlY1V1BjUC1uWFhCd2JYcm41R0toTFZtWXV5NlgzclBIR2pXUC1NQTNnckNfM2RRT3E2MDBuQTAtQ3pVLWlHN1FKdk1NRG9qOVdDa3czZk1ucGhLX2oyZWpNYnY1ZG1iTUhDMmE4UE5CaE9IWlp1Q0RKem54ak9CVWpTQ1pxU1YtWVY1MGttTE5F0gGOAUFVX3lxTE5yWlNVSl93STE3TjJ0bDZfUVNLZFF4eHRHMnZBbmRiT19SYzg2QWRkMWY4bC10TGhXZ2tCLUVFeXB3TU92bVAwYkVIRWlaYU5TSl9nV0NfYVVRY1lFUUlVbGNCbUl2Snh2OV9qY1B0Nk1Hc1V4QWQyeFpuXzJTTy1vS1VJWTdGVnNNRGotRWc?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
