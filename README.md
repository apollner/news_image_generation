# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**What to know about First Baptist Dallas church, the site of a major fire on Friday**

You can read more about it [here](https://news.google.com/rss/articles/CBMiiwFodHRwczovL3d3dy5kYWxsYXNuZXdzLmNvbS9uZXdzL3B1YmxpYy1zYWZldHkvMjAyNC8wNy8xOS93aGF0LXRvLWtub3ctYWJvdXQtZmlyc3QtYmFwdGlzdC1kYWxsYXMtY2h1cmNoLXRoZS1zaXRlLW9mLWEtbWFqb3ItZmlyZS1vbi1mcmlkYXkv0gGaAWh0dHBzOi8vd3d3LmRhbGxhc25ld3MuY29tL25ld3MvcHVibGljLXNhZmV0eS8yMDI0LzA3LzE5L3doYXQtdG8ta25vdy1hYm91dC1maXJzdC1iYXB0aXN0LWRhbGxhcy1jaHVyY2gtdGhlLXNpdGUtb2YtYS1tYWpvci1maXJlLW9uLWZyaWRheS8_b3V0cHV0VHlwZT1hbXA?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
