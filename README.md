# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**More than 20 killed as Bangladesh protesters renew call for Hasina to quit**

You can read more about it [here](https://news.google.com/rss/articles/CBMitAFBVV95cUxPRGgxLXBFUG9xemtPeE83bC1SWU9hV3hGc2RKMmk1SE1DR0pMQUU1ZG9TUVRfYlg2Q3I5SWV6VkY0YVJzX2piRzFYZnYyNFB0ZEEzUVJDNHhpbWZZOGdpXzA3MkR3Ukxnb3QxdEsxREx3SXhhVk83clpXQWx4a0RtanJEcXptMmxqX0JDMG9iclFJdHZsakx1NVZUSUpZY0RESlRYcmVIYWZOYzAyMlNGTC1NQ0vSAboBQVVfeXFMT3UxZFdTNWpKdHFUTGFnMkpzcFlibkJnWGpPdmR3OEQ2Y0I5N05teTJmbWR0Ymt4alI2aTBTNGgzQzktNGE2UzFrZ0xRbjRzSm9RckxFWWxVbTc5UFZOeVVBVF9HMlpzc3lQS3M5dGJKZ2xEeHJoR1NHNl9ma0FQT3oyal94c1R2a241SGZuZTQtdTBBYk82bmRjM3c5N2JRVVc3cnNqcGJtN0doSzhTbk1SdVhqbUNvRkZn?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
