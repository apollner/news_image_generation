# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Dramatic new discovery on Mars shatters Elon Musk's plans for red planet: 'Dangerous illusion'**

You can read more about it [here](https://news.google.com/rss/articles/CBMiywFBVV95cUxOdXNJNDYxQ0U0T1g1NW1ZdlVVT194Q29nUE1wUlVPbUZrYkFjYmlDUlpVajh1c0tja1NGdDZTRHhIUVZrVnlSczdDN2pmbzViWXJwUGtmc2pVdWlDREtYaUN1UmJ5N3ROY2kxRFNaYmRod0lRV3ZaNmVGTV95YnFwTm5QOTZIckFNbkVNTTRBZE0zQVBkVWVvMm1pYTE0YWtGZm9MWUF1MEpQYkdkT0lfTlhiSnQ0R1ZDckZWV2JJR3VqOUdIRG1ReG9tVQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
