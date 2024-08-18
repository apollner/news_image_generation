# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Dinosaur killer was a rare asteroid from unusually far away, study shows**

You can read more about it [here](https://news.google.com/rss/articles/CBMiswFBVV95cUxQYi15UVBZV2RkVHNWaW9UX0g4TGNuX09HYlRNcGR6UFZ2blNfSFZIVmFmMnQtaW5ZZlNYTVg3RVdZVDVqdHBTMzRTREliN3N0UTg1cDE1S1FGN1VnVjlJMy1IaDZLeWJwMlNHZTBVZWJlUUs1S3VjUjJWemZGQzY2MC1ZdTZSNVBPRTZvYkxBVHhndHFZOGsxazY0UVNUSGRMZzNNQ2NxYlJKeG8tdExaRm9oTdIBVkFVX3lxTE51VGNYcncxVVRCU3p6cklOOHdTeUJXQVZ6ZHFadmpwb1oyZk5uNWdQWnFyVGtGajFuUXZfWjlTWV9RZDNGcmNxb3JLWjc0ak9mbVo1M0FR?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
