# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Vince Vaughn makes rare appearance with kids at Hollywood Walk of Fame: 'Most important thing in the world'**

You can read more about it [here](https://news.google.com/rss/articles/CBMiwgFBVV95cUxNNHNQWV9DMU9MVzFKQzdlZndpVU14TU8tMXMxREZJaDJhVkVfMVNQZGpDRFJSLUN5cThiNWxNUVc3Z1F3YlhGbVBMMC1Ba1htWmRzaExud0hjVk95RFV2SGJwTklqdEptWnpXSmRSOG9aZm45TjQxblg3a2Q5cEFKSG9HencyQjlXYVVhZUJFelk5aGtHanNjOFplTHZmcVpDU1R4SUhpRDRJR3JURVBoemVzWDMwSkdQQWREalNzM1psUdIBxwFBVV95cUxQQWpsQ21TTE1JcWVON2t1c3pRRWlJd0Z2UkU1ZXI1aS1STEJCcWlwX05FRE9QSnFnSGM2UnhmZnZ4a1RlZ1RmNlQ3RXFmMWhVWXpOendpdlM0a0R3aDlhcXpEOVotaFNGblMwbEtfMW9ucXIwdTJ4THdTUXF2anl6a2p4TUhPaEYzOG5PQV9DQkJDY2hmTmJpcW53N29FTDBqbVhGbVZ1N29NYU8zUHhzUFZsNXBYVjdUMTF4X0hlcEJUN1p3dHpV?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
