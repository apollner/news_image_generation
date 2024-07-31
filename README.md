# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Stock market news today: Nasdaq sinks, Nvidia drops 5% ahead of next round of Big Tech earnings**

You can read more about it [here](https://news.google.com/rss/articles/CBMiigFodHRwczovL2ZpbmFuY2UueWFob28uY29tL25ld3Mvc3RvY2stbWFya2V0LW5ld3MtdG9kYXktbmFzZGFxLXNpbmtzLW52aWRpYS1kcm9wcy01LWFoZWFkLW9mLW5leHQtcm91bmQtb2YtYmlnLXRlY2gtZWFybmluZ3MtMTQxNjE1MzA3Lmh0bWzSAQA?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
