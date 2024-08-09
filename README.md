# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**UK antisemitic hate incidents surge in 2024, says charity**

You can read more about it [here](https://news.google.com/rss/articles/CBMiWkFVX3lxTE5lZFFHZ2VZSTdpbWNYWFJJb2I2N09pZ3Z4c3Z6X1Btal9HSXp4RHpTLXl6aDg4WXdJOUdZZTR5YzhtdXdhUVVNU3hSczNFY2h1R2Y1ZkJIcms2UdIBX0FVX3lxTE1TMEJnQU5TT2p2ZkhRd1pGM2VMRzR3VVZwR0JXMm5CUmRnRjVWXzVXd0ZEMmMxN0NzSS1ycVktNVE0XzNxRmV3VHRmV1pGa2M5NGx4UFFST0ViSlo1V3hr?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
