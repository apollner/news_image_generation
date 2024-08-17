# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Dinosaur-killing asteroid was likely a giant mudball, study says**

You can read more about it [here](https://news.google.com/rss/articles/CBMimwFBVV95cUxPMWVuX3NQSHRGM3lOUEY5cUxQZXBQcFg0WHJWNi1CMXMzT1dWWXRlRmZpWFZ1X2dmRVpmZGF0T2tUR1dNRmtSSXMtb1h3T3lxSnNEdU1KYTd5aTVmcFVmNndudnY4SUt0SUI5WUthM3ZJcm9mSEJMRllYRmRUemNrRG1xZHlod1pCVUZwMkZ0Qi1UZnE0dy1CWFRRONIBkgFBVV95cUxQRXR5VjJFUnMtSE1ZVUdMdmZtM0JrZVlXWnNHSWdUcXAzRk5fSmhLREpwSWVfdUdUdktHc2xzYWFEakdhd1NyQnpSQncta0RZbGdfVkZNd3NJN3NRSjJsUl9xLXZtYUYxaFhSeHpmSl9NV2dubTNiamtadmloVEhSY3p4dVFDM3d0WnB6cHdFMzlRUQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
