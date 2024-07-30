# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Local SWAT snipers saw Trump rally gunman nearly 2 hours before assassination attempt, text messages show**

You can read more about it [here](https://news.google.com/rss/articles/CBMiWmh0dHBzOi8vYWJjbmV3cy5nby5jb20vVVMvbG9jYWwtc3dhdC1zbmlwZXJzLXRydW1wLXJhbGx5LWd1bm1hbi0yLWhvdXJzL3N0b3J5P2lkPTExMjM1NjYwNtIBXmh0dHBzOi8vYWJjbmV3cy5nby5jb20vYW1wL1VTL2xvY2FsLXN3YXQtc25pcGVycy10cnVtcC1yYWxseS1ndW5tYW4tMi1ob3Vycy9zdG9yeT9pZD0xMTIzNTY2MDY?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
