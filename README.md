# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**American Cole Hocker pulls Olympic shocker in men's 1,500, leaving Kerr and Ingebrigtsen behind**

You can read more about it [here](https://news.google.com/rss/articles/CBMipwFBVV95cUxNWENDbXRFcmVVSlEzTjNuLUVxT3U4OUJMOTR5TjV2dy1ISlJGRHVhQ1d6MGZxRmhmb2dIcVR3ZXViYVc5SVNGWHFLLU5MMG52UlJfU3NHTW1PVFlZOFlTRnl1ZmZsYnZObG5FRzduZ3R1Ym9WeHlOTXhFRWtPNWZGMlo5ZmJYc0NSTGE3RHZwUGVMUHhmYndmOHhNS3F1Yk8wd1pMcFplcw?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
