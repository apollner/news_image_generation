# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Juventus 2-0 Man City (Dec 11, 2024) Game Analysis**

You can read more about it [here](https://news.google.com/rss/articles/CBMiX0FVX3lxTE1VejNVLVlfUTR1MFM0eUM3Zl9pbkM1bk9odERwRW9pWEVTMmgtX3NRTHI4M0RaaHY3RXpfSlZlS29XMVM3ZHhXMExJNmR2T1E5Vk85S1F1RlZJMHNZS3c4?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
