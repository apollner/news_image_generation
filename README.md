# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Trump says he’d create a government efficiency commission led by Elon Musk**

You can read more about it [here](https://news.google.com/rss/articles/CBMitgFBVV95cUxNVFJxR1A4MEVZS2VCLVB6T3RCWkhNZ3g3ckdROEN3Zld5Z0RLcmo1SkJJOFdTdnloOFV1aTU4WkdOMXNxOXVEaGVPWE1TUE0tdy1LTzBLQUF5UWI1b04xOGhsNk1GR0I3NUd5TGdLaTA0aE1QaE04VHJ4ZUNZM2o3SlpObG1fSE1MbnQ5UTlsdVlVQzZ0VnR2akRRTC15ZXBJM2tNVXQyUVNwYWZmSjlYbUNLVjlOdw?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
