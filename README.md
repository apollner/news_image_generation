# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Pain-free smear tests to be rolled out in US in WEEKS - and it's hoped they will slash cervical cancers**

You can read more about it [here](https://news.google.com/rss/articles/CBMivAFBVV95cUxQUDZFbGRJdHZ2UVVvZFYyZVFBcmpTdFJzTnhaUmI2YkJKQVItZ00weklsbGFjUHZjMjBYZ3JRZ0Fra0p2WGxaUmZsSEFiaEM4STgyYVdmckROYjhZQVZaV2syLWhWZDVSek02c0VXYmlNWEQ3Q29pVTFxamZPOHhZNEF3RnlLdkZXUWp0MDUxYmgzM3hWZkNMMnFhRFY5WGFacDFPMTJENnZLMlFqaUs2TUxpRlh3NVFHQm5Xd9IBwgFBVV95cUxNYkE0Sk56LXdTX3lVcXVLUzhvemhFQ1FsMF9Sb3V0MDIya09odHk5bkhRWWZ0TldiWHlSeFA3N3RnNzB5cERyMW8zTFJhVUYwNmJtTzB2QTFCdS1PQTZiWE1UMGwwVDhra09NSnVpSnhxSE5CY1NPYlQ2cmxvRFRIeUVaYmhpUThzZ3dsdmFud3JaaEhWRlRZRmxpY002TzJVMmIxNnlGU2dtdUdyM2REQ05FLVNPY2MwOVduVTYxRk93dw?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
