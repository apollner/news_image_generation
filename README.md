# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**'Slapped Cheek Virus' On The Rise In US. All About Parvovirus B19**

You can read more about it [here](https://news.google.com/rss/articles/CBMipAFBVV95cUxPcXdHZjctejVtWTdmcnMzbHFhdHN6YWloVDhUUG41MUpDRlZKY0hOYV9qTWhqY2FoVWtGZGlRY2ZlQ2hTV3N0NTc3Vl9JQ281aUtONGlTdVp4eWt2QTc2cC1RYjdxSkh0YU10UFUtMUl6bnhqMTgxalVGUGZiaGtXeEo1VGtnU2VyN1h1RWN2aGRoUFJUSWd6TC1TR0VSNmVWTlN0U9IBrAFBVV95cUxPXzZlcW5xYkRuTElaRXE3LTdsNkZlWnNLd2hYTU56bWFKZDJlUE1USV85d0hnOHVtMXBUVmlLSHNoZXRCTHNCLU5vb3VxcWxLdnVMVEhWNVFMbkZHdW1YYkJjbzFqckNjSE8tU1oyTVk1X2l5MDBtd0xKUkZZU29vVjB3R0cwMlRSamIzdmxOQ2xqWkdoYVYwUEk4RHp5R29ERVpWcTI0MW5RT0ZL?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
