# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Hundreds of proposals in Project 2025 match Trump's policies**

You can read more about it [here](https://news.google.com/rss/articles/CBMidkFVX3lxTFBCUzZIT2hnMm5xem41OE4zWlc5bWRDSVpocE01VUNBaHVONFJGR2JTc3RTSlN0YWtOaXFJdV9yendRbF9zOENEcHBqRUFvU2FscEl6SWhsRjhVZ3J6amlaRFgyMk1wUzRmdjhEeVlmcENOTmtmWkHSAXtBVV95cUxNWmNsbm1RVWpMWUpiN2s1M3JZcEVGeHJiTTdyT1RBTTg0eFJJVjdxVi16VkF5Nl9RQUMzNmNvdDNLdU5qdVc5Tjc1SjgtWEN5RWp4MjRwX1lKY3plUDd0MFJrRGZCbFY5OXE3VW5SbnhTMzVzUW40a3FmbG8?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
