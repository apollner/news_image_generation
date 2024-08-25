# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Foolish Kevin Costner, Francis Ford Coppola certainly made a splash -- in the worst way possible**

You can read more about it [here](https://news.google.com/rss/articles/CBMi0wFBVV95cUxPeTVJUjU5MVFNcTBpYXFOV3NWWDJESnlEOEtVc0E1cS1BM0hWdDFRQ2F5Nkt2Wm9yMGI5T3ZrUGNNTlVHOGFHeXhuWG1xWGQ2dS1HR1Rra0VLOVJZTWV5dV9JQjljSFlRcWsxeTN2ck84cTBRNERhUXByX2FOb3lkUTZWeWZSV1lKeXZTandkbXVHRjhkZU1DOVItLVdDOG9nSlI5cXMtcDVDZmZVTWV0em1yTjVIQjBrRnQzaWYzVXRHRnJaUUlBeXRuQ2c3QVRYQ0FV?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
