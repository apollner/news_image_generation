# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Judge Blocks F.T.C.’s Noncompete Rule**

You can read more about it [here](https://news.google.com/rss/articles/CBMiiAFBVV95cUxPSFhsYkxLRXdXTDd0SmdQb0RYSHZ1a1U1eWM0a3RBbVd4Q0ZQTTIwQXk4d2l3bk83aWJzZjM5VnZDQXFFWWN6SS1yem1FYmFBaUJZeXJpN2pqQkM5RjhSY2VHU3dsVG5QOGlxMHhHR0RRcEpZdDEwRU1hQjhGalI2dE1VWUc5akhQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
