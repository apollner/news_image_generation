# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**How much cheese should you eat a day? A nutrition expert weighs in on dairy.**

You can read more about it [here](https://news.google.com/rss/articles/CBMilAFBVV95cUxQcU5fMlk4SmI5d2czMVBiS1ZnaGNPRnNHdjFMNXplRVZiVEN5TW1YZGxYVTF5R2x6bEpvZW40TW05akNQRk93V29SMXFaRU9NOXVpM3pjb3VaeEdYNTYwQXVUMHRSRUF3MnVNMG9YcS1ST29PTlVXUFRod2NnS1JrNEtXbUJkaXlfazczaldzLXFiTFpX0gGaAUFVX3lxTFA1N3ZHUHpvVGJCdzVmOGtmNkJ6OXM2aDNlY1lQXzFLOVVHZHN2LUNYNzRpYmdzOWRhS0FWMjd1QmV2R285SDcyaVFaY1FjUy0yT1E5a25xTzZKandWTWUzaWpGaWViaDlUUExoSFRhaWZxUzBjbTZkY3pPYUluT2NlaFRxMzUyeFl0QjE3QmFHbXV5VjVXdW5RVHc?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
