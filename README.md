# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Google Pixel 9 Pro and Pixel 9 Pro XL prices for the US leak - GSMArena.com news**

You can read more about it [here](https://news.google.com/rss/articles/CBMiogFBVV95cUxQalVxTTZhbkNXMVlubU1uY0V5ckxBUWhQSDNidlgxS1BfSy0tcnFMRlJrZ1FxenJ4a3pzTUI4S2hFUVRpUDNwMDNZMW1mNEJqMWVWZ05ESElhOFBZWkZfNGZPS1UxSlZrLVJXdkhzUE5fQ2ZvN010LU5IY0pnaGFZbHJQMWNESHg3ZDR3b2NRaUdLM0ZHRnFsS1VBVEt4dFNadHfSAZ4BQVVfeXFMTnB2MW0tUU9Ia1NGbnoxS0czaHg0LU9oWFlPMkZpWUpWdVk4Mno0M0gtcFc5VFowU2dZUnh5QnFramJ2Q2x5VUYtb0R6UHNpYjR0M0NVbUQxQmZScTdSc05iY0lOSjA0dVdnMlJ1YUlCYmNhZkJmU2kwOEhQZVNGY29aaXFxVDlSTlFYTFdYaU5wMi1pekQ3VzNaUzZONFE?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
