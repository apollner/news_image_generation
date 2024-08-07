# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Dow rallies 500 points as Wall Street rebound gains steam: Live updates**

You can read more about it [here](https://news.google.com/rss/articles/CBMid0FVX3lxTE5KV2NObVg4WC1scnA0WFJOMV9DOWZJWGtHSXowcUtjTWt1WFVXVDBZNXYyanFiMEtoc3VBTWQzVlFCcjlqa2tRX0U2akdaRlUwbjZvWldVS3lhcFVtdUhkTkxmcEVYRktVaEZ3RjR1bGZoUmtudmY00gF8QVVfeXFMTnQ2M2VJdEtrLVFHNTV4andUT3E2X09oRXc4WGJ2YlZHVXE2N19QbnAybjFjeTVsWUlPNzVqSmxpUU92aVVEQUgyVjJYYnV4S1hjOVdkOWo4R3dwb1NwdjQyV0dSbUZ3WWxqNG0xRXJ2aUlRQjd3LWo2eXZLSg?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
