# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**NFL Rookie Rankings: Top Performers from 2024 Preseason Week 1**

You can read more about it [here](https://news.google.com/rss/articles/CBMirwFBVV95cUxQR0xFbGVKNWNRUk5Zbm82TkJIZHBQcDl6bkNhb1NUNWZ5dWlQWHpPTkx1R0dCVjB0WGFCRkZkNjlMbFBqSDJvMVJkNGJaUUJFd1BJZ0llczlib3V5SjZtSU9RLWtzdTVIak5pMGtEbE5MSTFDVk5CdGpiUnhMcjJ4aGVRQ3lYamY3QVF6WmpkMG92WVhFdHBzZGd3eXFqUmdkVkFsZDVrUEFrTkRONGZz0gG_AUFVX3lxTFBfVjI2TDN5VXVsNU8tZHZPT0YtR05ZcGVJLWcxRDRUeGpGWTNIZ3M0UjJlTnhZU1hsSWpjczdiT3QtN0hQRTJqMnM1VjVzcGtJYVp2U3lQSDQxZE9vbm90RkYwbjllbkJqWXoxVkV6MTZubVFhc01ENXdYNEh4RFRRSUtLNk1Mb1d3UExsMlhjY0N5ZkktR3pJcXk2UzZNMmpnNUloYjktOGJyLUlyck5wcXRBN0w2Z1FYSXVMTDZr?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
