# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Brandon Aiyuk trade rumors: Steelers in mix for 49ers WR; San Francisco asking for two No. 1 picks, per report**

You can read more about it [here](https://news.google.com/rss/articles/CBMi2gFBVV95cUxQZVhjNkFHZ3JiZ3FkOXk2SDJRNlk3eWM5RXZyNXJiSGVSNll0dW5lSzZCLVlxeGtkU1ZiR2U5M085ckJPSmpXeVRxbV9CRW5iTWRBSVFpa3ZaOFVkaEt4ZTFRVUxWQ1d2SHg4N0FRNEZDRjl3a1pFUzlvQjhwOHFRRTdSVnplcm5Jd0U0WEhCMTMtRW1RcUMtOEdMc2t4UlIyUFFzM1dIYk1BUzVLN2dWS2RpcEpnbDlKTHVIbVRpZlNGamNlYXpjaVpKa3VWdGFBdG9UZDdkZDhEQdIB3wFBVV95cUxNc3FWaVBETmFFYTA2OURDYkhtTEtvTGZrVUtmSFd0anlScmhyV2hEZldqTEJya0JKVjZOMDBGY1pUWGFNVFBUb0l6WDN2TTdCTHJuQlYwaEY4cGlsalFiME45ZXZ0Rm9qSWU2MjJlMFZJdHl0QzBYektKOThmQ2ZDLURvYnJLZ2VOdXRRVXRsQy1GUzhKdmNZRU5QaUhWNHFtcEpSVHJoU0IyQVdFZXY1MWJpQkpIQm1jVVZnQXVKajN6b1k3aVI2MWRGb0FMOWJueGo3MmVId01weEhsOU5N?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
