# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**The US is experiencing its largest summer Covid wave in at least two years**

You can read more about it [here](https://news.google.com/rss/articles/CBMif0FVX3lxTE10d1J1bFA4WUx6a3JaQjhWZHZlaVlhaXBlZWJaUUlaVkpwcERxOUdCQV9aYW5Ib3M1OTd4c3M3ZWFDYzhnUnJBWHJJbGlYNnlGQ2FlU2hHLVBmV2wweTBuc0NITlB3eGFsOW9EZjAwS2w4VjRrYi1IbFNFai1kajDSAXZBVV95cUxQdGNNTUplWWdSV2NBTjFZd0tsaE9QaEI1OFBlMXJXTW9VaW1PQUVyV3lBd1NrclE5R2kyTUhDMWxMVF9rX2FGZlk4TzRVRkt0NWZWN1ZhZVZIbDdUY2kxR0kzdFJaWDd1aGZSTDNpNkdqWXVnczJ3?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
