# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Paris Olympics gymnastics live updates: Suni Lee earns bronze on bars as apparatus finals continue**

You can read more about it [here](https://news.google.com/rss/articles/CBMi5AFBVV95cUxNMnRuVmFiTDhqbDJvbFVfeGYtNnpCZndOd0QxOG1aclZJNnBIZDUtOFVYSkJMWGdzRklPWHNldUdETUp0dUZyYll4THFJMHpQTDFfVGUzZVZlckJvYVFuS05fcVBZY0FGT2dpd05HOXBjdUd5Yjh0dGZnVTZHNmVwc0RJWDlBTm53Ym5fMFBNQTVEc2tVTDZ3a1dMdHpkX256bFlNeFZFeW5pZGJaT3gydzlyLVBVR2s1TE4xOTRQLW5LWTZWU2hXN1BOQy1KOU9XM1NlWGFRd2dxMzJ5ZGNUaFc5WFU?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
