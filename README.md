# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Santa Fe chosen as one of six finalist cities to host Sundance Film Festival**

You can read more about it [here](https://news.google.com/rss/articles/CBMisAFodHRwczovL3d3dy5zYW50YWZlbmV3bWV4aWNhbi5jb20vbmV3cy9sb2NhbF9uZXdzL3NhbnRhLWZlLWNob3Nlbi1hcy1vbmUtb2Ytc2l4LWZpbmFsaXN0LWNpdGllcy10by1ob3N0LXN1bmRhbmNlLWZpbG0tZmVzdGl2YWwvYXJ0aWNsZV9lMGQ4NzRmYS00NWYwLTExZWYtYmNlMi05ZjAxMmMzMGE4ZTUuaHRtbNIBAA?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
