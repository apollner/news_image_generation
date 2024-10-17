# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**As Bills and Jets show Jerry Jones what ‘all in’ means, Cowboys owner grapples with team's uncertain outlook**

You can read more about it [here](https://news.google.com/rss/articles/CBMi3AFBVV95cUxQZkplMG0wMmFfMkJUd29HZXk1U3RZNHhuRldvUW96LVJlSUNOTEI0S0FkaUFObFU0N2cwM0p0YXRPNlJCQ3UxdmY4aEVMd1RMVjg0dlVWVXBhMEpfUEJaaUlPX1V4VmU5amdJUmdCNHBmbVBNUHR4ZXVZRERYYTZQWWcwQVZBcm5fTl8zX0FveUZsUUJlMU1XZHotbGVKc3JOemxIWkhuSzIwMGZiXzZKYjctb2VZRjBKRlBWSWpmTDFteE1xaFBXanktSmtPMmRmXzJTQ3NQbHFuNzJO?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
