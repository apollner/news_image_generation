# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Donald Trump comes out in support of recreational-use marijuana in Florida**

You can read more about it [here](https://news.google.com/rss/articles/CBMioAFBVV95cUxObWlXRU5JTmFsbERTZzQ2aktpR0t4WVIwbFp0d2tfLWR4X05fNHNlZjZTTi1SREJvMXNuTFY2c3BSR0lZM3VGWUVUb2EtRTRjZWpPZHhkR2l6cjhkbEZXbVNJMjB1WGRKd0dpUl9hV1FQOW5BU3NCRDkyZ1h6b3dkR3AxYnZuNHpsU2tGY0Vtb0J6c0E0REZNYUxwTDNXdWVv?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
