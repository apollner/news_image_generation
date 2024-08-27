# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Dow, S&P 500 edge up as rate-cut bets firm; energy stocks rise**

You can read more about it [here](https://news.google.com/rss/articles/CBMipAFBVV95cUxNeHYtM21YdUY1OU5zQllMT1hoMlM0cl82N1l4TjhBcGV4UVlEc2JabWdFMjBaTWpGU2RHNTY1QXFRbFA4V0prY0U0SkZIRkRTRF9Wdk1Id3JBblZpV2hxejdFT1BqNThlWkRHTXlLYkpwNG55RHc5dy05T0NyZmRUSGtRbUVtTHZYaGEweVN2T0VkcmlMT1VJQndGTkNNZDJhZ1JrbA?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
