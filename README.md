# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Trump hits NYT while doubling down on near-crash helicopter story**

You can read more about it [here](https://news.google.com/rss/articles/CBMiowFBVV95cUxNQnB6T0oxcDRwSVN6NVU4eEJ6dDhxajZETk9uOVltUGVjbVBmUEg0WlFiRzk2ZktPYm1ES1VwMURhX0xSNGtWazhoV3lJOVFuSmZLNUdQaFZLbjRQWW5kM1VHQXRIYkFBNlJsZFI4b2NQRUJPOHZHQmJsdnZmaXViUzdUamZSNHVTSVpjVjdsV3BqMXJHX0dNUE15WC1LbHh6dmVn0gGoAUFVX3lxTE1FX3poakVYalFmM000R3RUTkM0dnY0cXVXbm9LRlRPZWxSOWdtY1RGVWFxZmcyWUJEMktZYnBSclVKX2M3c1pxalZselM3SEFmQmVPbGxZTm04aUNGdVEyRmozZmhwdDUtT1dldDVWNENuVGd6Rmo0NktBT2dsa0xKRXpDMEtqT1Y1OGxMbDlES1B5SzNvZGVkWmxKdlZBVVUyWTFhTXkxMQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
