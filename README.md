# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Disney reports earnings before the bell. Here's what to know**

You can read more about it [here](https://news.google.com/rss/articles/CBMie0FVX3lxTFAwQjRQdFJxc2FWTjBiVFd2NHJuSGtyYlRGbDMwYUhLV2U5cW9sSVVqN3BUVHpfMkJ6NTl2blNHSjZjYVlXNkVYVC1FRTd5WVJNM3I2emg1LXF4RzM3NWFRSFpYLS1MaUp4NkpmekxFbUNaMExjYUFJcFh2Z9IBgAFBVV95cUxNTnVfZ2F4TXE0cnZvZkUtaDNDdzNucVFzWWZBWEpRUG85TUxyZ0VxMWk3cWNVb25lTEJuVmhlTFNfSmZJQi1Vejk2dXRDMzRaenZ2elItQlNSSHBZNUEzeG10UUlxMC1lX0pqTGg2c0JxOEdlZ0FreHdoN1JfWXJUQg?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
