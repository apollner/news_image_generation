# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**'We just had to go for it': Herriman's 'Spiff' Sedrick rallies USA to rugby 7s bronze**

You can read more about it [here](https://news.google.com/rss/articles/CBMiuwFBVV95cUxPVUo4bVl4V1hDaUVtbkNTVG55NlVrZDB1bmhmazNESERRTWdTbFN4R1dUU0RDVkF2Sy1maDdTQlNsdGI2M2ltRm9rd1Vfb1V0WnNIOXdIT1lSUXFDNEVaUktDOWw4dUJjWi1JaGZJVGVwaThxNUtfa2p2NG1XLVpTM2N4UUlxRE4wUDYwN29fY1BuaG90ZE1iSDZqZm9yQUdGcUllWjFUamF2bUpfV2xjN3FSTjZoS0QwNUtJ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
