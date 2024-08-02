# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Cancer rates in millennials, Gen X-ers have risen starkly in recent years, study finds. Experts have 1 prime suspect.**

You can read more about it [here](https://news.google.com/rss/articles/CBMi8gFBVV95cUxOVUJBMm1Fcm5Ocnk0X1FmUzhPSS1sUVY3eWYycFZFeUVXc2ZSTzdmZFBXMVlmTDJSY1UtVUVULVVnRTIzbnZDSHVaWTRSZGUxeG9CZ1ZOaFI1YnZVSGRqUUttcURoZTByRW4zVEQtd0lFcnNkZkxWR1dSQ1dBaWNwWnBQUzNTYnBjdWplTjJYYm9fOEhLNkRYTkE4Ui1OblNEd0FrYkV0S1FVVWJRVDI4OGhIbC1rUGh1Z2p0TmNXZkFMYTJjc2U0NzJjSXhkMTgzUTRVWmNka1NEYklkdmdFb0FlMnVLc0VBRmYzREgyUzJkQQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
