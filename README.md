# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Elon Musk denies report he will donate $45m a month to Trump Super Pac**

You can read more about it [here](https://news.google.com/rss/articles/CBMidGh0dHBzOi8vd3d3LnRoZWd1YXJkaWFuLmNvbS90ZWNobm9sb2d5L2FydGljbGUvMjAyNC9qdWwvMjQvZWxvbi1tdXNrLWRvbmFsZC10cnVtcC1kb25hdGlvbnMtZGVuaWFsLXN1cGVyLXBhYy1hbWVyaWNh0gF0aHR0cHM6Ly9hbXAudGhlZ3VhcmRpYW4uY29tL3RlY2hub2xvZ3kvYXJ0aWNsZS8yMDI0L2p1bC8yNC9lbG9uLW11c2stZG9uYWxkLXRydW1wLWRvbmF0aW9ucy1kZW5pYWwtc3VwZXItcGFjLWFtZXJpY2E?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
