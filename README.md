# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Trump Claims He's A Victim Of ‘Very Bad People’ After Dustup At Arlington Cemetery**

You can read more about it [here](https://news.google.com/rss/articles/CBMiqAFBVV95cUxQbGVUUUtpdmhiN1hCekdWcmJrQkFjN2c5bFVqTEd4ZlpuOEk5eWlSX3dKX1hUWUx3NU1waFdEd2N5bWh5a3N1c3NDdERQeDBuQ0lDV1NneER5al8tMFBDTUlRdmRmXzBXUDZmT2xBS19nNFh2TVlMU2JLU3piLTVFa294a0Vmc0RpVmE4N2gwbThKNWwwUUtvOEdDeFc2VU9XTlRvcElHU0PSAa4BQVVfeXFMUEZFWGdlZFRYQXFFQmxvejNJX1F3TVVsTmFjRUhIR1RzZW5HMmgwbWJVMFN3TFVhTmZLemJXMVRiR0FmZ3RyMjVvS29rNy13ZlBuR3V5OUxJLXNuNy03TEV1amh4WkZwX245YXdhbVNmWDEwRk5sSnhza3hpMGhvSVRRZ0xKOThpSFVtVnN3WFR4cWRfVjlTVzRmcXo4NmUxMU9IVmVSRkdJSUJNUndB?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
