# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**This is what office towers could look like due to hybrid working**

You can read more about it [here](https://news.google.com/rss/articles/CBMibmh0dHBzOi8vd3d3LmJ1c2luZXNzaW5zaWRlci5jb20vaHNiYy1vZmZpY2UtcmVkZXZlbG9wbWVudC1sb25kb24tZmxleGlibGUtd29ya2luZy1jb3Jwb3JhdGUtcmVhbC1lc3RhdGUtMjAyNC030gFyaHR0cHM6Ly93d3cuYnVzaW5lc3NpbnNpZGVyLmNvbS9oc2JjLW9mZmljZS1yZWRldmVsb3BtZW50LWxvbmRvbi1mbGV4aWJsZS13b3JraW5nLWNvcnBvcmF0ZS1yZWFsLWVzdGF0ZS0yMDI0LTc_YW1w?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
