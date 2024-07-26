# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Bodies of five slain hostages recovered by military, returned to Israel**

You can read more about it [here](https://news.google.com/rss/articles/CBMinAFBVV95cUxPMTdEem1LYmRIeWJOdkg0aUZka3hyaGtQd0dOekNidzdIejYzTmdjRTFiNU9zemZoazh1aE0zRXFPZWRDRXJGaEdZZUJLcG5manZkcmZsQVRwR2ViQzVlMW01NEcyNjRjcUp2czFhVXZka1AwWjYwY3dRLTlsa0ZtVGJlN1R3VGtBTEh1bHItU094N0ozNkp5N1pIUHPSAaIBQVVfeXFMT21CaGVfczZxT1JoMU1oNWtKLURRU0VBWWZ1eGZkbDl6T0tmTDlHVWZCLTU2TzJjTU9sSWc3OTJsZ2FGTmhWWVlET2FPekNVejQyeVNhUzFaMDRYUWxKMzd0QS1FZERjZFh3ci1iZTRPVXhHeFhaMEwxeGlJUmNNZ1VDUnd6alJGMjh4RnM0aEk5cnlCS3EtMC1sM3VEWnN0eHpn?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
