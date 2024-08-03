# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Who is Josh Shapiro, Kamala Harris’s potential vice-presidential pick?**

You can read more about it [here](https://news.google.com/rss/articles/CBMiigFBVV95cUxQejZCWlh5ekt0S1h4bnpMekxGTGhoemhDN1BFemc1ZENibkpBVVdxVVlWTHJ4S015eTZocXdIQ0FRdENGZ25DU0IydVJad3h3LVRkZko4SjVZdTFqRTdvSHlvLV9iWGZyVFFoN0Vwd3ptd2FlOU5WbjZhNnB2V2VzMHJHZFZoYTNfcUHSAYoBQVVfeXFMTjdwX1RLNHZobWJvY1V6ODRDZWpLZjJ5QmdXQzh5Vl9Yc09ET2p3V3V5cUtXb1RiZFRNeTRsaUJJTEFIRkVRQlhjM1RMUWN2WkhCS2JweFJnTWhVRTZBdG9tT0pUTXZDOG04QURrbXBZdFUwUl91bkowWkUydVZDazhDbkNIZUV3R0pR?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
