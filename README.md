# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Disney pulls ABC, ESPN and other channels from DirecTV in carriage standoff**

You can read more about it [here](https://news.google.com/rss/articles/CBMiwwFBVV95cUxOV0JsbGhjSklWcWpuUjJyRGZWcjdwTk0zZmp5RThKMzdnNnJJS01zWU4tSDBOa1k1VmxZelVNenBtamFQR1lFYUFuQnlLWVF5R1JDZlZnQnJqaUVPaEN1VWRHVjAyOC16dVZFdVJBcU5CNjh1ZktCY1NfdzBoRDBNbW9kV0hCdXcwbEgwREdfUDdHc2dmaUNDN09MZmk1SUhkVTFFdjl2ODFxdG5BeWg3cUp3SmJ2TGNPTUhSeHBPdW9LcWPSAboBQVVfeXFMT29kdUZwUC1UZ2R1dC1yTGh3NWQ5cWdWejdiVFlrSnp1ZmhxbndMaXFDSkZRTF81c1FqRGc3cGhVV0U4SDBxMlBkN0wxUlpwSWNVTWlRbDB0SEZWVW9fMWs4U3NldTF2dUNIcW5KSEhselRRZXFLNGVlVXRBUHZTMFZaTDRMVHJNVk5rT0dWaXZlRG1mZV84VUhnb1AyVDE4bUxzZ1cwUW9kNFpqTmNBcHVhVjl3d2p6SmZn?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
