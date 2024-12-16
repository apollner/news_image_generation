# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Veteran analyst who predicted the S&P 500's rally unveils target for 2025**

You can read more about it [here](https://news.google.com/rss/articles/CBMirAFBVV95cUxOM1hRUkJMWnc2QzNQTkpNNGEyRmhMNFgxYm5wT1V6dlVreW4wRWFseDBGbGY3TG9kX1QyT3pFY3NrTzh2TDVaZ0t1Tjg3UW1TMlNjQURnMzNfZHBMRFF3RmhHME1CLXQtLWpOaGR3dVhlLWhwZEpkb2lLN0xIdG9Ndm1WUFUxYVhzY2hpVmpoYmwtN29GWFM3MUpmZVFHY1M0U2dYXzQtMFRjQkdN?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
