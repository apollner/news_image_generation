# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Sleeping in on weekends could protect against heart disease: Study**

You can read more about it [here](https://news.google.com/rss/articles/CBMiqgFBVV95cUxNNVlfdEE3ZEVJa3BKTmllcWo1N3JheW1CNkY4c2VEd0FKVHlaQU9rMjdlWjdmMHUtczk3SGQ3blZPVFJPbTZ5eVVWeGVTZkFtUS1hLXdLdGlJR09vRW9GM041SDVFY290REZXemVISDNxbEZ1ME9QbmZ1RHlEQS1FelA4YXZqaHFNQjkxSVV1ZU95eG15VjdxX2swR3BHYmxHMEt6Nm5yNm1tZ9IBrwFBVV95cUxOZmZUOFFDOWpBR1F4Mng1NFlEUlp6Sm9YV0NIa0w3Rk16NTJLZ3l5c1Q4YzdNSGsxdUN1VEtYZ3hXWDNMaWpSUDU0R1YwN3Roci1wNjc2cDNmMV9FbFNZellhZmRWRDFTN0k5NGIwQUJZNmZvUElUVlBma1Ezc0o0TUF2WExlZFFvaUxRczRxY0NsSmhwQ21RaVA3NWl3dF9PMzRpZk9DSlZmZGdUclJV?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
