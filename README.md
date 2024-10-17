# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Italy passes law clamping down on surrogacy tourism**

You can read more about it [here](https://news.google.com/rss/articles/CBMimwFBVV95cUxPOWNoaWZtWWI2ZGVDYW9fTXZoeGp6Q3dscDNEdFVGZnptZmdrSHdPbUI0N0FoVlBKSEZyZ0RtVUN3OGpPZVlxSzNya2RUcDQxUDN5WjZkd2FsSTg4S2FRREd6SXhid2hzdzdMLVlTWS1yZjB3Rk9ZQWNWOHphaTIteXptTXJNTjhxcktjQ3JHTV9Kd2pra1g3V2t2WdIBmwFBVV95cUxPYjdURzVES0N6WWJBTnN2bDhiX2xlMkZya2NPMFNyelM3ejlLS1huNFVkdk1NN3NLZWpJTUZrSDc2TTE5dlVOSFMxOXRDT1ZMamlrR0FrSVhMcG5iVGs2UjM1VjdIdS1pNGluQWlXZkRvSEVtQWp4NEMzSllHS3hzbHRLZjY1ejFCaHdTeVZoRHdJVmRremkxZjhqVQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
