# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Charges expected after 4 killed in CTA Blue Line shooting, Forest Park mayor**

You can read more about it [here](https://news.google.com/rss/articles/CBMivwFBVV95cUxNdWNfdlV0VDNjLUpLOXlrOEZwc01seDRlem1fSTZibUJILXczZkdvYVhvdEN4U3E3R2ttSTU2TEc1c0gxY1hYbmNFSGxrbkJUTFJVU29TWEZ0MUJweGp1S0dtYjlOc0JWd0dITGhfZFVHWHJRQ1I0cXA0MlAtUjhlMlVYdXp4OGZtOW5xSW1rWDYzNWNUekU2N2hRVDdiclJmQXFRNTE0Q3U1Ykpuck1GTWE3RDRrc3JBMmtMeHk5RQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
