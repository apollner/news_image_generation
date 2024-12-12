# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**John Fassel on Amani Oruwariye's special teams miscue: It’s a crazy play, and it happens fast**

You can read more about it [here](https://news.google.com/rss/articles/CBMi5gFBVV95cUxNQ2RsN2VzYzQwSDIyUzUyZUcxWUJpeGhYY184WHlZTFJ4djNqWXZUaF82RWt4bHRENVVlR1Q4SE4zQ1YzalJCMTdVcUUyTXhJVklrREhkRjcxbjhNNmdQNGhqX0lpSkRfVnpEbDNBdE9pcXFubndVdExQMlo3X0RMYW5qWEV4TGEwRUw3cFo1RDhIQnloNlE5ZkgtVDBQUy1BQkJ1R3UxTDZLMWE0VkxkZHhiSnA3MW9TWDVKQmJad3ByZzJWcHNabVk1ZWVIVGhEMlc4aXY4d25RcjZlV1pMRGFSTjR6dw?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
