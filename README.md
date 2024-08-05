# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Thailand still grapples with a strict law against criticizing the monarchy**

You can read more about it [here](https://news.google.com/rss/articles/CBMiowFBVV95cUxQTXFYXzY5a0NXQ3lCUEpocjBLWkNXdktlT3QwSDBtMm9rNDE1MXZpTUhUSUVkN1ZMdnc4N2d3Ymp4Ny1yOVFmSWduRmpSUFdEeE5IcGJWbmRNZWhfNG4wX3hFWHdfODRGTzYxdVExbGQ2R192QUE0Nmtxd0lOLS04dXcxTjJ6cWsxUTFJZV9qc01lVzd1aWJSc0tQaFdPcUdCaWtJ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
