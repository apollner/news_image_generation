# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Algeria boxer Imane Khelif wins first Olympic fight when opponent Angela Carini quits**

You can read more about it [here](https://news.google.com/rss/articles/CBMioAFBVV95cUxQT1FYMVF4THExZ0I1YXl4SG52VXNfd1hDaDVFSzdqc1hEZ25SUW9yR2k2RmFRWUJxRnhtQkVRQzJKRkYzS2hBVU5uNUdxUGpmRmtjSzZaLTNFa19maUVXaXVHbnBjX2RRd2hwUkQwcW5wb1dCWGNpdV9lQWdjLXBFNHJzT1Nkd3JWNEd6NUhzSkx0UGEzRVBzSFNfRmlGdzdf0gGmAUFVX3lxTE4zaWIzRGo4M1czYWV0NlBGMk1Ec0NhdTZESjhtUFc3QmpOTkh1RXRPZDg1U1JEdmoxUjNDVF9jaG9nUUpFeVUydy1IbWNjWEdzc2dxSjJkYW14VldCZjM0bktGUVVGQVRsaUoxVnMxRWdZWFV4UkYxdVhodU1PSW9KRGdLWkF6bFNYd1BfN3Y2OU43Y3dkTTlyWHlfSWpPX1d4MXNvS2c?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
