# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**The Bachelor Alum Ben Higgins' Wife Jessica Clarke Is Pregnant With Their First Baby - E! Online**

You can read more about it [here](https://news.google.com/rss/articles/CBMivAFBVV95cUxPZ1JBU0E1Y252QjlJSy1KT1podk90b2lVeHA5Z1FFbFE2Zi1BVUZwVm9Uc0p3RE1WekU2d0poU1p6TjRobEJRRnQ3S2R5cDFxaHEtbmw4b2NVMUJnODRXX3ZwSmpQRk1qUkpldERtcjZRYXpsdzljUVlBSEcweWh5V0VwNm5qLXdYa2owTFNvdUJyc1RzaXR6OWhxWnA0cmNmOHZrSzhlblFHaktvZjlQcWY3c3RFcndiaE9GMw?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
