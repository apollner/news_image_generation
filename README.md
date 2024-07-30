# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Erick Fedde traded to Cardinals, Tommy Edman to Dodgers in three-team deadline deal with White Sox**

You can read more about it [here](https://news.google.com/rss/articles/CBMihQFodHRwczovL3d3dy5jYnNzcG9ydHMuY29tL21sYi9uZXdzL2VyaWNrLWZlZGRlLXRyYWRlZC10by1jYXJkaW5hbHMtdG9tbXktZWRtYW4tdG8tZG9kZ2Vycy1pbi10aHJlZS10ZWFtLWRlYWRsaW5lLWRlYWwtd2l0aC13aGl0ZS1zb3gv0gGJAWh0dHBzOi8vd3d3LmNic3Nwb3J0cy5jb20vbWxiL25ld3MvZXJpY2stZmVkZGUtdHJhZGVkLXRvLWNhcmRpbmFscy10b21teS1lZG1hbi10by1kb2RnZXJzLWluLXRocmVlLXRlYW0tZGVhZGxpbmUtZGVhbC13aXRoLXdoaXRlLXNveC9hbXAv?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
