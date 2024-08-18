# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Former Rep. George Santos expected to plead guilty on charges related to campaign fraud**

You can read more about it [here](https://news.google.com/rss/articles/CBMiqgFBVV95cUxPSDFuMFRvOHpSSWtUVkpXeUZnWHFuZ2YtX1BkdDVYN0RMVjhBTXlwY3ZDb01fNFhSOGgyQmFRNVVIOG5FZmNfc3hEbXFaUnRteEFLVjdqZ1dHUjB2ZkRJR0VCWGI5V3NwN3dITDNLTWlydjVyOVFPa0lLdGZtOUJmX2ZJRVRDRXdGQmN5a292cnR6ZlRXaUJHSUk0RVFwY1A0WlBVcGUxMmtad9IBVkFVX3lxTE5XLTRfVGx4RGpSLTVOUWdIUUZuVUhOQkxiRGpHYTVKZkdpdExDRnVJVTJ6MWlGTWRsM3d3b0Y2d3NSamhyX19ZRGtWdEFaZWVLNTlrSGxR?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
