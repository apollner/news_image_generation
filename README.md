# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Who is Telegram founder Pavel Durov — and why was he arrested?**

You can read more about it [here](https://news.google.com/rss/articles/CBMinAFBVV95cUxOc0daSFJmcDJPc1k5MU5HNG1MU0lyYVU3S2lyd1lVV1UwQi1QM3QwZ3NPZlRWZUlramR6UDhBNzV1NFIwOTJ2S0w5MXkxYnFqeV9RNEF0M0laaWdoLTdWRjNfd2JadmtvQjUyUEd3SUZFLUJoazdLNkNLUmJIWHFfSzFHTG5UaHFkNWlLcW9ObmllcDdtY3U3Z2RSUlnSAaIBQVVfeXFMT1RhWTdiWVJJT2dNVHpVRjhIQ0JVVHhkQ0xFSzA4ZGo1bDNmbHZRc0k3T1NfRVo3ajhjbUJ4WkpJeE9EeDFDS3h1VXoyaFU3WThESE1UYU9lMlFkRE83di1iNmFLRVlsZlFncDdhMkt2V0FLRk4tRXhsOUl5aEtlYzlmX2laVFljN05TbmNtd0ZZLWlxU0NsU1pJSG52ZXVGdFVB?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
