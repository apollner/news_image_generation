# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Apple Loop: iPhone 16 Pro Design Leaks, Goodbye Apple ID, Confusion Over iPhone 16 Launch Date**

You can read more about it [here](https://news.google.com/rss/articles/CBMiyAFBVV95cUxOVlhQdTIwWFBwQ1VvNHlaaXJ0ZG52WUY5ZGpNczBGamh5U1BuMVc1MHBJRW1Ec0ZlUUpPQml6YVJWY19KcjFvRWNyRGRzTlFrUXhMSHBLTUVGbVItTGpObVM3RmUwYjRQRUg4NHNuTHpwV2dPdnJNMW9fdjgzY0pvNGR3SlB5RlBrSTBUQjRsNFNLRUdSNWV2UUVqaE9zd2c2dkhBdk10d1hFOHZXeUlFcEVUZG9wOGlTN05XQnVaUTYzZ0lxMlFPVQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
