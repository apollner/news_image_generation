# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Aaron Rodgers skips Jets mandatory minicamp for ‘unexcused’ reason, could be fined for absence**

You can read more about it [here](https://news.google.com/rss/articles/CBMiaWh0dHBzOi8vd3d3LmNubi5jb20vMjAyNC8wNi8xMi9zcG9ydC9hYXJvbi1yb2RnZXJzLW1pc3NpbmctbnktamV0cy1tYW5kYXRvcnktbWluaWNhbXAtc3B0LWludGwvaW5kZXguaHRtbNIBYmh0dHBzOi8vYW1wLmNubi5jb20vY25uLzIwMjQvMDYvMTIvc3BvcnQvYWFyb24tcm9kZ2Vycy1taXNzaW5nLW55LWpldHMtbWFuZGF0b3J5LW1pbmljYW1wLXNwdC1pbnRs?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
