# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**New fencing goes up outside DNC a day after pro-Palestinian protesters breach outer barrier**

You can read more about it [here](https://news.google.com/rss/articles/CBMieEFVX3lxTFBEdXJobi1zRjVNdFVhbUx3S2ZmUG1YUEJRSkNqZm93N1pxTjR3TWhDMV9VeUs5VFFXS1RDejBEak5WVC1zNjRacEptV0hZVWF4dzFQQ3pROWEyOTBLQmRjZkJLU3cwck9UOWdQd01sd1M2TUJnNGZQaNIBb0FVX3lxTE9jTTRxUmRPVlh0VGtDX1ZldEp6aFRJWC12eUVUeGFfc2dFaVNVMlR5Q1otOG50Wno5VzdTMzJ1YUpXMUk2NE5nOXQ4T2pMSnFxN2tPZ0JlcVRmY0gyRTFLV0h2Q2wtb1RlN3kxU3lNRQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
