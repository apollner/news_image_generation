# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**How Caitlin Clark amazed with 31 points, propelling Fever to the best offense in WNBA**

You can read more about it [here](https://news.google.com/rss/articles/CBMisAFBVV95cUxOMXcwOUs2TGx2eW1JUC14LThKc0VVNjBnNzZ6SnhTSG9TOUdRaWszTE5TeTR2MW0yeFRpN2RHNS1BaERvSzJIWXlCUjNOdkFVU2N4dlVIZ1o5YjBfdnJnUEpTbUs3X3hRRkFVQ2lvMkF5dm1kN0RiZjZrN1VjOVhuT3FHcEpPbE5HT0I3R2RiT1lzU3RweUpkalc3RmdxSklLSHBmLURrODkyT2I1QnNYTg?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
