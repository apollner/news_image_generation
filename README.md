# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Trump assassination attempt: FBI reveals first photos of Thomas Crooks’ firearm, IEDs in car trunk**

You can read more about it [here](https://news.google.com/rss/articles/CBMitwFBVV95cUxPX2FKdy1keW5kVVhOTzlpaDFOdzJxb1FBWWFXM3hDNzNya2tQTjFfQXhad3hJSENTWEFLdG1SbTNhNjV0R1dfcUN1cDh0SW5PV3lKUmNBcjhnR0w0RXFxZmtrODZPQWtLam1iZXV3SUtTckdYeENkbUZta2hZQWtYS2VkNjI3ZXUzb0pTMWlzdHBvSTVKTVhDM1NianpzREp1OEZqMmRiNFJnQVdNeEFrMUhjUWRwN2vSAbwBQVVfeXFMTWpSbjY2NzVHZUsyVU5uTVBmbEZFdkdRempOc2R3dVNuYlN5MVNaemRQRDdyT2dTWnNrRC1leFo5UGZaeVFqU2JkQy1ZekxXSVZibkpqd0ZIZEE5SjVpTDBBdWVYYV8yb3lVMWRITnNfTlgyT2xMZWlyVFZQX294RjNHSWhYLUk1cnppbm1EbUR5MU1rR0dSeFluc0psZzN6cndHakxZSm9UVF9talpYV29lM3QydUxZcE1taEk?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
