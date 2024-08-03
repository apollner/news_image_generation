# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Study finds major Earth systems likely on track to collapse: 5 things to know**

You can read more about it [here](https://news.google.com/rss/articles/CBMipgFBVV95cUxPYjlKVGZ0UGtmMUlaazc3SzdVQWFLbko4WmhUQXo3OHJsZ0NtV21LSXdZTHUyTjlELWIzX00tUkZIZWRxN0xSQ0ljTUZfclpQdzdzQmNkdExxQndrQWNKWVd5SlhlLW1nQmZLMkZCZ252YUFkVEJFTGFDXzRJZ2FvTUN3dVZNeWpseXZjS3JoWkIzNUczZEpqdWNaWEV5UVVJeDM5VEVn0gGrAUFVX3lxTE5TM1RBcnRveHNDblotbGx2WGZSZGVpQmhJYVVhR0N1dHcwWmtUN19zNjNsbExVMndUSnlLQlJzNHZRNUhqVHpVMHBGWkpRSEl0YUJxTmc1QW9NaTF0MnBLNm9HVTZ3Sk5JZm02Q3ViTFdoUFlReVJSdnpIREtRSVZYTWdXSUhYLVV3NEc3d2tjT0l5NXEwRUJvMzktVmtIcWM2bjBmNVVhX1F2cw?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
