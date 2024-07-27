# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Harris says she won’t be ‘silent’ on Gaza suffering after Netanyahu meeting**

You can read more about it [here](https://news.google.com/rss/articles/CBMiswFBVV95cUxQYmtuelRmZklrTlV6RGVkSkp4T0NWOHktLTdZeFAwQXQ5aVRsTGM4T2NoV0x4V2RTelBpTy1kQU9nN0wyeHA2NElJcnplQXgxOFVMcmliTVVrQ0huRmdfYUFDSGpvRkRTc2kzRzVfd0NyZGlRQk41NG5rZUlqdFJxc0FKQmwyQ1FzRVc2dUpfblRST24ydkY5ZU5TcVJQWllDb0w4OUEwSV81bGtVbnBPZjhVONIBuAFBVV95cUxNQm1rUEtEaDBDM1FONDNhZVp3TUZOemplR1JTcGJjYXFLemhLem50YlRhVkExUU4wRlJSNHZ4MWlfalBqTlZ5RHVOblZULVlqMm1wSE5IRUJGQzdtbGx0M3FKUS10U3RmbGN5TFpsV2p3bU1fVDBuRV9pbnJPMmJWajZGRzgzQm9YLThNSzlCc2NrWm15TEphaURUTjVIcTRKQUgxZXZXQlJJUExEdUZ4cXZFSy11Q0kt?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
