# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Caitlin Clark, Angel Reese are filling up box scores, setting records and eyeing the playoffs**

You can read more about it [here](https://news.google.com/rss/articles/CBMiyAFBVV95cUxQZEVIMUF3YTZXT0llSVNYTU5SZDBVdkV2N3Y3eDkzU1pHUExmRjhEUF9JVWpjNEowc2w4dDFjQ1NOZ0Z5b3RrMW42YV9FWjlZX2RpUDFqTlZJTXN1Zld0d2NvSGo3SEN1b3lGLXJUU1lGOE1aOXIwQ2tiTW4wc1U5elpvTGdiYzJZdFBsYmQtNE0yU0o4MHFFLTlOMDRtWS1tOFlkQnZuMlZ6aEREY1BHc3JSQ0x3RGgzZ0hsbTUxX1p2UDJIT0xmWg?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
