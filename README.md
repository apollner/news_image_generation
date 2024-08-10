# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Debby threatens nearly the entire eastern seaboard with flooding and tornadoes**

You can read more about it [here](https://news.google.com/rss/articles/CBMilgFBVV95cUxOb3I3SWpUN1Z0dFNjYUZhNS1xNlAtdXlJeWdLZnRJQ2REU09rblZjZWRCMTJfcWUzUG5PT1NqWjlITDRCQ19iOWVVdEthcU1Kcng1dENkdHpmaTltMU9WWmJVRWh4cFh3SzA3bEE4NVE2NXU4OElBZUlqeVJNcl9tazd5YnpzeFpobEZhVjBIN1NJSXFnOVHSAYwBQVVfeXFMTUlRZWJyWFNiNF9CZWMtUFdRZHdtY09hZzQ5bUVHclRfUDhOd2g2TXY5eXVRSklfNllJVGFkQW03UmF6b0tCNi05TXp2aFhLOV9OcDVUc1JiOVo2blV4bGJoTXZJRy10S29Zdzc4YUVhVzFMNmpiWERXVzU5dkZ1RHpzY1l5c051ZmNUM1o?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
