# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**America’s massive hotel strike just got even bigger**

You can read more about it [here](https://news.google.com/rss/articles/CBMicEFVX3lxTFBTbnBHSXE3YWJnajB4Q1FHSnpkT2xtWFB0cTcxZHp5WkN2R3V6eEtrSk1WZ01YMG5TX2Z5M0U0ekVqa2JRa3hTZGJ3NUNjX1RhNFNrVVZ0SkhxX1JualEzVzdhM2NOSFZkSzdweWUxUETSAWdBVV95cUxNZnJkUFlTOGh6dmhZZUlTN2w1aUNHdUQ5ZVc5MEdRbm1VM2Z2Mmx0cHVNWTBLYWtLUHB3LUJ4SU1lMXpLd1VWRzNVWHRzQXFMdHNjTW9VdllxV0hQN0tCaTBnUF8yclQ0?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
