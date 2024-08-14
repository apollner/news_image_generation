# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Teenager wearing a helmet and bulletproof vest randomly stabs 5 people at a cafe in Turkey**

You can read more about it [here](https://news.google.com/rss/articles/CBMinwFBVV95cUxPZzRfTm1HUFZjVVg1Ui1GWXhYcU1Sd3FuMkFvbVd6UW9fSWxlbEZNdGhMbG9QeTQ5XzhwQ24za041alJnMVhPb3g2U1Z2Qk42WFhRLUUzcVM5YkliWmkxcnF1cVVoYzhSbDF5SEl1bkZpMlVUQVdHRFZ4NC1BY1NQQkxhX1duVWVGU2FFQV9SNk5mN0hJOHF5SGk1ZTBPMmM?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
