# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Judge dismisses Giuliani’s bankruptcy case, allowing creditors to try to seize his assets**

You can read more about it [here](https://news.google.com/rss/articles/CBMiW2h0dHBzOi8vd3d3LmNubi5jb20vMjAyNC8wNy8xMi9wb2xpdGljcy9qdWRnZS1kaXNtaXNzZXMtZ2l1bGlhbmktYmFua3J1cHRjeS1jYXNlL2luZGV4Lmh0bWzSAVRodHRwczovL2FtcC5jbm4uY29tL2Nubi8yMDI0LzA3LzEyL3BvbGl0aWNzL2p1ZGdlLWRpc21pc3Nlcy1naXVsaWFuaS1iYW5rcnVwdGN5LWNhc2U?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
