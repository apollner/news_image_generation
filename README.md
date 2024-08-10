# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**U.S., Egypt and Qatar call for "urgent talks" next week to reach Israel-Hamas cease-fire deal**

You can read more about it [here](https://news.google.com/rss/articles/CBMinwFBVV95cUxPdjlnOUlVZm5YMl9IaS1iRko3UkY4dDE0bUdJaWhXMzh2NFZ6R2hRc1VKSTBNMGowSWNPbXpTZTBTUVdqaHpRN2VQTDE4eTVLTC13MzczR3lRc2NKWkFuQ29KWWdjUnlRc0NOeFMxWkszeC1tQnpLUnFCUDI2UlZKMk1xTTdaZE9DOEEwVzJ3TkctYm82T3dTSFNLYWR0elHSAaQBQVVfeXFMTmxmYjhYRXRNdVRxanc3bkw5Wm5HV1JLUHhScW1DbTNiZ0duWXhnSDgzc2FHUEtCTDItUVZzZWNnVG5UTE4tSDVCX2ZGQXVwajdjTjY2U1JTdkdpMGlwQ0Q1WGJUTEFFUkdaQmtma2ZtazFOR1dOUUhKNFM3Ml9yekMxNWlFTkpwQTlYaDZkMTU3LVhvQy1sOUpMS3BoMy1BUk1MY28?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
