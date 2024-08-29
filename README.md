# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Ex-politician Robert Telles found guilty of murder in stabbing death of Las Vegas journalist**

You can read more about it [here](https://news.google.com/rss/articles/CBMiuAFBVV95cUxOYXRnTGl5NmsySjdvTXF4dzg1SmZoMkJOaFludlhiQmFlZUNRdlFfUHAySDZFU05pRGk4X1h6Z2k4c3BGbld3SVNFWnc0ekRSaGY2dWtidWFtN3lTcC0yZmNaY1oxTkRHcUoyQmFnYmRobVJZVGg4aTVXeEJyNHJZVzBKaUtyQXRNMlRxc3lJcTVUNkQ1S2xlLTR4S3c0NUtpWjRmeC1MV0RHM1ZfY3Y4ZHZCREFnUE8y0gFWQVVfeXFMUGhLaTlNcklmd2pDT1VjakVETHFYdTM0UncwOFhQRG9VSDk0a2ZQRThaaFZaRWNaMExCZ2puRE9MbFgxUFNrTmpLOWJiVG9OUjdNT2tfMXc?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
