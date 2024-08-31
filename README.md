# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Nicole Kidman Says Erotic Thriller ‘Babygirl’ Was ‘Very Freeing’ to Make: ‘I Didn’t Feel Exploited’**

You can read more about it [here](https://news.google.com/rss/articles/CBMiuwFBVV95cUxQMEVWNDRqTFNTaW1lN3AxYzl5MjV5aUZPNGFNZ05RenJSdHQ1VnRFdERHOUFBbU1PeElOaC01MURKTzNJUzFQbl9IV19iczBHeHpycDJYZ2xWYzB5N3VPSlMxNUl2X1hxU1hESzRaVXBHU21hRmpTUWZpejBDbW1aeXV2UVdPRTF3STB3V2hKVjM5TVIxRW42Mmc1OUp4SWJmM25tYzZsRXZqWlpWR2d6WW1jSnBUSlNYczV3?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
