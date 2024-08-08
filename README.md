# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Harris decides on Tim Walz as running mate**

You can read more about it [here](https://news.google.com/rss/articles/CBMiiAFBVV95cUxOclVfQzByaHpUakhfbUlteW9jQk1FZ3djY24ySUE4NTJudWN2SzFRZlNDTW9nX1BFZlVrVXNOZnpfdjFEbkw1akl1NlE1LW9PMGJfSFZuSEZBUkZzOXRLRU5DUG1DUHo1NlB4bzlzX2h1bnl4b3dxTHY0YWVXSk91SUVNY2JudGVV0gF_QVVfeXFMUF80MUVsWGVZQnJhM0RyVDZRd09jbkd5ektXaEJ6Q3k5dmpLbjczQnYyRkZ3UTF0S2ZlU3BLSGl0VzJsZGh3SU9IT0NfM18wWUd6WkFTNUdqc3BLcDFEOTNBai11TDhsWE1MVGRqNGQ3M3RjcDZfa2owTVpyeS1XZw?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
