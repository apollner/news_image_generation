# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Japan plans to raise interest rates. Investors are spooked**

You can read more about it [here](https://news.google.com/rss/articles/CBMilwFBVV95cUxOY2ZjaEFfMXc4WnhWaDROQzhzOWhMTDRaWHloTDNMSVQtMUh4YXZzM1FVai1KeVN5MXpRdGw1RnN1czI0aDZscjdGVVp6RXJmNS1kWnB2d1ZyZ1JNYTlVSnVxMUtnSkplQXppbE1PZlk3elBDdWVuSDlmSDFtaEhCcVdZMnhiX013Qm04TFVNRm1hY1A1N1U00gGOAUFVX3lxTE9iVUptWUZYT2dWOHBUNmpaWjRUYl9pMThHQ01UOEZPbDRTdHBIcGhPdlZ2ZmstMWJfXzBTTHRIQ2xHdW1ZaEVPbzkyMXp2SU5IU0NIZW5WSWpuMnB0NUFyRk56cEJWSExTR2JsX3hkM0RPYV9wT1VpYW05MVl3SUJZVUhublBTNmJCZUNTN2c?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
