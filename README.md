# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Lake County Sheriff: 1 deputy dead, 2 deputies injured in Eustis shooting; Two suspects also killed**

You can read more about it [here](https://news.google.com/rss/articles/CBMiigFBVV95cUxQeEVlLXc2T1FBZDJBLWdEeDI4bEdaV1B3dHo1N0pfOGVYeXk2aEI1RExULUpMVVRKU2FJRlZXSVBkM0k3VkZ2RjB1YWdubUM5b1V3NTVGODY1ay1IV29iSmVOc1c2dWZXeFcwcGd5V2M5c0NxN1FCZ01GMTZXWkJmV1M3bDdBUDA0c3c?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
