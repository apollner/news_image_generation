# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Attack at beach hotel by al Qaeda-linked group kills at least 32 in Somalia**

You can read more about it [here](https://news.google.com/rss/articles/CBMigAFBVV95cUxOVHRvNERjaTlXSV9SVmhKYXVDa0FXa0dETHNMTEM4b0tScEtaZmlHV1d6bVMxQzBTSDVJT2Q4d0tQRm5WN2kwRVI3WHE3dGczaXF5NTJ3U2hXSnZGWTZSQXNjYU9DNlFrUjFRUjBJTkw3dHN4bHNXZGp0bGFoOS10LdIBhgFBVV95cUxNZ0ppV0VZQVlFdEhVMmxEQXpFWHRaRzJxWUZGNzNQUFhPdGw1Y1o1UTh2UmhXNVJob2NJNHRCSWthUUw4cHRwYVhncDZNcE55U3p3V0U4ZXFraGlTNlB6Y1F2alA1R1RreHNFZmMtQWl4V0w3aHZLcWthUkkwQUJhWlVxNEdqdw?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
