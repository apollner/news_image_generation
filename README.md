# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Exclusive: The inside story of John Roberts and Trump’s immunity win at the Supreme Court**

You can read more about it [here](https://news.google.com/rss/articles/CBMiaWh0dHBzOi8vd3d3LmNubi5jb20vMjAyNC8wNy8zMC9wb2xpdGljcy9zdXByZW1lLWNvdXJ0LWpvaG4tcm9iZXJ0cy10cnVtcC1pbW11bml0eS02LTMtYmlza3VwaWMvaW5kZXguaHRtbNIBYmh0dHBzOi8vYW1wLmNubi5jb20vY25uLzIwMjQvMDcvMzAvcG9saXRpY3Mvc3VwcmVtZS1jb3VydC1qb2huLXJvYmVydHMtdHJ1bXAtaW1tdW5pdHktNi0zLWJpc2t1cGlj?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
