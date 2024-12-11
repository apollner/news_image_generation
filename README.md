# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**S&P 500 Gains and Losses Today: Hershey Stock Simmers as Mondelez Weighs Takeover**

You can read more about it [here](https://news.google.com/rss/articles/CBMivgFBVV95cUxNdmVkcFlxOUgwT0J3VjZmNHpFZUt6U3NzOUFvd2dORmI3bDlRbnRkVnJqUGZwMEZ6NnEyb056TjFDOHE5T1RKajFrb2NNdVVkZ0NTWXJzYk1aT1pKa0liZWxQZlF5ejdNNjlEb2JaQ0lVZ0tBUjBqVnU2bG1IMzByLXQ2XzROc1VGU0tmODBQVUQ2RHU5SmVMRDAyWGxyc1lXaGxBVzEzZ3ZIX2x2TGRaNXA5SlgtNWZidXVhQmtn?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
