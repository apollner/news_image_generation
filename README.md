# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**UNC loses new QB Johnson to injury vs. Minnesota**

You can read more about it [here](https://news.google.com/rss/articles/CBMiqgFBVV95cUxQVUVaWW00QWVUYVlfMjB4eXNoMF85Ql8xNzNNSGdpNzgtTktOYWtwaTZsNlE5aHNFYWtyZ0dpbm1RVG1ENmlmZE0yb090MmFfd2gzWXlIRnphUVd6QWt5MWFyTEpPV0xsZ2hmYW9VR3k5R2laclpPdnZjdGk4eXljbnNESHJrMHJkdXNabGV1UHpUbUV0eWhMRFRrcEwyN3FpT2tFWkVVcVlDdw?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
