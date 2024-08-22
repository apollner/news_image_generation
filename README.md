# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Tim Curry Returns to the Big Screen in Horror Movie ‘Stream’ (EXCLUSIVE)**

You can read more about it [here](https://news.google.com/rss/articles/CBMihwFBVV95cUxOMk83Wk9GTlNqNUYtb1Q3WlZ1dTM5cVJ2dkw3Wm1taW1mQnpOZlU2NDhIVl9tZm9Ta0ZLdFZsSVY4Ui1FYXZxRUtqVnNLcE9kaGNlLXZuMWhJRGY1Q2dzTjVvOWMzNzRFUDRubTIwNXFtS0dOblRUTFNkU1gzWmlHRzhhS0ItZzjSAYwBQVVfeXFMUGZkRzg2RGNfV0hfRmRKRWd5QnZYMUhpejY5NGRFZkpCUWFrekZUaDRjSVVOdE1nb2FTLTlTUzNYSFBaOVF4c253bjQ5UzZ1ZW9VaXhadjRCVUw1V08wNTBpWDhQeWVSakZnWUV0V0xJbEliVHJFS1hrcjhyUGRuRDE1OC1hWmhwcE5faUM?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
