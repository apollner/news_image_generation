# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Who is Gov. Josh Shapiro, a possible Harris VP pick?**

You can read more about it [here](https://news.google.com/rss/articles/CBMiUmh0dHBzOi8vYWJjbmV3cy5nby5jb20vUG9saXRpY3MvZ292LWpvc2gtc2hhcGlyby1oYXJyaXMtdnAtcGljay9zdG9yeT9pZD0xMTIxOTg4NzHSAVZodHRwczovL2FiY25ld3MuZ28uY29tL2FtcC9Qb2xpdGljcy9nb3Ytam9zaC1zaGFwaXJvLWhhcnJpcy12cC1waWNrL3N0b3J5P2lkPTExMjE5ODg3MQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
