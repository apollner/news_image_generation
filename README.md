# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Judge in Trump's election interference case grants extension sought by special counsel**

You can read more about it [here](https://news.google.com/rss/articles/CBMirAFBVV95cUxQc0NKUkcyMHNuQldzZ3V3RVRsb1U2X3l2Y0lZcjlhUDFMSHVRQkdxdG5zQWloZVFMNlRnUjF5UXlwUHAtX2otZVM5bnNKODhIZzkxUjloYzRyVzRiNkFGZVN0RGJpTENiei1UQl8zdm8tdGNieF92QUF2aDRNV0ZBdlptbXI5NXltVzdrV2dVYkZNcWdueDYtYk5ZM2dlTDN6Q0pvVGRHX3ZHOXc20gGyAUFVX3lxTE5WN3VzeTZwbGdVMmxSTmpHVk1rYnk5UTdCVm12ME5MdUJBMzlMNDdKcDRvMzhpOXNfdUVPV004aTdJM0FrNjc3cHZXbERHUk81QXQzT19yWFExcGhjY2MyRi1NQnhUa3o1cmNXNzJSNmoyTE51UDZLVHVpU2JHV0x6TXRlYjU2VjZwOGNLZWotN25wUnBDYWVvOElOVE5ENjg1cHpGRGxjU0hOa0hLZnhsTXc?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
