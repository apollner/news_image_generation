# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Falcons trade QB Taylor Heinicke to the Chargers**

You can read more about it [here](https://news.google.com/rss/articles/CBMirwFBVV95cUxNeWpzVmVrSUlIM1licHRLQnh0MEZHb05MV29KUzI5d3h6eW9tZUN3dGlBaHQzcWxzYnBfcXJ4R0ZvWEVhN25feUN5Vk9xOUFUWWZFazl5Zk55blVfZzNQOGZBZ25CenhqakgtZmhGdERBYkJwdFE1ZXVCbGlhTGZjRmpDNnBpaG1UWHI0VktXVW96WTFYLUhEWEQzZzBjaXF3MzA4Wl9vc19nc1FEel9R?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
