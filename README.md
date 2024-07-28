# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Fox News Poll: Close races in battleground states show voters locked in**

You can read more about it [here](https://news.google.com/rss/articles/CBMiZ2h0dHBzOi8vd3d3LmZveG5ld3MuY29tL29mZmljaWFsLXBvbGxzL2ZveC1uZXdzLXBvbGwtY2xvc2UtcmFjZXMtYmF0dGxlZ3JvdW5kLXN0YXRlcy1zaG93LXZvdGVycy1sb2NrZWTSAWtodHRwczovL3d3dy5mb3huZXdzLmNvbS9vZmZpY2lhbC1wb2xscy9mb3gtbmV3cy1wb2xsLWNsb3NlLXJhY2VzLWJhdHRsZWdyb3VuZC1zdGF0ZXMtc2hvdy12b3RlcnMtbG9ja2VkLmFtcA?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
