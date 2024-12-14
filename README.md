# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Gukesh Dommaraju: How the Indian teenager became youngest world chess champion**

You can read more about it [here](https://news.google.com/rss/articles/CBMiWkFVX3lxTFBVemFnZlJaNzN0Z1pWT0JqUzNZWUJNMmlCb0N3U05yc0pzNDBCMU9mZEMxcVV3Z0RvNVZ4QTVIREZoRUdGUDA5ZFZ3VkxuVmdHVDktUWJUYUh5QdIBX0FVX3lxTE9XR3RMZlZpVkZkcHJTVjdONVpjWnZmbFk0VkpGWUdWanJpa28wVUduX2lWRkt1NkFqSEU2b2JYVndodkZjV1VhT1JjM1dtZnlFQ3F2Y2JEMDlzYzZFeWVZ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
