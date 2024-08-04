# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Stock markets plunge as weak US jobs fuel fears**

You can read more about it [here](https://news.google.com/rss/articles/CBMiWkFVX3lxTFBvZjFBVzUxTU5qN2JTMDl0NFI1X2QwU0NkZGJ5bXg5R0V5dEl6N3lqSGd4dFdIY1VTbUZFeHgtVy1wbFl4MVo1N2lXSnFsbDV3cnRzaW1uTjBhd9IBX0FVX3lxTE1YRjYxMG9Ia3RaYTZqMlVMWTZEeW14cnhZZS1EbmlDUjctRmhzSjh5aldTWEhHVkFEc091eHFQbW5VMXRUX1lXY3RHX1g1VmlUTlNEZDJUSlJ6T295TEtR?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
