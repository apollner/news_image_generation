# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Mondo Duplantis breaks his own pole vault world record again, weeks after Olympics gold**

You can read more about it [here](https://news.google.com/rss/articles/CBMiswFBVV95cUxOV3JNcTMxM1BqZnBEVU9RYUZRZ2lsWVpic2tGSHkwdnFLbWppVWdkMllpaDc2dGlpOUpTcFRyU0xKTmROUUdLQWRFZExFV2xjbXN0N2ZrV2xjY1pka3FvZDlTenNfUjNfVjlidHpwN19STW82MnZqR0RMTXFmbFExWWh4WGZ5OVh0NUpqclg4VFRQTzFiX1Nqay01UzExazB6YVRjOEhIT0VmWHlTV2FfWUs2MNIBVkFVX3lxTFBGazZwV0V0TTQ0MmJXTTB5aVI3TDhxa21haUNBWmJsSFdJU1NBcUlLdnFLN09CaEF4TGpqZmRIOW5KOVZ5T0dzR1VUY2dIVzhHRXBkaFhn?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
