# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**One crew dead, three survive as cargo plane crashes near Vilnius airport**

You can read more about it [here](https://news.google.com/rss/articles/CBMingFBVV95cUxPQk1DVDBGMENfOGtfdmh1d1JoaURWYUIxWC0yaXotazY2N2V4R1pKVmYzLXl3N2pjdUg4N1BlOXJUUUdPRDNpZnNIMzQ4UUNwNjhNZlI0UlczTlVuTTk1eGhpVW5oMTdVTzZEU3M4N3ZPQXlNNmo2dmNobDhtOV8xMG1aWE54bUVfSXYwbHI4ZW5lbFI0aFBnQzJIT2FMUQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
