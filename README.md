# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**FDA declines to approve novel MDMA therapy to treat PTSD, with request for more trial data**

You can read more about it [here](https://news.google.com/rss/articles/CBMie0FVX3lxTFBkczR2V0YyVUhFTnBQcVR6X2Vac3RPTldDMFVReEhtaXc5cDVfYklpNmVlbTc3YWhfTklyNmlyYm5EOXplNkJNSmtESjRMRVZMYzA2M1VxcG9DVmdLaVQxV3BkRmNqdjNObFY5ZTh2NnczRFRtRFhGQkhvMNIBckFVX3lxTE42OTRiZ3JfalhtSW42RVFDXzYyNHVLYmJFd211Ny00Rnp0aTZEQzdqNl91RUl0SjJKYzJnUXRwZk13bURxcEZSY29adi1kX3F6NlBvcmYteDBsNmd1NUFoaXJCWDN4QUhHTWZNZnVtVFVqQQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
