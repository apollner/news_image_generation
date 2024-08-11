# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Sangamon County Sheriff Jack Campbell stepping down in wake of Sonya Massey shooting**

You can read more about it [here](https://news.google.com/rss/articles/CBMiqwFBVV95cUxQblFoekZUY3c2bDd3Z01STDdaNVpaS0lwLVhrOFpyOFhEZmV4M2JlMkM4ZF9UNl9teGNQcllEYzJtTzg4WGpOMi1HVjhIS2MxcnUzYW0zbUZzVU5uZ051MFJ2SDZfMUVHNV9yZ2VnTkUwZGpMclBQREt2UUFGVEpLNVN5bTJES0MybHZETGpuTG8wTmMwWl9Jd3Rranp3RHNuXy1Qc0EtdjBJR1nSAaIBQVVfeXFMUElMTHRuUDhLUW8xb1RfV2NTaktWQ092cHZDY0wxMTZOLUtVTW5sZE9jYTc2N3NFVWR0WC1uUmZoS0hMUERiSk1UTUhFQ2pTNC1lcklKcDYyVC15RTMyaExScTNBRlYwNklkRVBFM2pwR1k3LXVyRXVZYXFvcExfak1sNVNhRGp5WkZ4dWJEMDRKd0NsR3VmX2llM2otc1JNRUV3?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
