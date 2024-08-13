# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**US orders submarine to Middle East, carrier strike group to sail faster**

You can read more about it [here](https://news.google.com/rss/articles/CBMisAFBVV95cUxOWHY4VUdZS29XcmdrN3cwTEI5SEc4ZUVpOFpKcGdNMjJtS1BUOFVJM09sZ2VDT21RejNCTVRSNUZhX1c0eFd3U2Z5TktoYy1IaFNPOFNZZmwwQWRTRXFIRkhNRnhycXNHWmJOS3BKN2c5TW1sWVhETzBXTWVsRXpCTGVaVWZSVUxLTXdfOURKTU1sVEk5dTNUVktHY1VmbnhicXowZ0tiMWY2bGhpSkNjb9IBtgFBVV95cUxPZC0yc3BIUXhHbi14bDhoejkxVlZMZU9oM2FjVXZKdHh5am1fM3lrVDdEWGd6dlZTOTdpNERrRHYydHYxYXQ3VVI1QzFEdVR3VGF6UHZ3Y3dmTEgxaTlkaGM2T245eXVrbnB1N1pRX2MwY3pYZVdSZnVYUXdhWTBVMmZCb1lUYUlkamRiTFBNVzZyYnZwTDJaeWxnakRpdnk5eWZYM0I1d3VXVi01QlkzR1hrbzcwZw?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
