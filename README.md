# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Kamala Harris accepts Democratic nomination and Donald Trump visits the border: Morning Rundown**

You can read more about it [here](https://news.google.com/rss/articles/CBMirwFBVV95cUxNNTNkUC1wNzAzSGVoSElaT2tDRXdidzFCTmVYdmZfODd3cjgyRmRvNFlNb2J0MVowSzFjcGt2UmlxMUgwTnBCMTVkVmZFOEJvUkNtNHhSaUpOM0N3ajZGbXJONDE3eGFNRzJSaURwaUR6ZHBJMEN6TE1PeFVIdFhxTWE5ZEFIa1NHcW5aZVEwZ0l6NzRBN2N0QWVWQkh4MmliV25pX3N1R1BqbE9EZEI00gFWQVVfeXFMUGpVdW5LenNVaEgzYVBwek1nMVNWbWpQdHZ5T1gtdFNXVlNRSWJjWFMyQXJkdmxobDRrNHE1X3N5RG9heEVqdHdLdEdfTWxFV1g2RzBPbWc?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
