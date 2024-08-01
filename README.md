# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Hezbollah says top commander Fuad Shukr killed in Israeli strike on Beirut**

You can read more about it [here](https://news.google.com/rss/articles/CBMiswFBVV95cUxPNG1aN2xENERvY09zSVd0QnF1dkViV1lEa1ZKUVJibkZEeWJSYkVTa3JwUDl0cXROdWRjNjdvN0p3bGhSb2ptZURjeG1uSWJic09mbnRiblNud1B6Zm9BWkcwSzhlMWxoZHhaaERHNjVPVldzNWF0QlJvZW4zTk5vZGpkSVBKVF9lN21GVGhsR2JtSUFIS3ZscmxtWGZiYlFuYWhUc2RiUnRXV21aaGI4Q2ZmZ9IBuAFBVV95cUxOZHVHUHlfSW9DUDNKTk5xVFhGYXFVRjhRaVZlRXZ2UmdxbjdQbGZaUERia2x3bzNFaWVucE4tcmcxTXQwRzdmQ3NUalltQVNVaTRpRnBOUHAwTjVsZXY1emFTT255UW01cW1FbXFNV05kUHFyblh6Y0RpM1RzSU51emNraTE3UHA0aEdJamU3bmRpRmNydFpWaTNhd0xHeVp1aDVUel85NkNmUjkxWng5VWUySGxxRFJ0?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
