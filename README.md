# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Colorado man accused of killing 10 at King Soopers in 2021 was ‘in throes of a psychotic episode,’ defense says**

You can read more about it [here](https://news.google.com/rss/articles/CBMigwFBVV95cUxNek9nb09WNEtVVHZtblRJU2p1ZnF3OUlBcWFBb1VHZzhVUFVjUktVZkhHQ1JoNXVlMmZubFBFNVUyRVJiUTBBZ095X0ZtTTNTZGtGM00yVHpmbmxJS3duT0dkeEtZcHEwMVBnYTloZGN1R2QwNFB6cHJsYVl3eTgwSk1RUdIBekFVX3lxTE0tcE05UUVuZ0pCUDFIQ2xWTFlDYUZJN3BWdjJpU2c3bWJhTjdrQndZTU1xNnpXUzJnckQ3bzBHSXpiTlNhcWxFRTcyZGxDVFFCQVJpWXJ2cGd6aEpfWExSSGZlWGk2akNnNEd3eS01aDd1M1hITWJjbDJB?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
