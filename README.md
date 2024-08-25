# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Backlash erupts over criticism of Tim Walz’s emotional son: ‘families are everything’**

You can read more about it [here](https://news.google.com/rss/articles/CBMiuwFBVV95cUxObFJpMXBUR1VZaXFOb0d3MUluYjNEaVRMWXplOHBoQkF4a092c1JURVNSem9HcV9rOTN0Sy1EQ2pjTDRmR2w3S3p1VVB1bk5nZGxIN1lFX21rZnhNXzhJeTl5QmZaZ3lDWGRvVHNLRDMwYnFkWnRkUnhZMU1jZ3F0UV9BWWJ1MU9aUU1IZFB0QlNwcDJkLWJWLU42NGVhN18wMEJqSWlkclF0bU5qVHdaWlczb1d2S3B1bkdr?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
