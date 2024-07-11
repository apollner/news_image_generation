# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**England vs Netherlands live updates: Simons, Kane score early in wild Euro 2024 semifinal**

You can read more about it [here](https://news.google.com/rss/articles/CBMihwFodHRwczovL3d3dy51c2F0b2RheS5jb20vc3Rvcnkvc3BvcnRzL3NvY2Nlci9ldXJvcGUvMjAyNC8wNy8xMC9lbmdsYW5kLXZzLW5ldGhlcmxhbmRzLWV1cm8tMjAyNC1zZW1pZmluYWwtc2NvcmUtaGlnaGxpZ2h0cy83NDM0NzI4MDAwNy_SAQA?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
