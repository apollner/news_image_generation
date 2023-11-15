# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Israel shows alleged Hamas ‘armory’ under children’s hospital in Gaza. Local health officials dismiss the claims**

You can read more about it [here](https://news.google.com/rss/articles/CBMicGh0dHBzOi8vd3d3LmNubi5jb20vMjAyMy8xMS8xNC9taWRkbGVlYXN0L2lzcmFlbC1hbGxlZ2VzLWhhbWFzLWFybW9yeS11bmRlci1ob3NwaXRhbC1pbi1nYXphLWhuay1pbnRsL2luZGV4Lmh0bWzSAXRodHRwczovL2FtcC5jbm4uY29tL2Nubi8yMDIzLzExLzE0L21pZGRsZWVhc3QvaXNyYWVsLWFsbGVnZXMtaGFtYXMtYXJtb3J5LXVuZGVyLWhvc3BpdGFsLWluLWdhemEtaG5rLWludGwvaW5kZXguaHRtbA?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
