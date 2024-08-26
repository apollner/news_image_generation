# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Florida State's flop and Georgia Tech's big win lead college football Week 0 winners and losers**

You can read more about it [here](https://news.google.com/rss/articles/CBMiqgFBVV95cUxQX3kwSGl3cE9veGJkUXpyRTRqbVhRZUJFX2VySUdRUms2UWUwaF9fXzVOQ3VrWk9KWHlKVUIwTjJRWkVLWGhwNDNlMXR0SS1sSXMxQUNOMGcwcTJuQjd1M3lsNlJvSGU2M2kxanpJa01CYmhFc2hMWXF1VHFOSW9yeWgzWC1TQ3JWY0kwaEZ0R0lhNjR5X2Z2OUZZd2l4alFFNm5BWlluQTJZZw?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
