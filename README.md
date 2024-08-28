# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Democrats sue to block new GOP-backed Georgia election certification rules**

You can read more about it [here](https://news.google.com/rss/articles/CBMinAFBVV95cUxNc0JXbjYzeURnQ1RjSVRsNzlKbE1RUWtuc3g2cmE3dENlaW51MW9wSVpXREVYR1pjME9VdzNnZERZaHMwQUs3N0RhbHFlTE5WNXFJb1MtLTdobXoydFdYNnhSMjZWUjlEQ0JQR2dNMVI1OFM5TXpEaWl2bHo5eHo0QmZPb3RKY2pEQkhnZG5nYjZuVFJkQ25TQmxrRlTSAZMBQVVfeXFMT3h5aVJyanB0d3A4U2d2MEdKZmVLSEUxZkJsQWFOMWhnNXhLdkIzNWxLS2xZajU5ejFvTHlPdW9nWC1HQXZXcXBtdjVXWjJ3NERrLUNkbEVOY25wNGFjbWM1YnhoWGlhTWFXRklmZC1zdmxMVWtUUy1PWWNKWldVSnRtTEpIakF4dDY2RnB0RlNtS1hJ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
