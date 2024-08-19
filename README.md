# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Google Pixel 9 series hot take - GSMArena.com news**

You can read more about it [here](https://news.google.com/rss/articles/CBMiekFVX3lxTE54enN4U2p2QlhJWndUYnMtNjhkdDdvZHlYamZJWUNpTl9YQVA5ODk4U3BXR1hsS3VOczAtckM1OEpodFhBaU51czhNUXhGQVFFV2xMdkNic2tWeVFzc0Z1VUJ1RUhkM2FGZ3hhUnNZYllTc0VITjQxRmlB0gF2QVVfeXFMTjBOS1RFaWpPYjI2d1RBeHRVWGYtd0NsU3lXZmE0N1VUakFHR3pPM3B6MFU2RktKMnJBSFUzc1MycjRXYnlwSl9waV9KZkl5OVd0VmZpWXIyazg1MjlSMnlwS2Yzd25DMXJScS1adFNNbGNQZFhGdw?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
