# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Ukraine’s Zelensky fires Air Force chief, days after fatal F-16 crash**

You can read more about it [here](https://news.google.com/rss/articles/CBMiuwFBVV95cUxQM25zTElVcHNnQVhXQzB4ZHU0SGZ4TU94QWMwZTgyTUtyU1VLUXBfUmVtZ3NvUTJHM09vQ3Z1STA5dkhQcFp3ZlE0MkVtNlJUMDlqYmFBWEhzZnVVTXlRdkNzano3c3BUMmNYek00bEZfcTJhcExpN0dsZi1RMHhTSFlvSXk0ZU5TOElWRGZhTXU3N2JKNldFaFFrNG1mRzVhdGZrWTk0MkxzcW9oZDJfWElLdTRJNURyUm0w0gGyAUFVX3lxTFBqV3k0ME1UcHZ2QTMyNldySnhfVFUyZDdBT2dGMGUxRUQ5MXdmZE5tbEZDR0xuRENMRWpKUFFNQ3N3WGhDb0RmcmZXWjJZaGR3aFJnUHhFemdQaUJwOXRiMUdmZWFqZHVKSDJBNE5xSS1PcjdReGZqdjY3NndKLVlqRDNyM2dZR3R6TU9xWVM3b3hSbnR3REk0S2ZvbEZfMFo4MTJ4MklLWGhzdXZ6RGVtU2c?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
