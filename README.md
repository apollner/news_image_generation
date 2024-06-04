# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Japan’s car safety scandal deepens, as Toyota halts sale of 3 car models**

You can read more about it [here](https://news.google.com/rss/articles/CBMinAFodHRwczovL3d3dy5zY21wLmNvbS9uZXdzL2FzaWEvZWFzdC1hc2lhL2FydGljbGUvMzI2NTE3MS9qYXBhbnMtY2FyLXNhZmV0eS1zY2FuZGFsLWRlZXBlbnMtdG95b3RhLWhhbHRzLXNhbGUtMy1jYXItbW9kZWxzLWhvbmRhLW1hemRhLXlhbWFoYS1hbmQtc3V6dWtpLWFsc2_SAZwBaHR0cHM6Ly9hbXAuc2NtcC5jb20vbmV3cy9hc2lhL2Vhc3QtYXNpYS9hcnRpY2xlLzMyNjUxNzEvamFwYW5zLWNhci1zYWZldHktc2NhbmRhbC1kZWVwZW5zLXRveW90YS1oYWx0cy1zYWxlLTMtY2FyLW1vZGVscy1ob25kYS1tYXpkYS15YW1haGEtYW5kLXN1enVraS1hbHNv?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
