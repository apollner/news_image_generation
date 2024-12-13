# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Intel Arc B580 Delivers Promising Linux GPU Compute Potential For Battlemage Review**

You can read more about it [here](https://news.google.com/rss/articles/CBMiakFVX3lxTE5FT2lnQ2Q0SUFWU01zSlZOcEZaOHlTblU0ZHJscmQ5N1R2SFBVQ3BxV09PbGl4d2N3UTFvTjV5cnpvbk9PQXV1SmdMRGlETnplZFBJREZMeXhCeWZheW56ZjkwSWFnNmZtd1E?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
