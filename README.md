# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Asia-Pacific markets trade mixed as investors look toward Fed decision**

You can read more about it [here](https://news.google.com/rss/articles/CBMihgFBVV95cUxNZ05Wc1FmVUFOQWpVQ005a0Z4SjlNNUprZkV2WXExR0VBZUpyTDVnTzI4bUE0Q2ZnY0dXeW0tYTRkNWhlQkk2dlRQekx1cG9IbVhxb0t5UXY2U29OVG9UclZMTkI5WVczQ0xLcVE0ZktNdkRGRWplYV9ZRDR2OFpUeHE3QnhBZ9IBiwFBVV95cUxQMzhpVVZsSktucHBUUEpZOHFITmRlZDBMZkNOWWwxTXVqakxzRGZ3emtQQ2paOHg0Zk1LMnNrQlhtUFgzRkdWd3NkOG90d2M0X3RNaE85UmxHTWNQRFpfTFpRUVg4dDNWSXBSUDVBOTVDOEV1YUpLWFdtSG1vdVlJWjBQV1lyUWV6WWhV?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
