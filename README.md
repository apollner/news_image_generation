# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Russia sentences American woman to 12 years for donation aiding Ukraine**

You can read more about it [here](https://news.google.com/rss/articles/CBMimAFBVV95cUxQeU9tdGk0aDg1dFY0OEM1QnV2Q3ZodXNTaWN6TmZRaW9IakdMN1lkV0NsU2RKQ0dfY2Fheldfa2RrRW9ERGh4RzJ2X3ZWWEstZVpXMnJXTWpSTk1FVTBQTzNLbmZhTjBXcDFIa3ROOThSN0RaWlFzTjg3UWt3NlY5WDRPX2dkVDNvN3hoaUZSWHFNRXkyaE93cw?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
