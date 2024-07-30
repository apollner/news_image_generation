# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Robert Downey Jr. to return to Marvel Cinematic Universe as Doctor Doom**

You can read more about it [here](https://news.google.com/rss/articles/CBMieGh0dHBzOi8vd3d3Lmdvb2Rtb3JuaW5nYW1lcmljYS5jb20vY3VsdHVyZS9zdG9yeS9yb2JlcnQtZG93bmV5LWpyLXJldHVybi1tYXJ2ZWwtY2luZW1hdGljLXVuaXZlcnNlLWRvY3Rvci1kb29tLTExMjM0OTg1OdIBfGh0dHBzOi8vd3d3Lmdvb2Rtb3JuaW5nYW1lcmljYS5jb20vYW1wL2N1bHR1cmUvc3Rvcnkvcm9iZXJ0LWRvd25leS1qci1yZXR1cm4tbWFydmVsLWNpbmVtYXRpYy11bml2ZXJzZS1kb2N0b3ItZG9vbS0xMTIzNDk4NTk?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
