# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Why is Team USA so bad at 3x3 basketball? How 2024 Olympics rosters were built after losses by men and women**

You can read more about it [here](https://news.google.com/rss/articles/CBMi4gFBVV95cUxQb19xMEt5VmNLR0FQaEZBM190d0d6QVJxRHpEblFlTElCRUJCc2xxUXJWLXVxZlc4Zm52NU9xbXJGUmJWajZxa2JCZzFudDNyVWNVQTF1X0M1VnNpMnRzSy1QcG83UVRUdms3WFhCLTV4Ynl2M01uS1JnWmNFSWw2ZTdoYmpPRkpacUxJWWEzdlZRNDAzZ0lEZ3AzdHlhQktHWTFxZVNPZ29aS2VYdEdlQkFFRVd4cmxUamRaWXFuWnBSTVJBMHBJdXF3VnhveFhqMGgzbnY2aGY1MHViUWpVWGtR0gHnAUFVX3lxTFBIZVB0SGtKUjRGNGwxRkRFM051a0t2STBNRHVIeklkVVFUTFloa1Npd2Z0bGctbEZnd1diM0x0YVVjZ2NvVU1VMFBJOFFHT3pERnRpbUpHV3dkRGhxSlkweG1pZXhJaW1xbjZWUnExZVoyVkUtOGVxNF9OclRwTFFpcmdlQlB2ejlQYXRCUDlUNFFBRzhxeEIyZlBvbnM5MEQyTmpIbEtrQk5lUmV2NG9RM0VENC1qVTBxVnF6STFabTdSNUFGa2dLX2NqVDhuWnBQZzdPQ2xHWC1GTmVmMDdPcllOUnVQbw?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
