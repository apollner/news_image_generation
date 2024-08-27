# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**FTC trial over Kroger-Albertsons merger kicks off, a heat wave comes to the Midwest and the U.S. Open begins**

You can read more about it [here](https://news.google.com/rss/articles/CBMi4AFBVV95cUxOcnlkaFRwN1NfcEpPQnA2LTdlakY3cDNwTlNfYnR6VXhSMUwxVHdPRktrelRoTnJBYVhaY3Q1QlUzSElOWjlndFFxZUpGRUxQS2RwOWs1OTYxbDVDQ0thLVpPQnVyMmEzUkJ0alZmZExvSW9QSGhXUFZxRmt2dEtSb0Z4VmZDMnR6djlOcU5fTmZmVlp6R2NIYmVkQ2Qyb05haWxkcUx3V1RJS3RPYXFEbjRRRl9WSGEwWklrandHXzNYNWZUWjEwakV4REFVOS1tRTUzWWx1dDNCYTdkTzFKSQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
