# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Captain of sunken Lynch family yacht put under investigation**

You can read more about it [here](https://news.google.com/rss/articles/CBMiwgFBVV95cUxNMEhNOV9mSUR4TFg1QWRIUkN1QlNiWG51VV9DSW94ZG8xVHBFVGx0RnowLXM4RmllV0RiU0lWa2Vhc1hSRGpURGFsVENNZHhmTjRWUkp6ZDgzU1k5ckwyNjdTelNqbXNIS1UxR09UcWs5b01sMV9sNU44YWQ4OUtUNUZLa2RQZVFkbThFY01wRUdvaTYxeVpZWWczOFFqNzEwamZzMnVxdHRKblJWMVZ5NmF5UWpYQ09lTTNYdEY2SlZYQQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
