# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**12 highlights from the 2024 Democratic National Convention**

You can read more about it [here](https://news.google.com/rss/articles/CBMiXkFVX3lxTE5wd05pRUs3cDBkRVdZSDJzR19NMjBOVmF0cXBBUklxYUlhZUxlX3NLU3VIOXJ5NVMwY1RqYmZHRV9Zd1FDRW1yS0hURFROeDNpQW5tdEtmMVoxTl9ubnfSAWNBVV95cUxPeUFkQjF1MzBhenRSbEdYTjNlVFhldnplVnc0RnlodGdaQ2RpVUN5UVlIbWFibGRpaVdHN0phSUhzSzN0cmxQNTdGTEJQZUd4cW55alllY3BZOHZSb0hJeEI2eGc?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
