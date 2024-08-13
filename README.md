# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**European leaders urge restraint amid expected Iran response towards Israel**

You can read more about it [here](https://news.google.com/rss/articles/CBMirgFBVV95cUxNV2pOb1lnZWUzMERvWGkwcmk5TUJNMWJUc3FzaWQzV3VkZElMdy1pV3pqZWNSeFJEU1pkV013bWNDZm9OVmVudWYwclB2eDhJM3ZFNUZDZjNudXBxS3dsLWhSMXJqWXZqblNVQ1psVXJxRS1HWW1nSm1DUWRyX1ducEpJVTFKZnBqN0hNRW9fZGdhS0FydmZmZzltSEZ0UXNpWmUwS2RJMTA3SGlYeHfSAbMBQVVfeXFMTzYwdUNua0VPVU9ycHlxOWxFbG9lU29mVXgtOWdWVThwVmpleXhhR1ZONFF6blFYMk5PMVhQdU9RT3ZNUC0xR3RpR0JYeFUzU1RuT3ZvWkNUbVYtWGZ0SF85OUZvMEROWjFuU2tfVm00LXNtYU5JUkhLY0VEOWliYThCUGdRVklEY3BqZC1kNG5pckg1ckZNc1liUUxUY1JMbzZfa0JrTlF3QlBPNGxQZ3VhQkU?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
