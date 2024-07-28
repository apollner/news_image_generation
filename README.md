# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**At least 30 killed and over 100 injured in an Israeli airstrike on a school in Gaza, Palestinian officials say**

You can read more about it [here](https://news.google.com/rss/articles/CBMiWmh0dHBzOi8vd3d3LmNubi5jb20vMjAyNC8wNy8yNy9taWRkbGVlYXN0L2lzcmFlbC1nYXphLWRlaXItYWwtYmFsYWgtc2Nob29sLWludGwvaW5kZXguaHRtbNIBU2h0dHBzOi8vYW1wLmNubi5jb20vY25uLzIwMjQvMDcvMjcvbWlkZGxlZWFzdC9pc3JhZWwtZ2F6YS1kZWlyLWFsLWJhbGFoLXNjaG9vbC1pbnRs?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
