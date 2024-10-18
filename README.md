# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Italy surrogacy ban: Couples banned from travelling abroad to seek surrogate**

You can read more about it [here](https://news.google.com/rss/articles/CBMiWkFVX3lxTE9UR0hIdUJ2XzFILW1IOGhObk8xTUlJQ255d1BlTVY3Vm9XM3QwdHdmcEJ0RHRleGFYY3BNZlVwVGJndGk3OUR2UG80TnBUSlZiYjRJaDBZQUpGQdIBX0FVX3lxTFBCWHFLbEtjd0VPUTlaVmpaT2VGMGthaHZqSVpZeW1xcHBScllpQnloSDYzRnJFNFNFLU5RamV6QmdYdnRmM2l1SzRhZnJzYkVseFlLOGpHX0lVUWwxX0ZF?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
