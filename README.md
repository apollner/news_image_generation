# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**MLB Rumors: Red Sox Beat Out 5 Teams For Garrett Crochet**

You can read more about it [here](https://news.google.com/rss/articles/CBMiiAFBVV95cUxNcWZHS1pXbTJpOEtuenFpREVSZXZlb29YVm9ZMWVzRWxOam1zY0hFcC14WnRPblBjUm9ZSWRQYldhV0hRdmhpeEtyOExNMWF2ZTFhWUlYUmIzUUdzcmlsTEVIdkVSVGhqT0hUNUhqQ1gzbXNpOHNDZ1FqLUJ6N3BESWU4YVhuSl9H0gGOAUFVX3lxTE5IT0FnaDlvSVRlY290bmpUZ00xZXNFNzg5ZTJZcDh4SFRWX3V3LXBtMDR1NXQtUzZrRzYxQ0JFeF9GUGZtY0NQTkNVaXRJWFNvQUxuNTk0ajNiRDFJdFNMaTBFSjBBcHl6eWpqZ2diODNqT2lsbS1vcU5uQnhjcV9HeG9lZHRDekZtSmkzT1E?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
