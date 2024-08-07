# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Source: 49ers have Aiyuk trade framework with Browns, Patriots**

You can read more about it [here](https://news.google.com/rss/articles/CBMiwAFBVV95cUxOb2VzRnV1Q0ZTdVpRTHVvYmZiRVpJSXpEekZBai1BQjlZQ0VhcGFzMUNIZnJqZTJIcUJWcjhWeHlKSU5mUTU2MHRCSGtsbl9Sa3pmQU1nZUY2U1dHc2lCN3BmbzUxS3lYcUJaLThKV0paZFdLNTdKY2xmUXByMWFOeHFEY0pDXzRpWFZzaDJoalV4MFlJa2lpV1ZRZWlkNXN5bmx6c1VUdXNQLTBjTnVHUkVrSThHODNNcDFEbU5RV2bSAcgBQVVfeXFMTjlWb1FBQy1NdDFCcF9KckFEM1JZZ0kwQm1JRjFyWnMtSmdEOFhKMlpodDNxcG5rYm9JSXRiZzg3RHNJbUwwOFY1M0E2dGxwb3dhQlQyMXBiLUJjRGFSWWFEVTh3dmNMVEtPMHViX1NsTmVialNLLWJMb0M0TDM4VHRhWnRoanlLSVpDODhRQnd2QmxfUjA4VWpRamNheUhDOVhya0NWcHgtaV9OcU41aVpuWlliWmd4dm1ISko0S2RhRmRxNTdyT1g?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
