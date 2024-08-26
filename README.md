# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**NFL Preseason Blitz: Bryce Young plays in the preseason and has a positive outing**

You can read more about it [here](https://news.google.com/rss/articles/CBMivAFBVV95cUxQV2hkdmVVWXV3dExGWXNVa1RBdVpvOU1EN3EydVE1bHMxYUxGb2t0Q21JN0JTaWJXdXpGU0I0dFpRWDdGbHJ5WVE3N2hzWnV0d2o4ejRJb0czc3dwUWxpUjYzSmF0TjYtLTh6OXBrd0pSUDZyc2hVQ0pKOVJBekNhandUdFZPbE1seU9MMlVzMnFhOUttZGRWOGFnbXdjT0dTeDFESDl6TUhvVU1KaENXTTFBN0tIa2pGc2pnNg?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
