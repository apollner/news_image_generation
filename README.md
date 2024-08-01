# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**First Murdoch papers targeted me. Now there is evidence they falsely implicated me in a cover-up**

You can read more about it [here](https://news.google.com/rss/articles/CBMizgFBVV95cUxPdzI3VFc1ZUN5MzJrQ1FjUm53Ni05QThLVGNBWHlvWkNxSFNRdmRsQm4wTGhHcGtlM0k1N290dEdqd0pZVFBTS1ZRZ2FoMThGRTV3bFhXZjFTNlFPWlNtS01KVENDNjhSY2pMc0NIaEluV3E5TU41U1BqY0t1RF96OElCY3ViOFcxRFNFelBZWHBVZGQtWGpONnRKc3FRYTBFNE45M3F6WWVBR09mZGlYNFRmaUl3TjFxN0RXN0Rmai1tWm5fWlU4bDRPNERHQdIBzgFBVV95cUxOcEdVdGhjbEZORXlDckRlaWJMekgyY3A3alAxQzdvQk9ZS1IzNThYV1lRa01zVmNVWjRRVHBHU3JGcUtHeEVVVHR2dUw3ZDE1N01kWmxGQjhZYkhoTmNucGF0UndzS0h0NjVoSjIxcUZCRFAtSHNRaHRua0VSNFBvZzBkV3l1VVZxalJLYmdpTkZ4YjFxYXg1ajlCOTRZTUpGeFo3Z1lHNVpqaWM5dzVfOXRaTGFveWdSMHI5QXNxdGZGbE93dEVyN19zMDJWZw?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
