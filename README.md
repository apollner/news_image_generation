# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Ukraine has destroyed or damaged all three bridges over Russia's Seym River, Russian sources say**

You can read more about it [here](https://news.google.com/rss/articles/CBMiqgFBVV95cUxQMHR5N0FrR2cyUDJVcXJ5aXJlb3JVVEh4V1VVeEJPWW5Ra21kQVkzMFpkZG5OaU1GeDNyQjNuR21iX1N0M2NnVnJXN21CU01ERDNIVVhfMUduSEZVZ01iRHFkUS1DZmg5eXFQQXpYUlZsRjYzdnhBb2tLWGN4RlljckFXb0wzU0k3VU1kajdPUjFuNUdHLUpaZm9JT0U2M3VZSVRncjZvU0Y5Z9IBrwFBVV95cUxPNGI5X0VnckVPNFY2T0RlWEhjUWJ1dHlyN0piQzA3M0NMOWROQzJtVHRjTUVnNGZhaUlNdDVEZ21DZkZTNXMzWTBLZ2ZmRHF2M1RRMEpXRXRTd1VPZHlHVnJmSmphY3VmdG5IVTluMWZIUVdSS1hQQW91WHJNUGY3c3JPT2o2QU45N0l5Y0hFSU03cmlqN2luRDhvdU1mSVZNb0FVRTc4QUI3RFM5eGpF?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
