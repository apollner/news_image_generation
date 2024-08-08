# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Saturday Night Live: 1970s Movie Cast Gets First Look**

You can read more about it [here](https://news.google.com/rss/articles/CBMiugFBVV95cUxPSVlpRGExZ3dsc1JkQXhCREgtRmxUVHhydkY2aU9sQVhPOUxnWnA5Nm9mVWx2Z3dNUWtVZ1BZZlo1STAxa3BKMWhGWmJUa25FQ2FIVlROeWc4azd3X2ZjcmdtVVNnSVViakRJYjg1dEsxLXY1ZXVzVlRQakVhWG52dFBQY0pCSURjOTBha1hBRUZFY1pNcnJOX1R3RjNJS0Zqc3JOTVhKSGtpcDdfNGR4eXpXRHc4ZWtnQUE?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
