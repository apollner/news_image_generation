# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**France: 'Massive attack' on fast train network**

You can read more about it [here](https://news.google.com/rss/articles/CBMiggFBVV95cUxOR0dZVHRlYVZ1V0wxanBHWVRYMFo1U1RCUFl6YUNiMUpsTEZZTEpmLWdIc2hvVlZrUjk4VHQ5eVJPYXg2Vkhhd3pvcEF2OHhiN2NOX2FpMDVtV2ZjZTd0Zkp2ZmRIdEVuZjZQTGxjeVZqQjkyWFlxWndCYTlJV0FNM2pB0gGCAUFVX3lxTFB6YUhLV0tKdFNjYVQxX2ZhNWxuTWF1LWZjOWY0MFI4YWFJWjRTdm5HREVPdHpfUDJnbU96OWxJQlpPU0NZRXN5Q096VXRoUUNfVVA4S2RWTHpmUVh5d2dSMFoyamRTcENvMmdoVTEtQ2gzUGg3WHdPSVJMb1JRMGtpYlE?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
