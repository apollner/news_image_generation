# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Week 1 Overreaction: Georgia pummels Clemson & is the U back? | College Football Enquirer**

You can read more about it [here](https://news.google.com/rss/articles/CBMiwwFBVV95cUxONFpkMW5tbGxndlJTYV92UTBOZ3YtamNqQW85SEMtUWp0Z25fR0JaMEZadXlvRFI4bXl0M2YyNFJIQ0ppc2twRkxDamZpVlZDRWpld2VNX2tqWVdyaW1EWmtPeEJfMlZqNjMzcngxUlEwdWRVX3l0czNwSWJNLTdLZ2VnTV81U0Vob3o5X1BKVmZZbUUwMnNudklJNWJMN3Z2U3Y2d2hFUXprRGVTN2lsV1JJWUpwOGlZTGNmcFhzYWlzRUE?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
