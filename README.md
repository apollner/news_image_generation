# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Israel says its Beirut strike killed Hezbollah’s top military commander, who it blames for Golan Heights attack**

You can read more about it [here](https://news.google.com/rss/articles/CBMiowFBVV95cUxOUGZYRXNpOEVJeW42RWppNDJmdzJfUnBKTW1Ka2VyeE43SlBrdjdGSVVCRWVvVHpSRkxXOUo4YTRaZFdFOWkzVlh0Ykg0di05dzF3bTRvb3FtYzJWMzFpR2ItUmNPbVZwdXEwR0tySWREcTFSb1B6aEQteU5jQURUSFVqZ0dZcFFHUUJ0Q0plMkpyLTBFaTN2b3pVU2xXOTB1dWNB0gGaAUFVX3lxTFBhdmU1R2hSTGxLQU9IbUNPSjNsS0F6QWJLSGtrMjY2bTZpeWNPczZ2SHpvaVlDSFRNc2RYVTVyZ0dpbDdWSHBLalUtTWc2U01wT2oyanAtbUVuR2cyQ3FMZUhmTnlrQ2RqMDVLLVpYR09pdXc4NEdPdnM4cnNrd19PUnJleV8wTjZJUGhrQ3RtMkhoRDJNbFl5V3c?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
