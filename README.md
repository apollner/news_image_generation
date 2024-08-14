# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Iran Hacked Roger Stone and Used His Email to Try and Breach Trump Campaign Staff**

You can read more about it [here](https://news.google.com/rss/articles/CBMiogFBVV95cUxOSUlaUEMtbzcwRDBzUXI5LXFOTGFVLW9RcEd2TkdySG1DVk8yRGctNlcwRXZGRXdzZmprT1E1WWQ0NXZvd0NaU2VVVEtXMDdXQjRHeWt5c2ZKN2oyd29QRF9DUjJsYU5HZWszV0NVSXZVTXNEZE5XQTNNS0ZXT0ZQemxFcFluTXFvMFk5Sy1ZeDlXRm1qN1k3ZkVPaFFtYUxTYXc?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
