# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Moon fests, moon movie and even a full moon mark 55th anniversary of Apollo 11 landing**

You can read more about it [here](https://news.google.com/rss/articles/CBMiYGh0dHBzOi8vd3d3LmNic25ld3MuY29tL25ld3MvbW9vbi1mZXN0cy1tb29uLW1vdmllLWZ1bGwtbW9vbi01NXRoLWFubml2ZXJzYXJ5LWFwb2xsby0xMS1sYW5kaW5nL9IBZGh0dHBzOi8vd3d3LmNic25ld3MuY29tL2FtcC9uZXdzL21vb24tZmVzdHMtbW9vbi1tb3ZpZS1mdWxsLW1vb24tNTV0aC1hbm5pdmVyc2FyeS1hcG9sbG8tMTEtbGFuZGluZy8?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
