# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Caitlin Clark makes more WNBA history in front of a record crowd as Indiana Fever down Atlanta Dream**

You can read more about it [here](https://news.google.com/rss/articles/CBMinAFBVV95cUxNcDdralVqaDhSaVdSVzhZNkFnRDNBVDB3dWNwTlUzeEVDekxzQlQ4M2gxaEFHdnpwZGJuLXpvV1RSZ1k3WXJDdWREN2dER19LbFpBdTk2LTRIVXdSWmtiR3FQaGFrS2Ntc3lhWU9RQnBXMlBCV2ZrU1JsZU1tcjVfUUlHXzdZWHFBUEh2WkI2ZmxmYWFNWnl1dGZZYU3SAZMBQVVfeXFMT1VCS1h6bUY3UTlXUkJ0S0lEZ0ZzUVJzNy1aNmpxYlJxcGxtOUo1NkJYUEkwaUFBeEQ0UWRQQjZyRERfT2lxb2hpaDJjT0NkV1o5eDNMNUw3ZWtLa0dTXzBzTnNDTkFza3RvNURfWU9JUHZTenJBUmVKcHZFUXk3eTU2MWlsR3RkUjhQRGFza1FzUkk4?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
