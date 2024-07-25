# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**New wave of North Korean trash balloons hits U.S. Army base and Seoul presidential compound**

You can read more about it [here](https://news.google.com/rss/articles/CBMiowFBVV95cUxQMzV5bXdrRC13MEdYb0lGcVd0SXJmRXJydTM0dS1mYXNfckRaR182OEZudUdYTXlNajBoRkJWYzJfYWplQ2NCRWZhQjJPQlhpNkVaZHJFSURmQ3Q2YlZDVE1oZzJ0VGRqY0pFNHpRNVRnS1lyQlJxVTNvcFRXTHlNYnJaVzR3d09pUGlDT2JBNG1IeU41MVYxTDFPbFNpRHRhZ09Z0gGoAUFVX3lxTFBXbVo4WGV4aDJlUEYxNUVtZk9VVTFCVXZJT1BlczZKcERreElkZkdnXzUyeWRmUkQydG1uUlRzLWNvVWY5VG1LQ1FlNXBDT0NVa3FmQlBVS1JpdUF2X0FoSV96eXRlRklQRFpXanRrdUxmSTd0dnZweHFvNGRJZXVXbzJsWHdsTldzdEhGV21hdHdhSkFGVHQ2VXhWeGVCWGdCR1lVVC10Xw?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
