# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**How Kate Middleton’s Ring Is a Nod to Early Years of Prince William Romance**

You can read more about it [here](https://news.google.com/rss/articles/CBMirAFBVV95cUxNeG9idGVZalgxbkcxbjVMNGVBS1BtU2RrNHdRZlJNMkN6U3ZGV2duOUFxd1dXeWw0aHBYc2pZMlZJcUNnV0JTbU1zZW1LYWIwaG05b0htczZ4ckpId2NsSEc0NlBoT0NmVEdRZGdFd0pkaE91Rm9BTkFWV1hFMVRucnoxejVpMVExYTdlc0ZQRGxETWxHSUx6YVdhcnRNV0J5WDY4NV9GNHI1RUli?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
