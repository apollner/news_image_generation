# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Hands-On With Amazon's New 2024 Kindles, Including a New Color Kindle**

You can read more about it [here](https://news.google.com/rss/articles/CBMipAFBVV95cUxPN0I2TnVMWDdZdm1ESFkybVBTeHBHSWQ3VENWNy0zS29xODJ5aEhlLTB4MktBRUduTWtOZlA1TnF6UlEyTnRaWnpIYnVycmJDd294Z1lBb1YzX2VZeVpiUVRVcDlvX29NYjAtUE15cU81N3ltXzY2R2JneEl2VWV6Q2ZrbmVuTWtxNTF5ZmdxR2o4QVo2dEp0bnMxWFVFTS0zOEtXeg?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
