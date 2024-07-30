# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Alzheimer’s blood test detects disease with 90% accuracy in routine doctors’ appointments: study**

You can read more about it [here](https://news.google.com/rss/articles/CBMicGh0dHBzOi8vd3d3LmZveG5ld3MuY29tL2hlYWx0aC9hbHpoZWltZXJzLWJsb29kLXRlc3QtZGV0ZWN0cy1kaXNlYXNlLWFjY3VyYWN5LXJvdXRpbmUtZG9jdG9ycy1hcHBvaW50bWVudHMtc3R1ZHnSAXRodHRwczovL3d3dy5mb3huZXdzLmNvbS9oZWFsdGgvYWx6aGVpbWVycy1ibG9vZC10ZXN0LWRldGVjdHMtZGlzZWFzZS1hY2N1cmFjeS1yb3V0aW5lLWRvY3RvcnMtYXBwb2ludG1lbnRzLXN0dWR5LmFtcA?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
