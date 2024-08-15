# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Yankees’ Jazz Chisholm Jr. has UCL injury, placed on 10-day IL - The Athletic**

You can read more about it [here](https://news.google.com/rss/articles/CBMikgFBVV95cUxOaVd2VTl5eXZCNXEwZUx1SWVseGNTcjYzY2I0bV9QV0pwdGt5aXlDUWR1Nmp1LXpUczRrRUFjUGFRRmRYVGwxdU4zSXZwMjluSjNNYWp5cEZRVmhFNDg4aTJLVWltdWV1c3pBYVpraFg5UjY5cDFLUDJtcE9Va3k5ekE1Nll2emVCUFRTUkI4QXljQQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
