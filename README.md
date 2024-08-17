# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Harris Plans to Ban Grocery ‘Price Gouging.’ What Does the Evidence Say?**

You can read more about it [here](https://news.google.com/rss/articles/CBMimgFBVV95cUxQTTN3RWY0amJjVldQWXpZcXdoR0V4WnhIb1g5ODFiUDRBUl9UWkRpNlE2UkdkemlBQmRfb3p1NWlwUG81N01pdVRlUmJBT3ZLQWhDaW9ZbFdoMGZ1aWI3ZWVpaVZnOGcwZ2lNWFJGeEExR1Bzc0xnSExDT3VhcDhmU25wMjZ5MFdVMnJXckdGajk0R0pQRU1BMkhn?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
