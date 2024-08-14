# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**‘I got it in mint’: Young people are dumping Apple for the Galaxy Z Flip6. Should you?**

You can read more about it [here](https://news.google.com/rss/articles/CBMibkFVX3lxTE1UbW1jUy1qWlFmaUt0NTVMbmJBVlZtaEl5VmV2b29ndXMyY0kzOWFYQUV1UXhMYUdWWTY4NU9pakJVaC15QThFZERxeVRfTlJla2UwU09vS0RqM1hPSVdDM3JyeVdYazhkbDhVNEtR0gFzQVVfeXFMTXhNQmxtYjlOZXF0NEhWZnNXbk1LS3Y1dG9MbVdrdkUxeXZCZ19mV1FsTGtKZno2bVRJUUh2VzRnYXlhVFNleElScVV3U0FHNVVTVWJBNDFDNWk5RTdCUEFxZHpvV1JKUmpZZVNESHVCb25ZYw?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
