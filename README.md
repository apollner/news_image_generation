# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Republican activist becomes first person convicted in Arizona fake electors case**

You can read more about it [here](https://news.google.com/rss/articles/CBMiigFBVV95cUxNdlVMcVQzZ0JCQVFlMmRKUzU2UmlxZ2FzVlZwbVEyOFhyUGhEUHZuN0hWMl9VTHRVMWEybEltVktLUlpsbldLa0VJSTJjRE5MYlRGNmtGMl9MT01OOTZ0V1hpd3o3T0tGRjlZbjR2U0VDOS13VkNDekJHTVVSWUF4WmdhQ0dxcndLZWfSAY8BQVVfeXFMUEZGMktvc2FHZjVGbGJTQWJWdzJxYk52andCM29JV2doQ1EwOWZnVlJZQXd1WDhaVzR5X3BuLTRsOGhIWGVYSloyRllBbTJMdm1kelEwTVl0eGUzZHJFLXcyV3FsZmVQY0FVTzlfcFljSXpBc0VQdk5lczlScHh6ZWJhY1p2ZjI1a2tKbXY0YkU?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
