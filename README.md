# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Duchess Meghan Changes into a Fabulous Oscar de la Renta Gown for a Private Luncheon**

You can read more about it [here](https://news.google.com/rss/articles/CBMi0gFBVV95cUxOR2daUmRJZW1IeHBKeHFMOTJTR3ZmVzZZWlM5NUhmVjdNTWp0aTZiRC1vNW1QZkdwcW5PV2ZybGtTQ2xIQUFONWFaR3FrazhpRTlTTzZFRVNsajQxaDhRT3RjaGFFcDAtOXlvMDdfOTcyMXNOWTdrd0t4VDdOR24zdEthOUI0VVBEd0x1YU1MWF82RVdtQUpxWUtrWVlWSnlUMkdoeGhWRUJfams2cTk1WnBSZE5uaEdPcWNUZGRNRlhnZ0hsOVBKcUdvRlQ5TW0yN3c?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
