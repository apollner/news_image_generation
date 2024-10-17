# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Victoria's Secret Fashion Show returns with Tyra Banks, Kate Moss, Cher bringing fresh energy to the runway**

You can read more about it [here](https://news.google.com/rss/articles/CBMi6wFBVV95cUxNRUlrNFJtT2RIeFdwZEl1MzNRU2VEMmwxckhQUkRPa1FiTDM1dTVUYk02ZGxMTkVkbUxKVXRpZ2F1V05GRVJuX2FKNWhQQnJTVjI0V3VELTlfejBIdUoybnpEOWJkd0RKb2tSQ2lyb3kzQjNHQWtSVkRDTDFoUVBFV2ZyX0RyenRab1FidDd0SGkzQjlzN2JxeGRiaUpUdV9ad2ROVDZkZFdCWUFnZWNtYzEzX0pxT2tkTlp4NzJLZTlqa2VXaGw2NWFIRHhJemxLbnRzVFR0UVZZWUVhWS04R2RtTXhUbnh6UDhR?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
