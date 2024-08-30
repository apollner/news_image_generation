# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Typhoon Shanshan pummels Japan; millions told to evacuate**

You can read more about it [here](https://news.google.com/rss/articles/CBMiwAFBVV95cUxQME41cVZmQ1JDcVdLdWNhQ3VuSXkwdUtxYmZsRDRHS1BYYV9CamhhSnRiRFlCSFctVDV1blRVa1N5S0lMWkJ4cGJieU1VSGV4WloxTTVHZmtXTGtqeHRRWF9PN2pHdDlqWkdrSlozNXpMMGhEODlYV3JEZFBoYnZENkRoQUxRQzZzODQzNFU0bWV2S1RWSlJGQUx3ZEF0Ni13TUdmMjgxanpzbW5lVURoUXpxdDNlX3BYeklldENQdzc?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
