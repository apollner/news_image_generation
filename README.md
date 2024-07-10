# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Mysterious radio signals focus of new solar mission**

You can read more about it [here](https://news.google.com/rss/articles/CBMiVmh0dHBzOi8vd3d3Lmt4YW4uY29tL25ld3Mvc2NpZW5jZS9teXN0ZXJpb3VzLXJhZGlvLXNpZ25hbHMtZm9jdXMtb2YtbmV3LXNvbGFyLW1pc3Npb24v0gFaaHR0cHM6Ly93d3cua3hhbi5jb20vbmV3cy9zY2llbmNlL215c3RlcmlvdXMtcmFkaW8tc2lnbmFscy1mb2N1cy1vZi1uZXctc29sYXItbWlzc2lvbi9hbXAv?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
