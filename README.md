# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Africa CDC declares mpox a public health emergency**

You can read more about it [here](https://news.google.com/rss/articles/CBMilgFBVV95cUxQQk5KOUtzLXhHVDBmbFR6MUp0NEFvdDJaeVNPVWgyaS1kV3E1X2tYdUVXOHFNeGtYN1JtdlFEYmVzX1hSQzJpUU1LVkNsdVRFbmdQTjlpRDEzMEVTdDFibU5qOTVvbjlqekNvY3M0eWtudnpHZW5EQzV3blhpNnJzbjV5c2pvV291UVAwMUM0UmNTUTRnWmfSAZsBQVVfeXFMUHcxX0czWkJzd1Q5MEdQNjNxMzlqM3daWFZmRXN4cDVTc2tWTjl3UTRwTlh1MjRGc1VZQTJVaUVwZXV4clpVSnd4bl9VOWJialIyRVctT0VlaUFxWkV5TDVReGIyTlNoMXhSSUN2TERfWS1TU0hKMkRDTWs0WGFvbnlESkdyLUlhX1R3ZXRlc21NWHA3NFVydUx3Y0k?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
