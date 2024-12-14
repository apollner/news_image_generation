# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Anker's 3-in-1 power bank drops to just $20, plus the rest of this week's best tech deals**

You can read more about it [here](https://news.google.com/rss/articles/CBMiywFBVV95cUxPMlk2MUNMc3h0VFJTLVktaEVZQmVTNHRySTRoVDQwRnByaEI0RlJmczllSmFmM0FfdGxDdHJ4YTFkaWMxZlROYmk2WVl2RkE2NWdkMnNwckxXN3pCenlid1l5cm51czZVdGEwOVRORk1wZTlrNHNBV3ZlekQ3c2lSQXF4RTJLNVdDa0s0VWRNS2QwejJmWWpqaHJ0S2w2ZVFxZlNpYjFpMmZrTGNGdzNPWk0xUDFhWkFka01Zdl9iZGFhTDFaZm81LUtrZw?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
