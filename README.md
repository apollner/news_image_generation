# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Rivian tops Wall Street's second-quarter expectations amid cost cuts**

You can read more about it [here](https://news.google.com/rss/articles/CBMiqAFBVV95cUxQd0dEZndBWkJsbXFROFEwTE9SUDFqams4d3pXdkNlbU1OLW1UUGRsM0lpVGNHR1FzVXJpQ3hiVF9ubk53eXFnZWhMeVg5enZHWXlrUTl5SDdDb0JrcXNTWTBqUFdoS1ZpbTRiaU5YNW83QktPVUdkUnVPbkF6N3BtenRhTHR3MW5HbUF0WmREMmh4b2lFMHg3MEJTb0RZS3c4YUhEWTh2NUbSAa4BQVVfeXFMTUdpNWRQNXRiWjZEN2R5NG5NcW9OV1A3REdCQUlJZWpJN0FMTW9PNTl5NERlelhXdzJ5SWVOTEs4RzZiZlBId2dpUkp3QnUtVmUySTNrVUhqYmdiSFJKVEFKMVBHOU1qWDhUNm9zZExjNkhGbUwxMXhZcWNqUWZVa1c4MHhEb0tFcUx2dW9PXzdJNkcxMnFfNnE2QllKd19aNXNpMVpRZ3VUMTJ3Y01R?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
