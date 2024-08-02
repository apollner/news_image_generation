# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Galaxy Z Fold 6 durability test hints at dust troubles, and it caught on fire too [Video]**

You can read more about it [here](https://news.google.com/rss/articles/CBMifEFVX3lxTE9DbVF1OGZmMjZ3Qm1BQS1td2lEaGl3ZjNWdllmLVdDTEl4R0VXM2VacWlIM2lSTmtTaGxDdzEzZEF0aXVQS0IwTldydXNLQ2hYSFdzMlZ4VHNOTEkxZEh5MFh2dV8xVEFzUXZhZEROMDJwV0lPbUdGTEZZMEo?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
