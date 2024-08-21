# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Morgan Stanley International chair among 6 missing after luxury yacht sinks in Sicily**

You can read more about it [here](https://news.google.com/rss/articles/CBMiqAFBVV95cUxQbzRmdmxNSFZrRmZHOW5zbkZGS09vSzJPNUFPSnkzZTlYZ3k2ZnNWQ1dSdlI2U0VuZUkwZTQ2azBuUUVkbkJVZGxaX3NsalJ4M1BEc2hXMUdlblM1WnlOZEFWMUpia2lrclZFY3ZBQVM4SklZcjA1V3JlUkZUeklubnVWNUdJS2FkWDFGQnYzRWhDMWlvQlphZ1JSVVppeUZlU3RJZlNLbzfSAa4BQVVfeXFMT1RnX2l0RkJQYmtSQU0tNFl5a2hmdC1TMFRKRHJROWVHX0tnakZJcGprbWdFYXRkYmtVNXMwc0dlbDVHNWtxYm9jMFh1WmVmbGFvQmNwZTQ5a3pZU3dwME85NU5vSmNxWHRJV1lCcWRlalc1VHp0Qm9BOXNjdlJHQTc0Y1BENENkbVJXckxWSDZZdTFTb2cxVUNqZWJhMjRRWEdodTFzTkFYNUhrQVFB?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
