# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Trump indicates he is open to RFK Jr’s proposal to ban vaccines if elected**

You can read more about it [here](https://news.google.com/rss/articles/CBMikAFBVV95cUxQcWxqdGQ2LU95RWFhT256V09wN3JSblBTaFNsdFlBVko1NjYzLVdvR2YxRUFRbll4amF5Q21hSnYyWEIyYUE4SnR4N19JQV8yNVEyQTI2TFZ5NmNmRlZTNUhHUUNLazdXbDlYcHVfOGZyMEtnUmFtS0tKSFFnSlFzZk03eEJnT2h4WFRXNjNxZDTSAZABQVVfeXFMT2oyVlpOYkpkMXRwck5aelM2V2ZLc3QwLUNGM3JvM216QkpZekVyTWtIZksySVRGWXNBRXZESVE4aXlwRjJxV3FnQjVfQWpMUDRGY3pmQnNxb0xxVTIxX0xzZEp1RktXcEdmUllqVF9QRGhxd215ajNGcDZrQ3E1S2F0NDZBY0N0WTVpQzAzaWVN?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
