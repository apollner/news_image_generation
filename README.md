# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Reeves and Hunt's claims about shortfalls checked**

You can read more about it [here](https://news.google.com/rss/articles/CBMiWkFVX3lxTE9vRE1aTEhMZ0lPNmttNjRxeW5BR1dBa0lYRzZ5NlRIY0RFbWlVSVNZZjhwWTQ0LXJRRERyY1NOMFU2MDZVRERlX3dwaEE4QW5VYmV5UUdCYm1GUdIBX0FVX3lxTE9qYkxRTVp1NmZpMmRpRDR1aFBoOWlsU2xWamQyZ3lDa3dqSjFZNjlwelRsWVQza05JWVNhVU9rV2ZmV1BBMXd4Mm55c2lEN1QyRDhRTC1MY1FJWHRJYWkw?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
