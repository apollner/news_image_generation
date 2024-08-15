# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Biden administration approves $20 billion in weapons, aircraft sales to Israel**

You can read more about it [here](https://news.google.com/rss/articles/CBMiqgFBVV95cUxNTm5wLWpLTXNvajh0cDBocnZjcERkamplWE9nYTFHSS1POFVNQlBwUXZNNUlja2Q5SnA1MFU5MjVhMFBqNGVORjFmQzEySzBfcm1LNEZ4Vi1GU2dJOWp1MVZNUlFnR3FXY2RzanJZZWpCTHZjRHVBSkNGZkxlN0ZaNnVZQl94ellaQi1mLU9jSGt0VVVTZ0VacTFqRDlETkVsdDZYTGYzTjFCUdIBrwFBVV95cUxPWHF6OUxJamswbmlCZmx3ZVQxUmFuX1FMRG5KRDh4d1RCUENNQ0tlbTU4bnFsajlCSUgwdWJ4UXZUWDFCU0R6QldYeWxhRWUycG9ndHZRQ0VDU0FRVUJHNTJiV2M5ei1SWjZPNWFhdlZSd0dFLTdLWlB1VjY3c1RXa0NJUEFnWmc5SE1hRDNtNTgzWVNOTHpwMWRCOGd6MlBHMk02SmtZckhpblgtYzVB?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
