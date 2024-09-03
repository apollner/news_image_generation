# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**U.S. soldiers assaulted in western Turkey, local governor's office and U.S. Embassy say**

You can read more about it [here](https://news.google.com/rss/articles/CBMixwFBVV95cUxOby1SVFdwODZpMEs3UjBaaEZCTTZDM3RwcHcySnBiV3JXOGppek9Rb0FGRG1EOWNqT285TlBVYmNsQ0FQRC00Tm5YNzJKRVB3dS1QeUFNUk9qZElIWDNTQm93VXF6cU9nSElSWlBkeVFzZDctZjRIVzRNZHl2TlFHOU0yYm1zUHhxMUU1YWdmZVBmN0p0M3I2OVRDaWFidm1EcXRHQmpzTFlfNk1INVo4Sk5yTHlFRjRFVWtPdTE4dXJ2VlZTNF9V?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
