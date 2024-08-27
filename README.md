# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Oil prices to remain elevated as Middle East tensions threaten a wider conflict, CBA analyst warns**

You can read more about it [here](https://news.google.com/rss/articles/CBMirgFBVV95cUxNT05uSXk2cEVLZGFDendQOFpCb3lnWVJ6aTJEWnpHal9KQXJnSXZHaVZMRFdOeVZIRjF2Q2Rqd25qc3N5TGoySEZEX2VmX1I4a05IRjk5d0M4a1NDaVVVYXdmYm9FR0hWZ3FUV0g3bHNOeEhCM3NMY0RIQjczYXRwYk5keWF0NG9DZ2dwNVlPYXBKdHpyT3J3TG1jODNnc0xmcFRDX0JkenZna3BJMmfSAbMBQVVfeXFMUDJCS0Y1RFpEYzJsWG1oTllYUk5GYy1lQ3Y3ZHBkRHRUVGtPLU4ySUVTd1lVOUgwam40Sl9vSjZmb2tUNGlra1Jabi1LUTIxTkNoLUNiSHkwemxnSGxSM050Q25Sa0FBbV83UFN2enRoU3dxQnZiM1ltNV9ObEM1anUyaUg2SXVDVEpJd1R1ckdEMHpoZUdnUElkcTJlQWlTQmhTaXJVUFRzcW1xQVNzQjR2NkU?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
