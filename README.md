# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Woman charged in alleged scheme to steal Graceland, extort Elvis Presley family**

You can read more about it [here](https://news.google.com/rss/articles/CBMiugFBVV95cUxNei00TFl2Ml81VE1HUk5CU211M3dkOXJMbkhqd1FjLUh6ZnlPQ1JBdldqNVJ5YWlHSHJ0OThwYV9pRHA2RHkyRVhuelF4TUFja0JlRWsxV0hBS2k0UkJoaEJ5c1l5WVJ0dzl0aXQ0OTVuQ1dmT1NmRmg1WmhtODdkZXhPMVBjak1UQ3FjRzZPbWhsemd3ZzFuTGhLWmJpNXJfN1lGT0laTFdmdjEwS1FqVVl2RFpQRGlRa0HSAVZBVV95cUxQOGkwUUhGUkxDdVl4S0RZRy12WHo4WktPT2JJMGxrRDYxOVpObkgzX2RGRjY1LUJMWDF2bFlDa0syelVqTkktYVhURlJlaDdqRzhkX2x1QQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
