# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**‘Ketamine Queen’ Jasveen Sangha went on luxurious trip to Japan just days after Matthew Perry died**

You can read more about it [here](https://news.google.com/rss/articles/CBMivgFBVV95cUxNaHRNcFZwZ0MzSHAtY2FabGNzaEQ1OFA5dVBxWkR3NmVSR2xnbldKckc2NDNQTmNVYVNyXzRoTkxfbHFWeWppT2hrR3kxUkpWRzlDSjNiUTJBNWw5b3FPRXAzT0VCQzJlb2xYaE16RUd2TTFyTWZlVkVVY1lsTGpVQ3VhOFpJdV9mdDRjVS13aDB3R3RZa1YyTm1hMG9vWWpNOW5GVFV6UmJwdG1uMDRkUllxcDV1OU52VmwxVjJB?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
