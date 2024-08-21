# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Netanyahu, accused of 'abandoning' hostages, says cease-fire deal may not happen**

You can read more about it [here](https://news.google.com/rss/articles/CBMirgFBVV95cUxQRjBNc01hSE1FWmI3Y2tQZE5zQWJ5MU13bWQxUWppTllQT0VUZk5YcWUxOHVrS1NTVW9VTnJ0UTllQ2xUcFJnem1PUElMM0x0YmtJeVhUdnJRSkI4cHk3QXB1UEExYXhoMU0xdzdnUDVOUmt4YmlaQkNGTkpnX0I2WU1QOFpoNE9HSDFKZFdaa0VwNURSd0lzMTIwa1BaVkM0Z09BWDRudnZtZF9ZUUE?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
