# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**FDA expected to approve new COVID booster: What to know**

You can read more about it [here](https://news.google.com/rss/articles/CBMimwFBVV95cUxNZEtNWVl4R1RIQWNtQkEySGpBZDg3OXg1c0d5OEs4Z2xLV3N3UUotRmhvcWNwUUVOMno4akNPM2RGdEFCeFA3UmxnWnlzaFdKYUlSRUVWR0RXeGJ5VUlYeXpnVC1XdzlwVzZlZ2RfR0NKOXlPVmhlY2RFenhSSkNTUWF1am4tOHNWeFdEVDFkRjE4LWNIb21maEJXUdIBZEFVX3lxTFB5cGxCSnBDWWgtR3pJWXdKU3NKQlB3ek16cENSRnJ2OURUY1lzTlhHX2NYTjRvOEhvb0trSnIzay01OWo0aDlKX1hacnlBdFBtQ0VrVVJMbVBxV0tvLWt1d2lLQ0Q?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
