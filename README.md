# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Many dozens of Rohingya, including children, killed in drone attack while fleeing Myanmar, witnesses say**

You can read more about it [here](https://news.google.com/rss/articles/CBMixwFBVV95cUxOQWo2dVFLdEdvSzVuc1ItWE5ZWi1yaUpZZHFSZmlvWUV5VHJUYldiSWM1TFREX0JpMW5SNHMzNXhIRjlaMUladnFPR2wyRDU2cFBURHNteDhxQ1FjUE5vU1Q5TXEyZFJoRGJRaEcyVmJmVzM1LXdZSnNDSkw3UEs0OTdnNl9DQzc2TVlSd1RibThrUmNTX3RXckR3cmxfaU54eVllaUl4TUplQXlUbVgtbG1Sd0QtSUcxQWFGaDNBeDlwZ2l5VEZR?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
