# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Trump campaign's use of Leonard Cohen's "Hallelujah" is "blasphemy," singer Rufus Wainwright says**

You can read more about it [here](https://news.google.com/rss/articles/CBMipAFBVV95cUxQUVExQWdjUktIRU5ZZ2NfZ1YwVVR2d0NubEtYanV6UWRaaHU5bllNekFfTmlDdUtoOWxmMFF4bjdzQm9UWC05bDB5V2NkZllOSU1nSTNFZHIzNnAyWEFhUjVVb09UdE5QN1J6X3JrdHJESnVMN0tPNURyVmd6bU95OFFqTlB2WWhYaGh0ZlYzVzBhdkE3RDZkVm95VVY1bVg0ZXhIZ9IBqgFBVV95cUxNYjZLV09aSkFtczFfNjIzd2kwUHBwdVBUaXVnTjBOelFhNjdOTnF3MUhQTWNadXVYaFk0c0ZhX1JXN1VScEdaRmlmWV9DSk11X2xGWGQyRVVJUngzd3ZabFFOV0VnNDBGOTI5NWtpc241SW9wRDduaEU0LXBvMDFWNHVDZ3paT0dZZllXSklwbFJWemsyVFJaUGRJWjJmSHk5QVVicWZweEpNQQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
