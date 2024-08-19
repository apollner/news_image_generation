# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**COVID-19’s summer surge shows no signs of slowing down**

You can read more about it [here](https://news.google.com/rss/articles/CBMib0FVX3lxTE1WR0tlTnRYbHFPNHNfNWM5NUFTelN3aTBEY2N2NFNvdkczNXU0Ni1aaTZ2c05uYU14a0d0MU1ZTzFXYXNQd3hWWlhVX2VIaFZSUGRVa2YtTHpLLTRwY1JJTHdwQWlFc2lHUDB3b1l2QdIBdEFVX3lxTFBQMlFEaHBlSEE3NXZJd3FoR2RRSUppRjFlcWttRWdvQm10NU1laU5jTzg3anY3TGIxRGVBV05WYkV3b3czOW1CWDYzNFRLYTRCT2xwanp2Y2dFWURDWWNKa2ltMVE2N0hXTURGQVd1RTV1Y1VV?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
