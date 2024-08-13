# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Jerry Jones clarified why he doesn’t feel urgency to sign Cowboys WR CeeDee Lamb. But how clear is it?**

You can read more about it [here](https://news.google.com/rss/articles/CBMi1gFBVV95cUxQQ0drdXc1Q1RxYmZ1ZW4yVlNhbFM5amJtcWpwRnVUUVVhWExXZmVWekY0VlNERElKWUhJRVd5Um9hN1JrVy1WM1RoSmZJOFN0VGtjSGxYWDFUMnRTWU9kYlJ5TklUZmM2djRHeUZOenNENzdqSzM3MVFTdUdtcHlUcmRwS3ltNkUxQlItbEg2bm9qTXdiVlNTZDFhSWJkNzNkX05vQ2Z3MFhYd2twVjR1VDd6dmJUWTkzRjZYUWtJTy1nUUxJYVRoWWV2YlpiVW1GSzR2OUpB?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
