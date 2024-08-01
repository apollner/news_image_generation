# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Kevin Costner’s ‘Horizon 2’ Set for Venice Film Festival World Premiere After Pulled U.S. Release**

You can read more about it [here](https://news.google.com/rss/articles/CBMiqAFBVV95cUxPelNIUHlON0tDU2ROMWtLQVNSQ1A4UzVWalZfREhILWRNQ3FlazA5bUJ2YlN5RjUzZzFkOXAtMHk3eEI1ZVRBczBFT2xIMjA3RUIzZU1ZaGd1RG5yM0JrenlaMHhXbW5Zd1M3SUhpekJRRXZnVjc3alhneG9BamJtLW9TMngxUjBjMFIzZGdlUktzQk55UFRGNHRBT1NJUDl6RHZjMDJBUWHSAa4BQVVfeXFMUFZ4TzJibXI5VnNxZFVkN25xcFdmbGgyamR0U1p4LVNuaFBISDZhZ0RGYWZLTmpra2VIUFVkNkN2aTBtQmV5SFJxZ3BWVE1FZGF4R1l2WFkxQnlxSDY0cGZYV096MDNBeTJmZlFPaHFaNmFRUXFoMzJzZXZGWFJKMllOZUZmeHM1SXNoVDh6ODdUSUVNNGJHRXRiQ1JnMG9aeEx2Vl9sYTNWSEVMd3FR?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
