# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**U.S. Navy struggles with warship production while facing expanding global threats**

You can read more about it [here](https://news.google.com/rss/articles/CBMirgFBVV95cUxPdHZlN3lCQlZWQmx1SEVHS3g5YmE1eDc2b1JGTDBLcUw1N0dFVHlXLTVsZGhGd3BuUzdIUVJsdmx4Y0ZPdVh5OUFWTlVqOVdaSU8zY3VZSFR5QXRLSWhkUEZlSFhtUHBxRV9mOWNRNnlIbHo4Y1NnQWo4WXB1ajFOY2pwXzRtUHhBbENlZVN5R3k1OHVRZThsWVZvUVFITG4xdDVWOHFwOG9nZHJUM2fSAbMBQVVfeXFMUFRYRGE3UWxrNmRJQ0llQUZOTnM3eUEwTUN4eXg1MWlBcTZ2VEI5Q1kxUGlKWngweENUeXM0cUtFdUJENDA5TFFQZldjdWRDUXhaYlk5cXZuT0VWVktZQ1BBem5vRkszLXpkenZRdmw0ZGI5M2NoZjVacmlHa2x2UU5nbEM0ZV9uUXo3TjhNbEg3dzh1QjFndm9rZkdCempFSWhnT01HUlVHeThHcVNBeG9hb28?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
