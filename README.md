# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Yankees’ Aaron Judge finally homers, but ‘pretty pissed’ at Gleyber Torres for disrespect**

You can read more about it [here](https://news.google.com/rss/articles/CBMiwwFBVV95cUxNUzdzZmRaS2hsNmg3ZlhGbFR1UXJaQllrejFYUXdpWDhDaTZwWktqMFlOVEQ0QmxxTzU1ZTA2eGR2YzFzTlZVYXdacFU4SVMtZ1Z2X1otVjB2S3B1MW5ZVGxkbVB0eWg4LWJWbUZ5d3ZJTmMySk9jYnZ0aFJadWRxYWJVQnpSeUd2ekdZWjRhRUNLeTdTUUVkaXVOOEpucjFlWG45U0JCcmRWVl9CQ21EZGRNMmFPX2NVWFdDdU5WM3ZTc0XSAdcBQVVfeXFMTnpPM1NsbW1nRl80ZFE2MnhlbkZGSmpUZzRhOW40bnM3TThXeGRBUXhpb2xvbzVYODRjOFpBU1lUeE11VVhySHI5UGZOZEVFcWt2anRiNXFKUEtHZWVKRWQzTS1USTg2bHNJT3dWY0cxLUZRQ09fNUlQbFktbTZ3b29wVG5tSmdHZEFQc2x2ZVFtZ2UxcVNCRE1sdEtMbWhGNGJ2VWVoak9CM0pfeUtxa0NBdXhTb05BUDhTNGF3b1pxQV9ISkgyS0VyaFc5MUQ1Z0V5a2djME0?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
