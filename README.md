# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Trump signals support for changing Florida heartbeat bill: ‘need more time’**

You can read more about it [here](https://news.google.com/rss/articles/CBMiowFBVV95cUxOZUJZLTdIekUxTnE3Zk1EYXUxNG5xblNxZnlYVWNVbERrV256VDlBSW04eTBZcnU2SWtXdDE2bS1rVVJZY3pvSTAyOHVmUkxDektaMVNuM2lkMGNRem5VNFJ6VkIyaFlVVVhNR24yem9lS3BGbk1PWkdFZG1Dekw2ZGlkS2x5TnUzUU5LZWVnLW1EMnJ2cjlra0IyUHVPMWNhTFFj0gGoAUFVX3lxTFBTUndKTTc5LWhyOXRiVFJyNjNVTjdXZjlRRFd2QVJvQWlwWUhNVXdlc3ZjMnIzUTIyTGlJNy11eF9YdEkzR0NRc196bnhwcWREZHZfYUl1VldLNXlpdTBERHZ4Ykl4VHhOWHh2dTljN0RXSC0xSkl1TXRpa3RpZy1SYkFRNFg3TzNHcFpJc0tZUlI1QTRtM2J2akNSMkdBSjkzd3hNLXhSOQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
