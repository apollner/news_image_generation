# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Teen sues Detroit judge who detained her after falling asleep during courtroom field trip**

You can read more about it [here](https://news.google.com/rss/articles/CBMivgFBVV95cUxQb3J2bEZPRlZsN0xjbEtLbFNFMHpyV01PUmc0dHFpU0RSM2VfbWN3Q25QZEtJdEh4Zl9LeHFZZWo5QkVfUVF4NTlybDFLNFp3MW1JZ1B1VWdtd0VudXh1dXp2ek1HRUV1V3N3MDBFNUtLM1RDeE4wUEllaXF2MDBqV1RVRmt1ckJBdmcwejNBTkFISVNubzJTNDFhUnF2Vmo3U0VBRDZKcTJvdEJRUFNIVnU2UTViM0dNUGRHQ1J3?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
