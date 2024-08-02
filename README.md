# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Why is Team USA so bad at 3x3 basketball? How 2024 Olympics rosters were built after men and women start 0-2**

You can read more about it [here](https://news.google.com/rss/articles/CBMi4gFBVV95cUxPemF0d29BaXNXTEtGbEJUeW9IT3ZqcDUzV1c4dlZZSFp2REYwd3RydXQwUDRaMnYwc0VVZktLQWFmWHNFTHU5YnNkcnB2RWxvaGIyNHphT0RPVHpnY2QzMGdnRDZrczBiRDU0dnpMWlMzY2NuQnJMVDNfRlA3V3A4SUdTRzJHajVYb2dwbGRlUVE5amVyaVQxOEdIYzlJSVpJZ1NMRUppcTNvbExRaFVZOWtPdWkyLU5nRjFSb2VrSm43elhtbzhRb0x5U21Id252bGhnaWhnbTZ1bU1TRzE4RVBR0gHnAUFVX3lxTE5tcFJqU3FDTzFQdTZPeWNQR3RCYUtxT054aVFiUFNGWDlXNDVYWWZ2QkhpMGZhTTFvNGM5TTB2N3pHQmI4dXkza0xfbkcxZjRwU2hEckRhMUNTdm54ZFdrQV9WQ3RfV1dqempfSkhTR2o4ZFhKM09HNWFsak1jWkdOVjRrQkF5M3NGT1hwSXp2TS0yOHFoT2dVUzI1S1JJYWRVSjRYczhkOXN6eDVXU2o4bmJrUkpkcTZrN3d4dzZHUDIxX2o5VGJJTExfYVhsd1IyUWplbDd3RjdNV3ZrSVd3eXNucDVCRQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
