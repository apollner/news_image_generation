# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Disney earnings: Streaming unit turns first profit while parks business lags**

You can read more about it [here](https://news.google.com/rss/articles/CBMivgFBVV95cUxOYXdLWDN6ZEZxVWg4TXY5T0hFZXYyVHdsNTFCc1V6QVV0bW5vNEhxMWJOX0ZTTHZFbFlQMkZXbWdkOU1YeFVtTUM4Q3hPOXZBeEVxM1V4OWg2c2FJZHhMTzRDejMtYzAyOFY2M1dQdGJ3STBweG5FbnBKc3Y3LTdqdGlxcjE0QWhuZmV4NGVDemFzVy1sX01vSVlHQXkyVk4yc1hZWEhMeTk4cFBSVE8xZ3hHYzFNX0I2OWtyMzhR?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
