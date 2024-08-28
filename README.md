# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**With pandemic memories fresh, town’s voluntary curfew to prevent spread of lethal mosquito-borne virus draws ire**

You can read more about it [here](https://news.google.com/rss/articles/CBMiowFBVV95cUxQT3U4ejllX2d0WnJjUWlwU1pNbDFDcGg3Y0xTeXpfU3JsT2IyNUtialVqQ1E0UnNRVDdqN29PcElOWmRZZXkxb0lNSmI2Qk1aOFdhUnR1OVl0TC1WM3dvU0d4RVFhNWFUTG9TZ0c2N3JvTjJXR3BZelpnSWxfMlloSkJlT05MQy01bk9tRWdVbldIb0RuOVVnTFZXejNMa2RZdEkw0gGaAUFVX3lxTFBwYUticWRKOTdGODNzTUI2NHBLNGdlTmVBVVJVN2Q2a1JobjFaTE5Ma3JrRmZERWdSSnpFek9GcnRpdDBDM2pHaWxhMTNuQXZ0Y1hKaUN6V0tYb0t1Y3JUVDM2OXR1OE9JeGZ5aU5mLXhKNmNOT0xEbHFhZE5FcE5odTJuSTk1UmNyTHpBaklOYldtMW9tUFF4cEE?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
