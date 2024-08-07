# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**NC governor issues state of emergency order ahead of Tropical Storm Debby's arrival**

You can read more about it [here](https://news.google.com/rss/articles/CBMi1gFBVV95cUxPR0tRam96R04zVVNzcXlyemVrQUZjX1dyRnhhLW9yZXNOMlZJM182ZFZLanZEWEtuN2V1UktDeUJEdEhsWU4xVlEtWnRqVnpQMWJoRmEwN3U1dDEwMmNTNlNpMVFoNVc4aS0zUGU4QjFFemRydWhqcGl3d1l2LXpFb0dxOTJqcU5kS0ZpaFhDVDNZd21yelgyNHMxOVBsRk53RGFrSFFDZUJnMDZsQ3RRRWVDSWNkellEMTQtNkZZWnk0ZlhZTHZuMDFiT1AxV05ERFJIdUNR?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
