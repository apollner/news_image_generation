# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**5 diagnosed with Legionnaires' disease in New Hampshire, health officials say**

You can read more about it [here](https://news.google.com/rss/articles/CBMirAFBVV95cUxPN19yWHpwLU9UMzdDQzg4dUg1Rm9FLVhPb1hkX2U3Q0ZzTnRDVU1KN0pZN2hNY1VFSnFoMktKbUZEdDVzQ3lZTGF0M3Fqb1dzbU9iRzV0Qzh0Y2U2SFpkWTRKWlJVV2d2ekxmRVFiVDRRZkVIODRuSUx0eFQtZFRMb3JJdllkc2tGLXdQUER6ZkVrdWdsaDNpcjBDVzNLRXNQdzZEbFRwcVRDNmN40gGyAUFVX3lxTE9RaldlbHdYWVZjZmd4S21ua2tkUWtJRkstM05wOFBGdDdfMDJXN0pFZ1BlZmtaV0dhMzQ0WFpmaFpBN3FUa2V4VXRtZ3VDTE85dXc2bG9XQWtZNmpjUUdSaGJWNHZfWm05NnZtTXFpOUU0MFdQV3A3QUJNbm40QXVzN0dNS3Q4Wm1jYVIwY1dXc2FaTHluU0VrYmtjMXZWTkpfbnp6V3plVTJlR2I3cjdJS0E?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
