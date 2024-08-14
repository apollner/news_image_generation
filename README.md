# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Harris backs ending taxes on tips, echoing Trump proposal**

You can read more about it [here](https://news.google.com/rss/articles/CBMifEFVX3lxTE9iV1IxU1ExbG41RWMzOGNfMzZCQlN3R2RVTEVITnYtczNoaE1KSmhnVGJNdllQcW00YVdEYXNRZ19mbkdiVG1WdDQtQWt2R3BfcUdISXlLS3cxT3RaRGdicHVnMlpha1M4YzFLNDFuX29wOE84dC1Vck05TELSAYIBQVVfeXFMT25ueGpRN0d5S3IwTzFxRUZvSHJONUdNU1pCXzhVYnhJNEpWSVFKWXhrZHNGUlQtNmJvYzlyNTcxaGNZT1dMU2tucmtuVTV4NXU1LWVHZlBwSGdMTU9URjBVYnRydzlNUXFwOWpIc2JENFM0VjFzLWY4M1dKSHptUDUwUQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
