# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**A really big shark got gobbled up by another, massive shark in 1st known case of its kind**

You can read more about it [here](https://news.google.com/rss/articles/CBMiywFBVV95cUxPMUFDT2x2MkV5eElGeGNZQXV4TjVXczdIbFVNWW9VUWNtVWVKVTg2eFl2M0xncEJCUjhfdDd5Z0EtTkRNV2xVR1pwdEtxS3J3bVlOc0N4RU1lNnhyeUFxYUNKdzNHRUt4NERwQklUY0VtRFFDblZCU0hwZm1OZHRNNWdLMDB6QU5aNW1BZUpyeGYtNmNRU29hSVpLMXJnZk5mazlRQXhrbm15TnhiZVhvT2U3TG5PRW1XSDgza2p1TjB4RkRqUVdrbnRaaw?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
