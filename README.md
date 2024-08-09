# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Zero calorie sweetener linked to blood clots and risk of heart disease, study finds**

You can read more about it [here](https://news.google.com/rss/articles/CBMiiwFBVV95cUxNaGFnRVFPN3BGalpqeEMtVEpKQzR0R2VyaVo2RkZJakpMajdQc0YzalhwWXRKSU1oZElTOUdaeFdycjRrMmVNUkd6OGtnUU84REwtbnh4VFZqQzdnNzR3U0NDQ0hXbEs2dEdCekVydHA1Z1hndkhKdHROU3RRUERXNDBrc1Itamc3cERj0gGCAUFVX3lxTFBHb0E3elYyenZXOUVNckF3RzdBVkVaZ0R6bzNmQnlndGV0TDFCY1pSOVJCNzJ2VTFZZVRIZ0Jwc2wyVDVKdm5LTmZJXzlBX1Vva0EyWEZ3MGNWYUQ2OXJxNDVlaS1CR1ZnRWNiSzlYekpZa3FYbUZRYWxuRlRtR2hCc2c?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
