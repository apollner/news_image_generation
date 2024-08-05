# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Katie Ledecky swims into history with gold medal in 800 freestyle at Paris Olympics**

You can read more about it [here](https://news.google.com/rss/articles/CBMiiwFBVV95cUxNenNSd1JGZFRtQkpPWkk3aFhCQ1czaS1HS1pJQTlGYWFpaXF0M19zX2E0YXlmVGU5T2ZEejV1S19WOXFPdWRTOWhIajlMNDZ0WWxtS3cyczMzdXRBdFFETVpCX2xjZWxGLUdYQmYzcGdQQTkycG1Ec3BGVWtORUVFcWlYNFpsM3BNVktZ0gGQAUFVX3lxTE43cG5DRGpDVU1HN1JQQjZEa2dTYmx2RHp0Q3NGZ0lUNjBQZmZZcDRjSGZRWVBaYVM2aHdHOEQtVWFmOUZ6UlVSQXpKSkk2M2xNQkIteGNQWDRRUzNTTnprLVFMRXFTVURTTVlkUjhjcV9OQkJLZmdTRUpaZFNKODJNYkI0aXlzc3A0WURYRDR2Zg?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
