# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Supreme Court allows White House to press social media companies to remove disinformation**

You can read more about it [here](https://news.google.com/rss/articles/CBMiY2h0dHBzOi8vd3d3LmNubi5jb20vMjAyNC8wNi8yNi9wb2xpdGljcy9zb2NpYWwtbWVkaWEtZGlzaW5mb3JtYXRpb24tc3VwcmVtZS1jb3VydC1ydWxpbmcvaW5kZXguaHRtbNIBXGh0dHBzOi8vYW1wLmNubi5jb20vY25uLzIwMjQvMDYvMjYvcG9saXRpY3Mvc29jaWFsLW1lZGlhLWRpc2luZm9ybWF0aW9uLXN1cHJlbWUtY291cnQtcnVsaW5n?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
