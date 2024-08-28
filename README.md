# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Oasis Reunion: Liam and Noel Gallagher Announce First Concerts in Over 15 Years**

You can read more about it [here](https://news.google.com/rss/articles/CBMilAFBVV95cUxOV0pBWVRxN1RkZ0Jyem1LT3p6NXVjaVZSbGFxM1E0cmRBNE9IU1pyM0xlNUdILXZ2VWtGOWNzU2hJbm1DVWg5UVNFZlo3U1daTHBxSUNjbkNCUlJDN1RiLU5FZnZENXlGM1dNT1hVUlB5Wng4bWV1WGptOEs5NXVGZ2hVSTBxU1BwY3UtbUpjVkloNXZL0gGaAUFVX3lxTFBsbl9XNUo3Z1pmRy1SM2xJUWJMWG5QaUtoMXlQajkyRzRvam02NlRBMGpVemZFa1VBdEJJR19HelJhVkgwakwtS3VHa00zWU9nN29ib2Vmc2tmT0VnLU1yb2dZSnJxX2pITlh5Z0dOV1FRd1cybHhzYlN2YVlPbmpBUVUzanBkbmlXVlFRUUpfMzNKMFdPSUUtakE?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
