# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Trump says he agrees to Fox News debate with Kamala Harris on Sept. 4**

You can read more about it [here](https://news.google.com/rss/articles/CBMilwFBVV95cUxPZWZCQTZCN1VHZ0VyVDNUT0EzMW5kSHhYZTltekxGSndzQVVoamx3elg3WWxZTWJ6aTNwVlVqdFpjMzJiRXVlSnltUElfX29aZ1duME95SUFrUWtvLUc5d0VYRUFjc3JXcTF1cEtmdnhDU3pEUU1EUzAtb05iMjR4OXNvcDZrQ1ktOFJTbnJZdTM3UWNkNzBV0gGcAUFVX3lxTE5xS09pNl8zUWJOS21jUGFJdlBxOWxXV3pyT29pUWItQ09hcVFjZ3pfSXdrNTJaRXlLeTJKdWpBRHQzdnRyelBGU1BDU3M5OEgxTTJjS0cxb1IzTGpHbkNpRUFpSEl3bEVkQkdURnJnRGtLTU1oaTh2M3pjMXpseFliMW43cVNCLUdmZlMtLXRSSGUxSWZTbExRRE5Deg?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
