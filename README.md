# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**FDA Approves and Authorizes Updated mRNA COVID-19 Vaccines to Better Protect Against Currently Circulating Variants**

You can read more about it [here](https://news.google.com/rss/articles/CBMi2wFBVV95cUxNdGV4V1pWNXh1SmdkS2JpSUNsOTNQMXhxS2MwSl9wYnpWQ19sYVdmbHNraC0zQmlVdVVJVmVGT1YyN3JwNURzYjFoTldtWFc4M214X2xQM0Ffb0N6NkJKQ0NDX2hxc2FXN3JJLTJMTXVWb0pBMVlBaVI1YzRmaTdvWGF2SjA1Y0t3QU1MYlpHc3JNa1A3bk96RDBZZm15aXVrakxBclV5alRRXzU2R2lOc0pPT3B4eUdBbnRhZGIyaDVwamtFRVB5M3VtLVJUMm1zYVlpTDBFWGRBbEk?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
