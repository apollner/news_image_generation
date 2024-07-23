# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Sam Altman's giant basic income study is out. Here's what it found.**

You can read more about it [here](https://news.google.com/rss/articles/CBMiTGh0dHBzOi8vd3d3LmJ1c2luZXNzaW5zaWRlci5jb20vc2FtLWFsdG1hbi1iYXNpYy1pbmNvbWUtc3R1ZHktcmVzdWx0cy0yMDI0LTfSAVBodHRwczovL3d3dy5idXNpbmVzc2luc2lkZXIuY29tL3NhbS1hbHRtYW4tYmFzaWMtaW5jb21lLXN0dWR5LXJlc3VsdHMtMjAyNC03P2FtcA?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
