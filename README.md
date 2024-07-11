# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Ex-Browns QB Bernie Kosar diagnosed with Parkinson's disease, also likely needs liver transplant**

You can read more about it [here](https://news.google.com/rss/articles/CBMihgFodHRwczovL3Nwb3J0cy55YWhvby5jb20vZXgtYnJvd25zLXFiLWJlcm5pZS1rb3Nhci1kaWFnbm9zZWQtd2l0aC1wYXJraW5zb25zLWRpc2Vhc2UtYWxzby1saWtlbHktbmVlZHMtbGl2ZXItdHJhbnNwbGFudC0wMzU0MjM1NjAuaHRtbNIBAA?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
