# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**As Matthew Perry’s PA prepares for prison, Hollywood assistants spill all about what they have to do for their bosses**

You can read more about it [here](https://news.google.com/rss/articles/CBMioAFBVV95cUxObjZlM0I4RTlvUFlpUnF1RkVHN3JpNDdmczRrR3hTVkotMFV0eXVORmhaNnlFZmxmZ0dRUVNONmZkdXRhaVc2QUNzcHZ2N04yTzgwNjZ0aGdMeElpZnRLdkdmb3RwRTMyUjFUaFVEYVYyTU9IRkppSmx1dWE3bHYtV1JNNFhqSkZaVjhVZTJIYzJFekdKX1dOd3dRemMzdHVH?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
