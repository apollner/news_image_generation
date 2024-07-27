# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**GM reveals new Chevy Corvette with 1,000-plus horsepower and record top speed**

You can read more about it [here](https://news.google.com/rss/articles/CBMiekFVX3lxTE43UGh1cTgyY0lwcE1BU3J4OE02YjZGS0EtQ1BzWDF5MlFUSHpFVWU2WGR2VEFpMFBCOU9QOVVGUXI4VWdTaXQ5Rzk5UDVVNENqd1BvR3hucTVOUS1USERVZWJXOF9RS2VYRnhpUlBqQ1lBVGNoMTZBcmln0gF_QVVfeXFMTTJLM2djTnFGRVE0NEFXeDljd3h2MUN6Q2IxT0Y4a1M5SHpXeEYtMFB5NHd4cGw4ZmtnNWJBMEgxOTc5bEV1WDBvcXRWd1RHTnZHRW00TUFMYXg5cTRYLU5RMURobHdQRldqVTJtT3ZzYVRwcmxjMndOVXB3Ymc2QQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
