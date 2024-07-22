# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**NASA's Curiosity rover makes 'mind-blowing' discovery on Mars**

You can read more about it [here](https://news.google.com/rss/articles/CBMiYWh0dHBzOi8vd3d3LmRhaWx5bWFpbC5jby51ay9zY2llbmNldGVjaC9hcnRpY2xlLTEzNjU2MjExL25hc2EtY3VyaW9zaXR5LXJvdmVyLWRpc2NvdmVyeS1tYXJzLmh0bWzSAWVodHRwczovL3d3dy5kYWlseW1haWwuY28udWsvc2NpZW5jZXRlY2gvYXJ0aWNsZS0xMzY1NjIxMS9hbXAvbmFzYS1jdXJpb3NpdHktcm92ZXItZGlzY292ZXJ5LW1hcnMuaHRtbA?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
