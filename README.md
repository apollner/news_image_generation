# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**The life of two Boeing Starliner astronauts stuck indefinitely in space**

You can read more about it [here](https://news.google.com/rss/articles/CBMiqAFBVV95cUxQZ3JJUk8zUXRDekpzTDdGa1NxRW9yMkloak02ZG5QYVg5OUdXWHU1ZFVqV3lkMVU3Nk1yV0NxNmJlb3IzRk1ZRDZEUmQ1QVdwTG1FdnI3ajlIRUx6NFR2RkdnOWs5U2g1N3c0YzUtS09ybHA1OWE3dGhobzRMZTlOX0pnRWNrZXl4TThSWVg0c2tNUGVsWlVDcmZqYS0tMmtxVHI5a002Njk?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
