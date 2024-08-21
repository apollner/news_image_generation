# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Hillary Clinton tells DNC that Harris will break ‘hardest glass ceiling’**

You can read more about it [here](https://news.google.com/rss/articles/CBMihgFBVV95cUxPSGRWbEVVUVFaNGJQMWdqQ2FRWURwRGt3NWxaMjNjeV85Q0g0d3otNll6Vm9WeE1lZ0E4Q3ZfZUd1d3RvMzVCa0ozbExqV0F4cVlwdE81N29uWFMwRmw0aG9uN2xic25OZEwtdXY4MjF1bDJGenM3R0VGVlF3dHZRTzB2cDU2Zw?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
