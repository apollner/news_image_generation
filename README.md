# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Independent poll shows dead heat in Maryland Senate race**

You can read more about it [here](https://news.google.com/rss/articles/CBMinAFBVV95cUxNRm0wZlptU2xqZGp6aG40dDdCNVNXclpXdUNKU0MtemYyR1ViS2s2X1hhMENBS1NMdjl3VU1fbkJyaUpteUhJYlB5TmR5MWl2NkRTTm5fWkloR2U4V0l5RE0welE3enppeHpFTGhOMFFyODNtdEU5MnFMMGRuOVo5Z3FremNjNERzdHVxNUVFMm5ZWDFqMEtvRk9aUHo?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
