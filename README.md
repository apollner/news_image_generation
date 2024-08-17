# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**NBA schedule 2024-25: 10 must-see games this season, including Knicks at Celtics and Lakers at Warriors**

You can read more about it [here](https://news.google.com/rss/articles/CBMi0wFBVV95cUxPN0dmSmtQQ0owV0NXR3MwaG1fRzBGS2swWEgzWHR6Ny12dTg5SC10NDVtZjZRN2l2TWhaMnF3OTFhU2gySnVyWHczTXFjc3Y4dEU3TzdYY25hVERPTEtfUmZ1dzBwV2kyMnYyaEZsMW9Tc3EzVnljdHNmX0NFbkQ0NGRhR3J3cm10LWpnNkNZQ1JxaHp6V2ZORmhuVXNMMW5MdkY3SWlRb0M5Ni1QdGNKbkdwRDdKYkFPNDdTbDBueVczRVhfTnVmNllEZWVlSW9tV0VZ0gHYAUFVX3lxTE9vQnJubnp2cjlEUkN0VnoyTjdZQnN3Vzg3M1p0c0xoY0V1SVhvMkZfYXdIVUtjcnA0Ny1BWXdKc1YwOXVIUVhEaExxYVBHaUhZX1BRNFdvMkpQNFUtTFJJcHJwSHNUeWd6NnZJVDd3RE5mZDJYMExVLWh4Slh2b1UwQUtDdVJYMHZtLWdvRS1uUGJPc1hxV3Q2MnYtU2RYa2dZandZUVNITXNRbWoxakNxbEZwRWIyYllxSTRZTWRwbHBIb1FJc01wYTFidFdxUEpoZVBfM2RxNw?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
