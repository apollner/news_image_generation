# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**A 911 caller said a camper was killed by a bear. Police say it was murder.**

You can read more about it [here](https://news.google.com/rss/articles/CBMijgFBVV95cUxNLVlacWFfMjdkblhFekRvckdJWVl1YXhvV3p0bzN2Z0tHV0lpMU9fcWRKNzgtTVluZmhMeWc5VkR1enFMdE1OaVJOZ08yRFB6TzA2UUU1MGdSdV9ZdzJ1d1BKVlFYSUUtTUpWOE5XaVFrTUp4TWx5TGdIVWhiZ0hhVlRsY082YjRnTWVPWlZ3?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
