# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Tiger Woods tries to strike hopeful note after nightmare eight-over round**

You can read more about it [here](https://news.google.com/rss/articles/CBMif2h0dHBzOi8vd3d3LnRoZWd1YXJkaWFuLmNvbS9zcG9ydC9hcnRpY2xlLzIwMjQvanVsLzE4L3RpZ2VyLXdvb2RzLXRyaWVzLXRvLXN0cmlrZS1ob3BlZnVsLW5vdGUtYWZ0ZXItbmlnaHRtYXJlLWVpZ2h0LW92ZXItcm91bmTSAX9odHRwczovL2FtcC50aGVndWFyZGlhbi5jb20vc3BvcnQvYXJ0aWNsZS8yMDI0L2p1bC8xOC90aWdlci13b29kcy10cmllcy10by1zdHJpa2UtaG9wZWZ1bC1ub3RlLWFmdGVyLW5pZ2h0bWFyZS1laWdodC1vdmVyLXJvdW5k?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
