# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Stock futures rise slightly after S&P 500 notches best week of the year: Live updates**

You can read more about it [here](https://news.google.com/rss/articles/CBMid0FVX3lxTE1tWm91all0ZDJqYlppd3VPa0hBWlk5RGlIcEhLeWpOTnhhZHlSV2V0Ulc5T3lGUUExMXJGMEh0NlJtb01Tc2tCR3VvQkpqcDlGbFRXTk94VERqNmNXWnZBejJLLWJkZ0VQZm9vQWFHUW5KWEtUWUFv0gF8QVVfeXFMUHItUmhBTE5faS05cHI0ZERiWUdhQlZnM3lwbHpBamJCeG1FUTNVeWlpYnVKckFyU21XWmZ3N2tKdy1UWGkwOG81cllUaHFId2VGS19YT1o5MzBIak11SndkWnl5X0lQc3owd0Nzejh2R1VrNS03U3oxb0w2YQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
