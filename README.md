# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Israeli strikes kill dozens in Gaza, health officials prepare polio campaign**

You can read more about it [here](https://news.google.com/rss/articles/CBMiywFBVV95cUxQbVVXV0J0Y0pQLVJXWGNpLV9qcHlKRE40NVU5dlJFOE5zYzNjY0FLVElGSWc0Q1luaG8tc2xzSk0xQWdOSGRoMkhHeXFzZnBraEdtS1otWVAyam9HbWRCLU9RQktfbFdyb28yQXNNMm5hSHoyMllIVmR0UU02d1dpaFgwajUzMWlvdU1Ib1Rxak1PclRITmlOM3FleXd0dkRkcnNhOUloLWg2aU9QTXphNER1ZDUta2ozWVkzS0lLY0l3RzdOMWNQVmpzYw?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
