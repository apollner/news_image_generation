# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Patrick Mahomes Says Travis Kelce Finally Grew His Hair Out Thanks to Taylor Swift’s Influence**

You can read more about it [here](https://news.google.com/rss/articles/CBMiswFBVV95cUxQUTk3LXFvcmZwVG9rR3RvMTNpR1FCQzFFVjlmcS14OUc1S0s5bFZEQWN0ZXE3T3o3NGxjU1RnalR6TWNMR2VUejl2SzFJX3JUU19aQ055b18wZlVORUZMbmRXTHFMVXgxYmtCV0laVnBHV0luSjNDdEtBLWtzRWVxZFJwOXdyQy12c3dhNUpHamJuUkhqRWswUHVraTN5YTN1YkRRZFFnWFI1ZUVrZXFYbE04VQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
