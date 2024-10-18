# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Liam Payne, former One Direction member, dead at 31**

You can read more about it [here](https://news.google.com/rss/articles/CBMijwFBVV95cUxOdXhTb010N1AtRG03T0I2bFIzdHhiWVh3LU5ZWnFUdUhoZkFLdUx3QUgxN3MyNzl0di1YZFRWMDhleVhGaFVCV1o3Q05lb01tTDJyODQ4RVlCM1Q0eFdXanpSZFFFMXVyVXhickJobG4wd0Y0eTM3UmdCcjV0aVN4dnFoQ01SVXV3WHhKMlc5MNIBhgFBVV95cUxOSUpXSEpuSFlkSGtSeTJ3MjNydFc1RnpkVjI3UTgzT3BNZjVhS2tQZGN1TEFENEE5ZnB2emNRdDYzTE56emU5bXdFTmpuZU1zQ1pQQ1h5aVZTNWotMklnUk9kLTAtMTJKb0toYUNnYlhZRXZiZ1NmdlAxQTV1RmlETWpuY29ZZw?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
