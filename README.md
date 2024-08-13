# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**How Boeing's Starliner test flight got here and what NASA might do to bring astronauts home**

You can read more about it [here](https://news.google.com/rss/articles/CBMigAJBVV95cUxPSTFFWUZuUVZ0OUdkZlBoVkhwZWRuaHVHZC14bjhEM1QzSXM4eGdjSk5JdGxqdWhSOE5wQTI1WEdEbFU3LWwwTEZDc0wwLWlSLXQ2SnNHUkZMN1J5U29rbm5YYmVpSXJQX21QWmEwamhCSVI1SDkxUWxCX2c3b3B4THFpTzZOdXhSOThjaG9IUXBhc1RRTnBzM0RRME5GQkRsSTRRMkhoczJDWTROelgxNl9xSFluLXZLVGVfSGJtMm41V19aYXBTRnp6NG9paGpudG5KcGFKb1JOUDQtV3d2LVRxQXMtSWUxa0IxSzY1WEUyOE5FbFNSeW50VExPOS15?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
