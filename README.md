# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**NASA Astronaut Shares Pic Of Moon Over The Pacific: "Mind-Boggling"**

You can read more about it [here](https://news.google.com/rss/articles/CBMiowFBVV95cUxQNnAwUndyX1kyNEdjMW44dGJtTjc0ZDQwUnh6VG9RRU1EUlJBcXdHVGlJREQ3ZmRZSzZCakRubHBrWlQ4TlZnNWhWeFZjWGhFd1I1cUp4ak50S3dQdnlmeFpOQU1Rd1VUN0E2WWtOTjNBblZMdjhIZjcydTVJSU05czFmYXNNSXg5QXNzRGJSQURrUWxfUjJ1Z21UMGhKaVdabmdR0gGrAUFVX3lxTFBXYmNSQWxqenVVbjBoRVNza1RiZGZkY2hPaF9OMGFya2ZvOWFJYWw0N3hrQnZNa0hyR0g3N2FidExlWVZCRFp4YTNQcXZRR1Yzd094VmVlLUc1TWhaU0tYTld3dmVpeTBfOWw2M3RUWWdnZ3RlUnFQaFU3LXowUHBnVVpwQlplUDhvLWllQUYyQjJhSUxmRmxmUGNiaE50bDFWaEt6ZVR0VUEzYw?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
