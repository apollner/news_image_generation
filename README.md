# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**European Central Bank set for first back-to-back interest rate cut in 13 years**

You can read more about it [here](https://news.google.com/rss/articles/CBMif0FVX3lxTE91LS0zS2M0NXpnS242a01CUE9VWm5lamI3QkhpM0RpM2FfcjlLVzhlSnRoUUpjLU9sblZZX2hUTDRCV3NGUWliNmFsVFRUMFdKeFVKVUNCWGg3OU03Slp3UmF0Vy1pV3pBa1RtT3hGTy05QTJfdjVUX0dsUHJuZFHSAYQBQVVfeXFMTkVTRVh6R0haakgybDBsU19xWUlZajIxeTR5RmZZbFB2QnlFdHczRTZZcTBDZlhCYW9GY1pXc3Y3SmdGdjVzaVdELVVVUGJ2OXVuS0o4Yk5Kbkt4QmZtSXVwaVNOX2llenlDem4wZE9iRzRyTmN3WWZ3VU5KY3FfM2c2ZUsx?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
