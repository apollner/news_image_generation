# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Almodóvar returns to Venice with 'The Room Next Door' alongside Tilda Swinton and Julianne Moore**

You can read more about it [here](https://news.google.com/rss/articles/CBMiqAFBVV95cUxPWjNLYXA3OVJ5LXVyc0RhZW51WmJuMkRzSjJ5NnprbEdDRkRfdEVpYjRsMTVJNzN2WG5JYmFCci1vazZMUEdqZWg1UXZKcUQ3SF92NVR6eXJqSkw3RG1fUTVZMVdiNlRQZTBkWmRSeXdjdmxWWFZRa2JnS1FEVVJlWkRXZ3dkNVU5ZjFwc1lwVUdjaWpONHJMcTQyd3RGS3FhQzFpWVkwZGc?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
