# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Jamie Dimon says he still sees a recession on the horizon**

You can read more about it [here](https://news.google.com/rss/articles/CBMigwFBVV95cUxONi00WUktSFUzZG9WalFReDQzaGg2TjZHbzJhRkY3dFBFRHByb0l5S3B0OGQ4cEFJT0ZHUTZRdy1nVTlsTldwVW9HS21KcWI5c1JJMUwteGdhZ19wdUV5ZHIxMGVOV3E4TUFEVkNEQ092NENPbjhpRzh4NHgyeFVnZG5kWdIBiAFBVV95cUxPeUhFODl5NDFHV2NDUDFXY0lMR2ZTc251UTlmSjFtaEtFQ2pqSnVNV3VJYmF3WUhRRXMzR2NHcW1FZVRjeXBoWXlCUkJQbFdCZWZkcWNqNzVYclJLOW90cTZVZl9hai1OS1VQTGFKSzdMRVBzZkNIazdEZExNVG1oRU1VQ0JrU19a?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
