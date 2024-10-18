# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Bird flu concerns mount as California reports more human cases**

You can read more about it [here](https://news.google.com/rss/articles/CBMilAFBVV95cUxPcnZlWTFfbS1Rb29DaUc4dFNwZXpfZ2FyOGUzbmxqNDN1ZFBRVmtteGF3bU9HcXRVTjVSYnkxWmFRc0hQRTlhenVkRFVSLTgybTNYMmpSRTl2Y0t6WUcxYlNQV0xuaml4cG1GcFloeXFRQmlhLVRUbXJiM1JWSlBkWTAyZ2dzYUVNZXRBLVRmU2paQWRk0gGaAUFVX3lxTE9uT1RkNFR4VTF4WHl4MkVPUUdFMWZFT1JveHppRGd2aDBVMDBIeXUxeUc2RS0weVAzZlh3ejU3Q0RxWmlONUxCV014UXo5ckVTcDhvTlJnLWw0dDVXS0tNUFYwX3dpUXNJM1diOHFOTFB0LUZmMzJuNzFtMloyTm9TWlhSeDFPeFo0TG5xOHlycU1ndmpaOFJGeWc?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
