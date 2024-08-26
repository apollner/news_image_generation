# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Dr. Anthony Fauci Recovering From West Nile Virus Infection**

You can read more about it [here](https://news.google.com/rss/articles/CBMigwFBVV95cUxPdFJBVi0tTExnM1kxQXJPRmNxWldJdlo3MFZzV0t3M1I3Vkd4YmI3clZ3Y3JpV3lsX296UjZtUGNIMUpUTFEwR05uWTBqblpJX3l6VXRlLXZpMXdiUWR4eVRUd0JfeEpJZ283V2NRTG01c09HMWdfak9Sc1h5aTczS3JKMA?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
