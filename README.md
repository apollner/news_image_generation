# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Nasdaq and S&P 500 log worst day since 2022 after Alphabet and Tesla fail to impress Wall Street**

You can read more about it [here](https://news.google.com/rss/articles/CBMijwFBVV95cUxPWVlPTExKRm1xdVQ5UGVKa1BIVGp1OURsSUtHNUE0aE91QVVtX0VPOHpxX0pZaVlMX2lGUGVHVjAyVHFPZlgtcExuQlM2NWJTTDRHSHFyZVlfVXdyLWhQaEVqc01CMG9PUHVTMjlxV29DWHlhdVVNSTliWEFNcEY5c3ZXSGVLQjEwbUJfY1JjTdIBhgFBVV95cUxOUzcwNVNUOFAxRnNLWXRacnQ3WUVsZ1hhZ1FMYTVwNzFQTkxIM25hOFBzVTd0S1QwZk1iNjR6TC15cUt1bXF6YXdoTEVWekVab1hURGVCZS1OeEV4OFMya0JJZ3lZWW5mQ3kxWnU5Vm1kb0hoUVVMR0Uzcm4tUXJkbW92Q1dOdw?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
