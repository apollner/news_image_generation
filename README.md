# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Hunter Biden trial enters day 4 after wild testimony from exes on rampant drug use, trashed hotel rooms**

You can read more about it [here](https://news.google.com/rss/articles/CBMihAFodHRwczovL3d3dy5mb3huZXdzLmNvbS9wb2xpdGljcy9odW50ZXItYmlkZW4tdHJpYWwtZW50ZXJzLWRheS00LWFmdGVyLXdpbGQtdGVzdGltb255LWZyb20tZXhlcy1yYW1wYW50LWRydWctdXNlLXRyYXNoZWQtaG90ZWwtcm9vbXPSAYgBaHR0cHM6Ly93d3cuZm94bmV3cy5jb20vcG9saXRpY3MvaHVudGVyLWJpZGVuLXRyaWFsLWVudGVycy1kYXktNC1hZnRlci13aWxkLXRlc3RpbW9ueS1mcm9tLWV4ZXMtcmFtcGFudC1kcnVnLXVzZS10cmFzaGVkLWhvdGVsLXJvb21zLmFtcA?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
