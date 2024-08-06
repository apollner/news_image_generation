# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Bangladeshi PM Sheikh Hasina resigns as widening unrest sees protesters storm her official residence**

You can read more about it [here](https://news.google.com/rss/articles/CBMirAFBVV95cUxOOXFuS0FVMjMyc3VOdkFIaG9PSjA3U2JhbHBQTFQ3MHp1Z2hxblhubmJ6bjBnd05RWlI4YVBHM0tmRndfRG4tQWZIWFM4MXBBUkwwY3JhR2dIVlNYYndqODJTTkJaYUhOQ1lYRkwyczRSN1djTkpnVGRLdzBpZ0RyZ0x5eUMzbFdjR3RtcVRCTlJqeFNLRHFocEwzZHJXX3g3Z2N4d1IxdEg1blZh?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
