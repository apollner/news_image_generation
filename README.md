# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Conflict, creditors and a car crash: How Ukraine clinched a wartime debt restructuring**

You can read more about it [here](https://news.google.com/rss/articles/CBMixgFBVV95cUxOR1NlSmFYc2lvZ1ppMkN3ZF83MHRNdjZoQlFIQU9UOWZmR1VkdmRtQjh1VGZBZm9NR2xHc2tzZk5YYm1CUkZqLV85dHhiS3VaSTUxXzdlX0pJTk5pU2JxYzl3SFYyNkRyV0pBSW9lcXYwbkNYY2Y4NWRYQnhzWGZkQzVEUkdBdWp4SnIyS0R6eTd0Q1k2TkxVbm9MajFuejVlVkdSVFB6ZWllRjZLUVVDQ2thdXlJcmV3WjZUenN2Z1R6a3ZYWkE?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
