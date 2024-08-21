# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**‘It Ends With Us’ actor Brandon Sklenar addresses online ‘negativity’ after backlash related to the film**

You can read more about it [here](https://news.google.com/rss/articles/CBMikAFBVV95cUxQUEtESGRYaWExZDgxbXp5RklDbVYxbDNzT1FyNy1YLV9WSlV4azhwSERDeDJqUTVjNnpPTF9JYlBMVlBQa3JpV2VPUUFqMS1lYkFlSFpUa3Juc09hdW1uZ0psc2lyVUNpTkJOVXpqbW1CeExDZC0taVNkc3lCcUZCQm5hcDRCaF9DZ1ZWakVSYmrSAYcBQVVfeXFMT24tQVpNQ0NRb3M2UC05Z3NCb0FCTy1VVVF0TmdWOXp0ZHR3SHh4YTk4UUNKN0tucXgwZ0t4VW9LdlktRVdSbmRzQ3JMZXV1LW5SNjgxUXZsc21CTG55ajNkeTVBWnRNWUlHNjBtcVBiUXJ2Zlh4Tzhmc0IwN0NDMWRHaEFuT2JF?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
