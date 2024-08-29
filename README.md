# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Longtime Tesla Bull Ross Gerber Unloads $60M In EV Giant's Shares, Cites Declining Confidence: 'Nobody Wants A Robot From Elon Musk'**

You can read more about it [here](https://news.google.com/rss/articles/CBMi6AFBVV95cUxPS0xkQVlaS2FZaENWTkZXSVZKTWNaQ1BWMnJRV2RSRTctSFA0c1BSN2RXZ01UWkVEcWlLZkFOc2JDSXEyZ3JHdzJLUURXbEdVU3ZSMDllcEFUZFUybDc0YzdPSkZ3Y0pGVzFCR1BIRExqV1oxWUNpQS1laUZzWndvcjdDUGhrckZ5WGxxeFVCbHJtbmR0N3haTVFHTkNxRW5aVWp3N1N3LXZ5RjF3bzY5OWlMTFhLTmc2aTRyZURLdzQzUWFCb3drMzdvOUNUdVIwTWJYU21Sa0pFZTNVNTVJeWwtSEdrVEZQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
