# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Celebrated "Russian Spy" Whale Hvaldimir Found Dead In Norway: Report**

You can read more about it [here](https://news.google.com/rss/articles/CBMiqgFBVV95cUxQUTNBZlktazdlWkVhT0E3czlqeVlqeWZmempMZVpMMF9RdFA0WGhxX19iVDQ0TThPdk9wbWVSZEhlcFJTZkZBeHdyVEdGR3hDTGVENTZVcldsZjBwTVhtV0NDTmltRWJvc1prS1MxaWpqRGNqd0FZbWpWeU1yWkxkNWVhVDZLZ0txRVNvaFZwbDNnXzRmeTBEVzZRSFhxZTMxOWZjVW84NER4QdIBsgFBVV95cUxQTUVhSVJRNGJFUzhSLUZsNzBlVzRuRWJtYUtyLXk5Nk5Jb0dydl83TzhpMWljaUU0Vk1FYkRqTEFNb0d4Z1gwQmhqSDB1Rjd0dGd2dkRjSktxUG15cnBiQkIxZl9jcW0tWnBYN2xRa0VUWU5ILWVYRExUWjdKV1VDdU9GeWM0TXNNcDNvOE9TTW82VVlGWVBDWDVNUzdDSklueF9zblFtZlZkYndFLXlCcnBn?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
