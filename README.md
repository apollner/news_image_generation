# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Israel-Hamas War Day 266 | U.S. to Remove Gaza Aid Pier Due to Weather and May Not Put It Back, Officials Say - Israel News**

You can read more about it [here](https://www.haaretz.com/israel-news/2024-06-28/ty-article-live/smotrich-backtracks-on-decision-to-withhold-funds-from-pa-fearing-its-collapse/00000190-5c9f-d7e5-a1f3-dd9ff3360000).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
