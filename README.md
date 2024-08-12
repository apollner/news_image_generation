# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**‘It Ends With Us,’ a Romance Based on a Best Seller, Soars at the Box Office**

You can read more about it [here](https://news.google.com/rss/articles/CBMixgFBVV95cUxQZmtHaS0wU1pieHphMDR6YnF2bFpqcDBxSUswS0cwdTN1VFNEZGE5SVp3YVdmcTVzc2JmRUtuaDFkUzdzVURxUDBrQnZIbWZMRjMwNlJibWtwTFR1VEd3T3hXSEZYRDNDeXFNSjBPZkJyaHo0RVhhbmFXbFY5akdNbFVuVDhXX3h5Z05DX05tMld3YmZpQmY0WUcyUVoyWThwVGlTdFZsbktfb0U4SWRUUGNwc2ctZ2JSR2wwZkpRWktfS2Q1THc?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
