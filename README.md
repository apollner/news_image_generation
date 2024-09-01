# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Teams across the US hold moments of silence as sports community mourns NHL star Johnny Gaudreau and his brother**

You can read more about it [here](https://news.google.com/rss/articles/CBMikAFBVV95cUxPQm5mekFKaFBibmNjWDRFcnRXUVNoT2xKTTRlRmN6ODU5NnlKRkh0b3BRQk5VaW9pN0JOck5XSnJwQVBuNkNGRXVWd2FkVFVwOE9vck1Wcjlha0lRZmloS0VSQmJxbmgxSkpTcFRmTTNMX2c2QjFYYXlBaTI4RkFtMENTZzRQSmZSVkRqNjBmLXDSAYcBQVVfeXFMUDJaVmR0cWlEX0ZPSnBOMWxxMGZFaDBVNzRqdkxIUkNsamVoanZTbmkwVkt4cnNnMVUyMnhYeFJFUUdPaEdheE1BbVdZRkp2ZkhwTXBVLWZBQlpSV1J2aEItOTFYT3FIT1RLcjdPOTYxQm1JUHlWeDJoOEJMV3FTWE03N29rdHJv?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
