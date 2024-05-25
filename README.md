# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**3 US service members treated for injuries related to pier off Gaza: CENTCOM**

You can read more about it [here](https://news.google.com/rss/articles/CBMib2h0dHBzOi8vYWJjbmV3cy5nby5jb20vSW50ZXJuYXRpb25hbC8zLXVzLXNlcnZpY2UtbWVtYmVycy10cmVhdGVkLWluanVyaWVzLXJlbGF0ZWQtcGllci1nYXphL3N0b3J5P2lkPTExMDUxOTU3NNIBc2h0dHBzOi8vYWJjbmV3cy5nby5jb20vYW1wL0ludGVybmF0aW9uYWwvMy11cy1zZXJ2aWNlLW1lbWJlcnMtdHJlYXRlZC1pbmp1cmllcy1yZWxhdGVkLXBpZXItZ2F6YS9zdG9yeT9pZD0xMTA1MTk1NzQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
