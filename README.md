# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Israel retaliates in Lebanon after strike on Golan Heights soccer field kills at least 12**

You can read more about it [here](https://news.google.com/rss/articles/CBMiaWh0dHBzOi8vd3d3Lm5iY25ld3MuY29tL25ld3Mvd29ybGQvaXNyYWVsLXJldGFsaWF0ZXMtbGViYW5vbi1zdHJpa2Utc29jY2VyLWZpZWxkLWdvbGFuLWhlaWdodHMtcmNuYTE2Mzk1M9IBK2h0dHBzOi8vd3d3Lm5iY25ld3MuY29tL25ld3MvYW1wL3JjbmExNjM5NTM?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
