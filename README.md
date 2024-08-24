# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Former Tennessee officer accused in Tyre Nichols' death to change plea ahead of trial**

You can read more about it [here](https://news.google.com/rss/articles/CBMipwFBVV95cUxNYXh5N2lSeHFKT2o0T1h1dDFRSE95YktRejVYN2pha2VBODhrLTczZlgwYndoSk51clZlN25MbTk4OHdza1BQb3ZYaEZMR3pQSXVZajAtdGh2TWdtVUVjTjlYd1RGQlBERk1kMzVnT2VfcUNqMC1GdDRJdUNCSzRSVjd0UWpDSGVVWW1DRXE3TDVzeEhTYy1VUTFDM0ZCZXMwdndpa1BDMNIBrAFBVV95cUxOQ2JrUHU0c3ozYk1aa0JlblNlOEJEZjkxMGg1QjVCSTdYa3k5ZXdmdm51TXFOcV9FQ2pNS3BnZEFvTVZSekxENnRvS0VCVHZ6akp0UkpwdTREYndPeG9oYjlWVnBTWkZfXzFIQloteU5SSThKeWotZXBrd1ZZc05ZVl9ieXZxOHFVd0ZDUTBiNlVxSGJyWFZKUzB5c0JhbEpBYzU0aTVnQUtjcUF2?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
