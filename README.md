# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Brazilian authorities are investigating the cause of the fiery plane crash that killed 62**

You can read more about it [here](https://news.google.com/rss/articles/CBMiqgFBVV95cUxPZmJsR1cyQzlpRE1TOTBTTU5GcWozYjF0SnFaaXQzc3NXYVl0MkRFQTMxMG1EZ1FGdmVzXzhMMTBqVlp2RmtaQ1lsSkYxWG5HTHE5djIzS3h6UF9Qb0Z3MXZMWkFjQk13NDVuX3hhcWppRTY0YTg0eXY0bEpONzJwSjNqV083azByZ2FPbmtEQ3FfVVlhMkJKV3NJWWhZRUhxeEtKaGxZRUxQZw?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
