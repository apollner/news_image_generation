# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**A decade after Mike Brown’s death, his family still calls for justice as progress toward ending police killings remains slow**

You can read more about it [here](https://news.google.com/rss/articles/CBMiggFBVV95cUxQeU1odlF1X3hIRVBTZm1ta2xnalJub2k3Rm1RbzNHbTFBUy1yOUlpdnRMYU05UEFpam5iX3pYaXU4aGNKd2lnLTVJN0ZMNDA4am1OTGhYYi1fRUtFN0lSX3JRdE0wN2ZJN3FyVU02dzQwdnhvSzNqa1VNSmRLLUxfVnl30gF4QVVfeXFMTkZiRHVoUlozN19BRF9MZUNhZkpqY2ZOSmJoS0oxamZqSkNtbURYY0RxWTV6WVEwY1lUTmotTGtBYnM5Z1NEOGZIUklCbUZLdGg0RDdnNExrRlU0dDZscHg1TUJwX19sZnNLVC1JVTlBQnJyU3ZyRFVY?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
