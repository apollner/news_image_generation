# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Their homes burned in the Camp Fire. Then again in the Park Fire.**

You can read more about it [here](https://news.google.com/rss/articles/CBMipwFBVV95cUxOUXQ5TjROYU9vbThxTXlJR2dfMlZnNDZ0RzhaR2ZNdlAxdzhlbm84RDNYLVBlb2lwYnl1czZYVGFXczBsbkhTbEMzQVZMa1kzdFFRU3JxT3B4bW1FUkxIRi0yTG43SDllc3BwRG1YZzZnWFhJNEhrUUJ0VVFGVDhxWUhydUhQWVM3WmxseHpNNDdxSngwT0U5QmRJa0FBRDVVSFdzdkV0RdIBVkFVX3lxTE9HUTVPeElCOWF3ZllJb1Q2b0NGUTQ0SHZWNFpiNUYweDJJUmd5R0dWWmp3TlY4U2pnamg2eGdkV3BGaEY2OFZRc2RCVDlnZ2FxNlFOc1h3?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
