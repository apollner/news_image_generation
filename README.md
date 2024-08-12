# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**2024 Paris Olympics: 'America-made' Emma Hayes reignites USWNT's flame to earn gold medal ahead of schedule**

You can read more about it [here](https://news.google.com/rss/articles/CBMi3AFBVV95cUxNYUt0cjVRMUljWjR1Q1phZUlRNUVUVk45d2U3S0xOekZvZFF1UHVvTlJDSjdQTGloRHFjWG9UTDJJYVNEdks3ZG5aWHRjOGNpU3U0Mmo5VFhLaFllUFB2OE8xdlpTa3lYRjVNN0ROb2FMdEJaYkxWdmpwaHlfMlE4SmZWVVNHeE91dWxPQnRLcjVFelRnVFBMQUoyYU1GYkpsdzc3dUNmX1NreGtLRGEzSEJyVjlRblZ5MW9Mb0V5VlBrQnFzMEhHTTVDV2RNTmpRdC1ya1ZCMXhBME9X0gHiAUFVX3lxTE9VcWpTdWphMHpvRThLX3hLc2NfRFo3emk1Z1Bsa2NFcDc1b0JEQTlnMWp6eWpQaXc5NXREdTJTMXJHNjVsRlktVG5vR2c4eFFxN212QU1uRUtWT3JyRDlPR2dkR0tJVXBLY2loYnh3UUdCOTdfcmtQaEltUnA4dEtiSmlDRXNYSXFCeGVJUGF0N1EwUVBnekstQVR1a1NSd1JKajg0dWFwZl9RbWZJZHY0VzlKWlRpMFNMZThCMUllTEJwU185c0xZWWJCV2ctRi05OFBSMFIwNlpOU1FhanJCZlE?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
