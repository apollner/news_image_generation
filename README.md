# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**San Francisco 49ers Ricky Pearsall released from hospital following shooting**

You can read more about it [here](https://news.google.com/rss/articles/CBMivAFBVV95cUxOLXZXRXpZdWV0OFJ1MkgxNHJYY2ZWU3MxaXFudnpVWEVrNnBCQkcwU0ZhcTNTMk5PbnZpeUlPQ3dZOWFzRUVMdnRYUmh2bTQwT003VWVMQ0MtSWpUYU1oWFhDZEVrWTA1X1FvLUVkYUlGQlhEc2NZQVBnMzd2bk80V0Y5TGI0cjI2TkFDOVgzRFNEY1FNaE5fdHFTZDZyR0JYOWdiay1KZWt0VjBZUk9XREc2eDdLWFlRSDFCZ9IBwgFBVV95cUxPdkJ1dUFGSVoza2NTNFVPTTdoS0dVak5HODlOWWdjVEljQVdZWW1uRi16QW9PWjBVMERGMGhrSEMzeVBwZktrb2JPckwzS0FMZ090cURVTS1UZkc2cVQ1S29GQ2RDdFBvTkt5UVNqV3hqTHAxZEplUVVxN1pBaXY2a2RxaEc2bmxHYlJoU3h1UGcxTDg0WFFkM3JjNmtnQWZvYlB2SGNLVzhlZDNpaTEyMW82RGVRYmZubjRqbmhnZ094QQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
