# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**2024-25 NBA schedule release: Knicks-Celtics on opening night, Lakers-Warriors highlight of Christmas slate**

You can read more about it [here](https://news.google.com/rss/articles/CBMi2AFBVV95cUxPNk5SSTEwbncyYWJOdXhWMTVCel9idUg4WlFFaEpFd05pbU9KNm50cldCUGppdTF1WENsZHBETzlieEtiTzZtNjdGRi1ySTd0MXBCdHR4S3hGMG5TeHNiUWxIME1WNnJ4Mm9McnowLWNtZ3NpYmxnYTRLZjFzUFpKU3NtSkF4YUpSc2dwM2cwcDdKMERENDc1eVgtNUpBZE8wNjNHUVlJRUdQeG1JNjByQTB1dTdzam5HQm1ONGdkR0FzaFlZRlpXbWNZdjBjMG9DQV9NODhwRTTSAd4BQVVfeXFMT1djVkY4SjIxVU1ZemYwSHBpWlJBYnRoUXlZZXh5enhqZlV2N09SSndGM09kS2lPd1lQQnM5TmU2bTBYUG1pUzhPamJqRkpNREhSTnpuZmJTY2t5THpZczVaV1ZvT0NOWFltMERKVDZfbFVfMFBVcUk4anR1dWRZQmtuWVAtY21kUzhIdnpyajlqd0MyeExmZGxMVDh1R2lEYUVyeUY0STdyaU1NdXFzREJrdmliV3AyNUV5bVA1ZlpNX2gwVjk5Qk5SdFVuUjhVRC0taDJVYU1PWjlDVTB3?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
