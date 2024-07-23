# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Kendall Jenner Is Called Out by Miley Cyrus for Singing During Her Intimate Concert**

You can read more about it [here](https://news.google.com/rss/articles/CBMic2h0dHBzOi8vd3d3LmV0b25saW5lLmNvbS9rZW5kYWxsLWplbm5lci1pcy1jYWxsZWQtb3V0LWJ5LW1pbGV5LWN5cnVzLWZvci1zaW5naW5nLWR1cmluZy1oZXItaW50aW1hdGUtY29uY2VydC0yMjk0NTTSAXdodHRwczovL3d3dy5ldG9ubGluZS5jb20va2VuZGFsbC1qZW5uZXItaXMtY2FsbGVkLW91dC1ieS1taWxleS1jeXJ1cy1mb3Itc2luZ2luZy1kdXJpbmctaGVyLWludGltYXRlLWNvbmNlcnQtMjI5NDU0P2FtcA?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
