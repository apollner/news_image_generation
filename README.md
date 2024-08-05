# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**2024 WWE SummerSlam results: Live updates, recap, grades, highlights, matches, card, start time**

You can read more about it [here](https://news.google.com/rss/articles/CBMiyAFBVV95cUxQUmd6Vm50eXIzTjlBTG1iTEIzbk0wSWJhWTJERXJkUmhDZV95Y0xTblRZX2JRYkQzemN4OXJqbDJiMF9OT1JXUWl2bDE0Sy1vZUYyU3hDSnhXLWV5SXdiOUJrbVhVc3BUcXRwT3lGbFExS1lhUmlaN1FGQ2lORXBiSzBVZk5tYk4wdDZBRk1JQll1aVNnR1hrU3U2MUJBR3ZqbW9ONkMzQVllQUphZFVCRGpucl9VZGtCQ29QWjFqNmxpQXo3SEVJetIBzgFBVV95cUxPNk53cFFDQ0EtMEhyX1U3SjFoSHlYbXhPcjROd1BlUVRxZFdTejVGdWlPZ1Z0YXJxMS1EQ0ZpRG9UWFVWbmxNaFZYWE9xTzJucEM5M19xM2JnajZ4QkozbFhtT0NyVm9CMkNpbGJiWVdrMWozSkdTYjhWb1cxbWpvWGZBTzd4bnJRRFgyOWl5MlhRdGhnLUZFaHN5SE1lYkNCV29NWUZfN2ZEeUdGSjJ6Vzc3MV8ySUo1QTlONVZVRjAyMTdBMGluZ2EwZWgyUQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
