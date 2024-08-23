# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Will the Bo Nix choice work in Denver? How the Broncos, Sean Payton came to their starting QB decision**

You can read more about it [here](https://news.google.com/rss/articles/CBMirAFBVV95cUxNOWxjV2VYOFNFZGlsMnIyMW5JS2hHenNPRXJSMHlWQTRxYTBkUW5US3NOYVMxU2tGQ3hyUllOSklOOUhrRy1wZVZVVUNRV2gyWlBfWm1ZMWpJUnNCRVFZTDQ4Z0V2RmdBQWZLZlpjdTF3X3EzLUU2ajNWeUpPc2FmVl9HaEQ2VHVQaUJMTDNjZVNDVm96eDRmcjVwMW5fUkFmVl9uZVFqcDdqOGw0?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
