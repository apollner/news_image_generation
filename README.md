# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**The 27 Best Jokes and Craziest Moments From Tom Brady’s Netflix Roast, From Gronk Smashing Glasses to Gisele Divorce Puns**

You can read more about it [here](https://news.google.com/rss/articles/CBMiZGh0dHBzOi8vdmFyaWV0eS5jb20vMjAyNC90di9uZXdzL3RvbS1icmFkeS1uZXRmbGl4LXJvYXN0LWJlc3Qtam9rZXMtZ2lzZWxlLWRpdm9yY2UtZ3JvbmstMTIzNTk4NjQ0Ni_SAWhodHRwczovL3ZhcmlldHkuY29tLzIwMjQvdHYvbmV3cy90b20tYnJhZHktbmV0ZmxpeC1yb2FzdC1iZXN0LWpva2VzLWdpc2VsZS1kaXZvcmNlLWdyb25rLTEyMzU5ODY0NDYvYW1wLw?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
