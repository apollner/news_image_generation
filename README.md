# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Alex Morgan, world champion and Olympic gold medalist, retires from soccer**

You can read more about it [here](https://news.google.com/rss/articles/CBMirwFBVV95cUxPaDFUd1Z3Q2JWMDNtZEgxeGN2WkFwZ3NPSjQ2VEZvU0VURF9BdDdIamd4dTlyejU0WTh0YU9vTnBRajBfRU4yOXNZeWN0TVlmbW1GZ1lUejlCWjhLOHVINFpmRWlGMlk2S0tPTWIzcm5ZN2dUUXNFX3ktcGpRUlJyV1hxN0xBa0hxRHoxTXlueUdlZmFIRmhJU1EtRlVPZWZHUnAyVWhacFBaM1MxM0I00gFWQVVfeXFMTWUwNFd1NFQ1MDFSOFdHTW5NRjk1NGt6WnlwNTVjdDF5RzJYa1p5UkVEdVZGZU5Za1BDU1hGQTRuS3VrTzQ2TWdVaVZVZW93T2pBRllYYnc?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
