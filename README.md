# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Format, favourites and key players: guide to women’s Olympic football**

You can read more about it [here](https://news.google.com/rss/articles/CBMi3AFBVV95cUxOcF90QWJ1MkJ0Wk8zVGYzZElNNFhSVFRBVi1YUmI3QUw3aVFWWFdfSnY2bkZtSXFnTkRFRVh6YmRtalpNaHRwRldpWm5tcVVnUS00VmExeGMtYk45RDdJNkJYSjNMUndkVGRwOVQ1YWpTZWdJaHI4eG1OeER6VDFLVlpsRHlENUstMHhUcW1SZXFycDRfTzQ1dWo3UW1tTXhGRS00eXJxdDVzaGpHQ3hPazRRcUZXQkFPbWNaemdERm9wOHJzaUVtT0otMURwaU9YYUdEY1NzMGotUXJY0gHcAUFVX3lxTE1rR2VyRGFMWGNzT1hMUkx4ZE1USjQzUG1UMFQwU3o0LUhGSUNkeUtNZ2NIazBYTW5tTFB1djcwRTQ3OWVSWUdLYUFCY3AxVFZHMklLVWxoSlpra0tyRlY2SWxxY0dobzVrRGlQX3AwRmFfbE1oOEJiVzI1cjFHMVZBeGhXOWZjalUydmx2VFkyRG5kOEhjQUZfLS1KT2FKT0xTWTJqdzA1empFS3VWLWFIdWVITVNweWE2UW02SFZrWGZiM1AzZFRtdTJYTGV5azZHR3A2b3UyU0s5d2I?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
