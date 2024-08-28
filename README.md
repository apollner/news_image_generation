# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**The biggest supermarket merger in U.S. history is in the hands of a federal judge**

You can read more about it [here](https://news.google.com/rss/articles/CBMiwwFBVV95cUxNTjZMX29sZnZBcVZNcE9UT1BtY2h4TXNoU0Nlbnd5TFo2OEsxU2Q4dWducGJMX0ZxWTBwaWVtN2JJbzNhLXF2NzdlTF9CUGV1UzBUckM1OG5NNUprb0VnTnZqaXZnWk8yek9oTDNBRHhGbjhsaWpPdlU4Y1ExU0RXb1huM2FyM2d4ZmRGcVRjVHFDM3dZbGl1QnVJajZ3UmRIbWdmeml2d0JqRGFVbm9HdWZaeUZZajcxWHFidU0zVVNHQnc?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
