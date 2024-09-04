# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Netanyahu defiant as protesters demanding a ceasefire-for-hostages deal bring Israel to a halt**

You can read more about it [here](https://news.google.com/rss/articles/CBMinAFBVV95cUxQZE5ZeW5lQUtTVU9ScnhZSENfR1FCcmZONFFVWVY1SWxoQk9xN1BtTmh2RWFJcm5wODFiZm5HeGtpY1pkNHhvNDN5XzFfRHdGdTF3ai1DUER4czBKU2hjNEtGR2NYX21BOHdGOUVvVFBnNFdPT0hRU1JacDhUMFV6TXo2TENocjJ6Z1dPbEhJclNYcXE1Smh4dHZTR1jSAZMBQVVfeXFMTXVwNVFNaURGNDFxV1B1OHNyYV9OZnB4NmJ1SXM3SzFLN3ZHOUp3X2MwbS1hWDlpRExfZzlES0tVYUVGamtZNFNRS0w3OEJ4c2lycTg3YkRxOXRPZDVqNGZQSnlnY3Nwd3FDZXNmeUIxdXFmajhBUHgyZGVfc3JRdnk2cWcyOExEcDg4dzAzQ210UHVJ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
