# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**New Jersey lawmakers meet with security officials after weeks of unexplained drone sightings**

You can read more about it [here](https://news.google.com/rss/articles/CBMijgFBVV95cUxPMFRJUmc5STN1YmN6LUNUbUF4MVQxa3RVLVhrWEotSWxiUm1LMkotUzlHWFk2VnZIWEpKODk1TWhLUk0tREZYSlJnWFZZUm5HWDZOcGY0NTFXN1FYQnBwbDRta2poSWpYOW11RUNfZkNvaHhIOE8wQThsM0lXSlZUMDdfNk1CYWF6WHdESnN30gGEAUFVX3lxTE5SZV9RTXBFREJld3VsazlVeVZuWGhLS3BFRm1OUzF5TndVMHAxTE5fdUJTdUI1Q2ZZSUc0Zkl2T3lnc2pOTm1FcVVfZjdGeWIwRHpJSVBSVmNObUJuY0xSZnJrNmE0Ql9xYXhZMFktVUVfdFlOT205dmdRZUMzYzRNOU1uaA?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
