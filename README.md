# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Arizona prosecutors asked grand jurors not to indict Trump in fake electors case, court records show**

You can read more about it [here](https://news.google.com/rss/articles/CBMiqwFBVV95cUxNdzFuaUx0VGN1UThZZnNxbjZJUjlTR1F3WnNMdVFWY0dfX2ZwNkNpdUgtWG5SdVJDaTk4UkNSbW15V01sb3Z0RjVsbUlzMlhOQVRwVlF4c3A3Z1MxNWprN21XbFJYOVBYUk43aUxGNXpvWHRVdUh2Ql9valBUeHdmQzZEMlRadXVQdWZTb1VIOW1TVExSd2NaUkNJQU92LW8ydmkxX0hyODRiSTTSAbABQVVfeXFMTWwzWF9SWTVZZFlKQjNBR0E5SkltVUJqeFhsY3pscU1LbTBEWFJqa19KSXBjNnR1YWFLVjM2eEZGZDJEVVhLVGRJYkJSVkIzRk9FOFVoT0dSRGtsSmkycm04MXNJSklOcUNnNWYyQ3B0SUZ3VlNQOVp0LWZjdGY4RktHXzN2UmIzQW10SmR4c0dNd01NaE9kLXZWVTdDWlQyRDc1WUZWcnQyME5yOEdWbnY?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
