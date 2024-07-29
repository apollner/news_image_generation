# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Justice Department accuses TikTok of gathering American user data on social issues like abortion, gun control**

You can read more about it [here](https://news.google.com/rss/articles/CBMijQFodHRwczovL3d3dy5mb3hidXNpbmVzcy5jb20vdGVjaG5vbG9neS9qdXN0aWNlLWRlcGFydG1lbnQtYWNjdXNlcy10aWt0b2stZ2F0aGVyaW5nLWFtZXJpY2FuLXVzZXItZGF0YS1zb2NpYWwtaXNzdWVzLWxpa2UtYWJvcnRpb24tZ3VuLWNvbnRyb2zSAZEBaHR0cHM6Ly93d3cuZm94YnVzaW5lc3MuY29tL3RlY2hub2xvZ3kvanVzdGljZS1kZXBhcnRtZW50LWFjY3VzZXMtdGlrdG9rLWdhdGhlcmluZy1hbWVyaWNhbi11c2VyLWRhdGEtc29jaWFsLWlzc3Vlcy1saWtlLWFib3J0aW9uLWd1bi1jb250cm9sLmFtcA?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
