# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**How ‘The Good Doctor’ Series Finale Handled the Death of [SPOILER] — and Took Shape After a ‘Downsized’ Season 7**

You can read more about it [here](https://news.google.com/rss/articles/CBMiXGh0dHBzOi8vdmFyaWV0eS5jb20vMjAyNC90di9uZXdzL3RoZS1nb29kLWRvY3Rvci1zZXJpZXMtZmluYWxlLWRyLWdsYXNzbWFuLWRlYXRoLTEyMzYwMTA4MzQv0gFgaHR0cHM6Ly92YXJpZXR5LmNvbS8yMDI0L3R2L25ld3MvdGhlLWdvb2QtZG9jdG9yLXNlcmllcy1maW5hbGUtZHItZ2xhc3NtYW4tZGVhdGgtMTIzNjAxMDgzNC9hbXAv?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
