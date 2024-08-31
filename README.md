# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Trump proposes making government or insurance companies pay for IVF treatments**

You can read more about it [here](https://news.google.com/rss/articles/CBMihgFBVV95cUxQamJsc1JtSS1wNnBTTzV5YlZydUhxcHpjMVRvQTRMX1dGN2lHYlBqclNMRWVQMjU5M0RpdTVYLUpsVEtRV2VqSWNpa1k2eDBkMWJZdGpVbERLemtjZGplS3JaUzdhZDZNQTMwc0JoX3pxakotZ2E2Rm45UE9kUl9teWhYU0lpd9IBfEFVX3lxTFBPbmE1M1Q3Yzg3ZVFDSGhMREFjcXlCQk1zamMwWFBFWUF1SkpaSGYtUFFyZU5sdUpaaGJZZTIwNXhsYUlzdURRMEI2OTQtbWhiTUxjWW9XdmlHUjk5ajN3RUJIcm15UHRCNy1oWnE4MXdkTGNuUWFXRGR6TVA?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
