# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**One Direction’s Liam Payne mourned by Hollywood after death at 31: ‘Absolutely heartbreaking’**

You can read more about it [here](https://news.google.com/rss/articles/CBMivgFBVV95cUxPdnVqYV8xVmhLSVpLY2E4MTBnRTdIdlVaOHVxTFdyOXc5dUM3UkttOWI4OEd0WUV4TkZTZ29EbjM0LUNkR2RQUGlyQWZ5ZDg2LWdfNGFteFZLa0h2MnFobEJJcENfVzlCVU5LWnJRZURJQ2UteFdsczdKMjBhcm1ZREh1TlNERWtneEl0S25kZTNuRE9xNUR5cEZDZjVZSktfS0pDZnVTbHAxV1hiOWlUZFEtMG91UjM4QjAzX3Nn0gHDAUFVX3lxTE1KTWV4akliVzV1bGppWmNNaUpPWENNeFEyblpST2wzZ2xnSHFSZy11ODdwNGR3SzRhNzJwMVo5QmZaT1JDZ2I4Y25yTzlUUkFyZ1lQa01QSUExWWNWTm53MldWRVhEUTlJTVZZUXBfWWtnTEN6MHB4eHIxWk9wTzl2a0FJY2lob3BxQWJld2F3VHM4UDYzSVBaQTFXVXJQb1FfOU83TFM5ZzRlOWZCN3d0SFlXWVBhcWdkUkt6WFp5X2IxNA?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
