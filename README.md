# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**iPhone 17 to have 12GB of RAM, compared to only 8GB in the iPhone 16 - GSMArena.com news**

You can read more about it [here](https://news.google.com/rss/articles/CBMiqwFBVV95cUxPR1o0VDNqN0FoeXc5NzZYYnJva1JEbE1FZFNsY0RyWUE1X2t2Y2J0UDhWcTM1blh0d1FxU3ZxX0w4LTBpd2RhcllldWg5a3I0WlIza2tvLXpMaG5jOERtV0VzRHBSNWJ0enZRRG45ZndNcnZRb0FfbG5ubUtMaWVoWlUyS3o0OFAwcnBKemVZOUJJLWVqMU1NM3lIa2FWck1TV2xyaU1aTk1uREHSAacBQVVfeXFMTWlXLVNGbTd3MXFwUjdPTEEtZ1VOM2Y5VXZZYkxUMmpWbEJUeEJQYTJJSEdSNFdNXzBvWG9rSmVJUGVaeVBuaF94aGJQSVFRMlEyZFdYeTZqMEROVDRCcjFtZDMwemhoUGlTc1NXOF94bGJOSE55N2taaHEzcjlQcWdXUnZPQkMtR1hETzZRNkFLalRjUzZJdV95Si1VT19LTkxKSmZ6Ukk?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
