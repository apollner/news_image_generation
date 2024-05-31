# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Chris Hemsworth in Talks to Lead G.I. Joe-Transformers Crossover Movie for Paramount and Hasbro**

You can read more about it [here](https://news.google.com/rss/articles/CBMidGh0dHBzOi8vd3d3LmhvbGx5d29vZHJlcG9ydGVyLmNvbS9tb3ZpZXMvbW92aWUtbmV3cy9jaHJpcy1oZW1zd29ydGgtZy1pLWpvZS10cmFuc2Zvcm1lcnMtY3Jvc3NvdmVyLW1vdmllLTEyMzU5MTIxNjQv0gF4aHR0cHM6Ly93d3cuaG9sbHl3b29kcmVwb3J0ZXIuY29tL21vdmllcy9tb3ZpZS1uZXdzL2NocmlzLWhlbXN3b3J0aC1nLWktam9lLXRyYW5zZm9ybWVycy1jcm9zc292ZXItbW92aWUtMTIzNTkxMjE2NC9hbXAv?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
