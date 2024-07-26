# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Two more troopers tied to Karen Read case are under internal investigation, authorities say**

You can read more about it [here](https://news.google.com/rss/articles/CBMimgFBVV95cUxPOHpyaEZ5RXZ4cGpFNkVkNjBOT1NTTkJrWkZkaEZ4SjhpYTk4ZTY3cWo1VW1sYy02cG9WMENTU3FVNkpqUFpZX3d2OVJjOHo2RVEtTGRuQWdjaXN0Z1oyMFpad0F3dkNuQUo1X215REJ0NkJ4QmRzOWhTV1BEYWMxdkt2ZXdoZXRmX3ZqMWZXcFhqZXJCV3pqeXpB?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
