# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Matthew Perry’s ‘Ketamine Queen’s Other Victim Revealed**

You can read more about it [here](https://news.google.com/rss/articles/CBMimwFBVV95cUxQbVNqMGVKZmp6cWlkdlNyMm9fYWRWb1lCS2NmWFRfOXlHOXV3UmtMaXNTT1FRb0p0cFU4bXVIdnRXSWtiaU03Q2FQSEFWdklSUWtjQi1VU3BxWWNGb1hJM3BBdGRJYVh5NUZiR0VNcVVHVG1WMWFqQkNacXFGRzhzdEs4ZVJma2RPVXBVTVVJMk13N251ZDNTbmZ0Zw?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
