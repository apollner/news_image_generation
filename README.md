# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Family members stand behind Lyle and Erik Menendez as they await a decision that could see them released from prison**

You can read more about it [here](https://news.google.com/rss/articles/CBMihAFBVV95cUxQYWVnOGs5OFI1VHVzYlNLRnoxNUNYc001enl0TmxWVXJLRXlycEFzX2NaLTdEUS0wNXFZWEt3c1R4RTJFLUR4TVlPUEcxWUYtS0dYdURMOWh0bmw5NEJJWHQ4VjFSekxQSVlNUWpRVC05cUpnS1ZDN0NZR2doSkw3T09kMznSAXtBVV95cUxNQWFtQmdZX0h2UVlDZ3VFaW5BN0FoUndjZ3FMWHBleXByNVBSd2szVnpVeDJlYlBzaFVRcmI4YlBGZzhRZ3hOeVlEQ2xxcVFPZVoybUtxZ0NaTm5lZTBWSnZYa203aU0tNWRUMWtxX3JQaEt3OVZqQkpLUVE?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
