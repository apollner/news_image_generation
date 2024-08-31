# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Trump v Harris live: Harris bats away Trump’s ‘turning Black’ remark in CNN interview**

You can read more about it [here](https://news.google.com/rss/articles/CBMiwgFBVV95cUxQV3pWQXdRSTNXdVlMNXhaTUV5eGxBN2ZodU16Rko0ZkcxU0REMzNLN215eXZzUW5oeHg3ZHBqUXVYRGpfaE1RdXp2M3FOVFRWN2RFZmVHVXN6V2hDNzhFRW5DdUVlelBwNzhmY19ZbjY5N3pkMHNidEVlSWZxZmFTNjZ6aWUzdndiRVZXN1BRMk5ESUY5MHJPTGFCX0ZSMVhxWUc4OEU3RUp3Z0VQQU5LUzZ1Mld2UUVMdkFMLW0zU3UxZw?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
