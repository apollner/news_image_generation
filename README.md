# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**How does sleeping in on weekends affect your health? Research offers clues**

You can read more about it [here](https://news.google.com/rss/articles/CBMinAFBVV95cUxQU09pWGZtVThQd0FVN04wUXBWOFQ0cWh4UENiTGZMT1F5bUJ3aWVzNWs4SmY5azl5dXhDTWpLdHVRQlJxZTBibFdkcVc3NUEyTHMyT0ZNY01vbHV1M3k2N0Q0UmQ2eG1ndXlTeDJxMjRWMjR6TmxoaVVhRmJqdHJOOGVDQjZqNjhYNUliY3lzYjBVYTdiWUlucTBUWFjSAZMBQVVfeXFMTjBuS09QTGw3ZExrNnhOVVpTeGV4V25ERHVRZ2U4d3pXWWpMb1E5NTNCTllIZE5tSktzUFlXQ012OXI4dEFOQ1NWRXFiR3hGSHdDYzJZUHpaYnZRSG9yblpyd292bnBFc1BpSjNmQV9ERTNtUHZaU0hHa08yUmFXbVRvYXVtYm93Um9QSmtRRUdvV1J3?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
