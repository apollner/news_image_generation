# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**NASA delays SpaceX astronaut mission as rumors swirl about Boeing Starliner’s safety**

You can read more about it [here](https://news.google.com/rss/articles/CBMilgFBVV95cUxOS00zVF95Z2FsWGFKbEpDb1ZyMXo5eHFKOVdCU0Q0M0RrN0wwdXduRkVneVBsWkdKVjlaMU85eUo0VG83N2U5VG9HQmRHREItZHgyM1ZJMGVYcnJveXpnYVBSY1JHdzQtVzdOWld5VzNDTS1nQ0xwQmlRbDdaRFd4RGhRSTZkVnczUDZFMTBpRjFPZXczX3fSAYwBQVVfeXFMT2N4a1d1dkVIQ1dkZzRJZFI3VDN1UTV0MkpLSndHcmtaMmVCMVRtZ0hEQnlpTFpiNDBZaEYxSG9jWHRqQ0k0MFJueXRzcEFySDB4azFwSWlUQzRqbHBwTlN3amZkRTcxWlZoMUN3UWQxLXdwWGxPZlNrZGZ5amM3aWVBbm5OZGRiMzFaTzc?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
