# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Weekly poll results: the Samsung Galaxy Z Fold6 and Z Flip6 are too pricey - GSMArena.com news**

You can read more about it [here](https://news.google.com/rss/articles/CBMicWh0dHBzOi8vd3d3LmdzbWFyZW5hLmNvbS93ZWVrbHlfcG9sbF9yZXN1bHRzX3RoZV9zYW1zdW5nX2dhbGF4eV96X2ZvbGQ2X2FuZF96X2ZsaXA2X2FyZV90b29fcHJpY2V5LW5ld3MtNjM3NjYucGhw0gFuaHR0cHM6Ly9tLmdzbWFyZW5hLmNvbS93ZWVrbHlfcG9sbF9yZXN1bHRzX3RoZV9zYW1zdW5nX2dhbGF4eV96X2ZvbGQ2X2FuZF96X2ZsaXA2X2FyZV90b29fcHJpY2V5LWFtcC02Mzc2Ni5waHA?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
