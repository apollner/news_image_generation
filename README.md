# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Rep. Nancy Mace says she was ‘physically accosted’ on Capitol grounds**

You can read more about it [here](https://news.google.com/rss/articles/CBMimgFBVV95cUxQNnRreG5xaEs4aWFZb1pTVGNlT3dhekYtQjJ0MGVieTBXY0U2dG9sYVUtb29VY2U4UDJxM1VpeUlQU25uLXJNdXpyMW5pS2lLLVRyMjRZSERFNzB6cTBJOWpsei11UTRxYWt0cjZYR0NJdnBvZmY2dFhmUE5vdTNMVlhxQUVCdHhOMzktV1A0dHFlRHMwb3dHTzBn0gGQAUFVX3lxTE9aQ0ZCRjR4X01XdUx4Y0dqcUlkRnNCVjZaZjl2eEtZbTlwMjExYW9RWTNqSGE0NERMc1k3V3h5QnVYc3luYzF1MjFrZkRqeHVTRlhpcVJ3OTRMZ2pFYU1lMWJMOG1Tc0UzT1NwVmU2ZTRmOGdfV0UxOWFFTkQyQmJYMzl1emk3R3pjV3Y2OTZBYQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
