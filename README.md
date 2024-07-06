# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Germany XI vs Spain: Confirmed team news and predicted lineup**

You can read more about it [here](https://news.google.com/rss/articles/CBMijgFodHRwczovL3d3dy5zdGFuZGFyZC5jby51ay9zcG9ydC9mb290YmFsbC9nZXJtYW55LXhpLXZzLXNwYWluLWNvbmZpcm1lZC10ZWFtLW5ld3MtcHJlZGljdGVkLWxpbmV1cC1pbmp1cnktbGF0ZXN0LWV1cm8tMjAyNC10b2RheS1iMTE2ODQ1NC5odG1s0gEA?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
