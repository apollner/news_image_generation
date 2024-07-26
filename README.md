# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Kevin Feige Explains Why Marvel Spoiled Dafne Keen’s X-23 Return in Final ‘Deadpool & Wolverine’ Trailer**

You can read more about it [here](https://news.google.com/rss/articles/CBMizAFBVV95cUxQM0c4SnlNTTI1Y2NOSmotNVhQS1NxSmlJNzFvbGJrU0RmOXRXLTk1TkZaVTNiVFo1dmF4LVRXRkJHVkdwanppeFRhR2doNXBDOVZ2M3ZnRC1ON0prdHJZYks3OXhDRzRKN2hWUUdvTlprbllfYndNSG41b1hPV09fLXJfN2xaX3pJM3hxZ3V4UGJMdHV6eXhkT08zVndXYW85T2J5X2tfdm81U0NLbUFHVEdlZ3ExNzBPMzkxMjV1bGp3QmZnaXRacEdLbG0?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
