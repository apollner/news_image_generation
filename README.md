# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Oil inches up as war jitters outweigh surprise build in U.S. crude stocks**

You can read more about it [here](https://news.google.com/rss/articles/CBMibGh0dHBzOi8vd3d3LmNuYmMuY29tLzIwMjQvMDYvMTkvb2lsLWluY2hlcy11cC1hcy13YXItaml0dGVycy1vdXR3ZWlnaC1zdXJwcmlzZS1idWlsZC1pbi11cy1jcnVkZS1zdG9ja3MuaHRtbNIBcGh0dHBzOi8vd3d3LmNuYmMuY29tL2FtcC8yMDI0LzA2LzE5L29pbC1pbmNoZXMtdXAtYXMtd2FyLWppdHRlcnMtb3V0d2VpZ2gtc3VycHJpc2UtYnVpbGQtaW4tdXMtY3J1ZGUtc3RvY2tzLmh0bWw?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
