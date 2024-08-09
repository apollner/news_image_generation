# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Stock futures fall after Wednesday's afternoon market slide: Live updates**

You can read more about it [here](https://news.google.com/rss/articles/CBMid0FVX3lxTE0weWFPSVZFYnZXbnllZTJ3bkNHZkpEZWFwdnRZdDg1by1qc05hWnFodkNhQkRUd2dhdnFndVQyZG5uZkx1OVRXVUlQbGJwSlZSTHJjM0cwb205d3lBZW9DV0dBbjJ5dmJFV0tXUllKa3RFNmJ5U1pB0gF8QVVfeXFMTXRnbFhISGtaSDhsLV9scXE2RHVoS0JFOUd6ZXBCSDBPVFNFdlVqZUxHdDIyM0VZMUU0RWQ1dXZEQ2J0NzAxMUJxNk5MU1J0V2hyOEY2WUd4RDdmVWpOZWVXT05OMUQ0dUdqb0FXT3pmX3RONUdxcDRIRldHNg?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
