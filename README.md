# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Son of 'El Chapo' and Sinaloa Cartel co-founder 'El Mayo' arrested in Texas**

You can read more about it [here](https://news.google.com/rss/articles/CBMiqAFBVV95cUxNMEZqMlg4TExBbzloSlJtVWt6TkxPdWpOOURaVGg2R2pZQWZ6MDhaR0VQUzc1X19VTm1wbVBlY1l3WHNoVFlyTGVONHFOTUdwYWNNMURWQk1QZ25PbUVNYmJKeFRNUDBBMktkVEFwcEVFQWd3M1BYamp2M2lEOXNTZFNaVnlHLTBxNFpYdXVQcnFNc2laam51azZRMkRsQ0tlM0U1XzF1ZTTSAVZBVV95cUxQaGd4dlZFLUlMMDNJLWl2T3lub3lKWWVGZWZ1U0ZBbjJNN3owZlBxUE53TkdhaGRRd0F6amI2MTNESHctUzlqVGVTLUNiSFpUSC1yeDFLZw?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
