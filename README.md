# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Nokia shares slide 8% after posting lowest quarterly net sales figure since 2015**

You can read more about it [here](https://news.google.com/rss/articles/CBMiZWh0dHBzOi8vd3d3LmNuYmMuY29tLzIwMjQvMDcvMTgvbm9raWEtc2hhcmVzLXNsaWRlLWFmdGVyLXBvc3Rpbmctd2Vhay1xdWFydGVybHktbmV0LXNhbGVzLWZpZ3VyZS5odG1s0gFpaHR0cHM6Ly93d3cuY25iYy5jb20vYW1wLzIwMjQvMDcvMTgvbm9raWEtc2hhcmVzLXNsaWRlLWFmdGVyLXBvc3Rpbmctd2Vhay1xdWFydGVybHktbmV0LXNhbGVzLWZpZ3VyZS5odG1s?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
