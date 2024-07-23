# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Election 2024 updates: Democrats say they've raised $46.7M: 'Biggest fundraising day of the 2024 cycle'**

You can read more about it [here](https://news.google.com/rss/articles/CBMiUmh0dHBzOi8vYWJjbmV3cy5nby5jb20vUG9saXRpY3MvbGl2ZS11cGRhdGVzL2JpZGVuLWRyb3BzLW91dC11cGRhdGVzLz9pZD0xMTIxMTMyODnSAVZodHRwczovL2FiY25ld3MuZ28uY29tL2FtcC9Qb2xpdGljcy9saXZlLXVwZGF0ZXMvYmlkZW4tZHJvcHMtb3V0LXVwZGF0ZXMvP2lkPTExMjExMzI4OQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
