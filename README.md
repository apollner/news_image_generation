# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**‘I don’t want to die,’ Uvalde student told 911 dispatcher during mass shooting**

You can read more about it [here](https://news.google.com/rss/articles/CBMirwFBVV95cUxNMHlET0JkcUg3QmdNb3dDakhVdHN2NzBiNFR6cHpHcTNoOVNWYkJvdDNWaHVwZzc3dEVqRnY5WXYxMVhKQ0pfT2M1ZEh6cFBJV0J0TTEwb0FMTnM3cjlXb0ZUWUs4bmZWODFsZmZtZTJfcXh2b0g1WHNQODJnU3lmVEIwZXFJNFh3eUtWOTFDSDVhbTVFTHl1UjRKSmJWQmFQQi1MLWlRVVRENl9wVWdF0gFWQVVfeXFMUDNTaDlpR0REOWRVeGFfMjdRR1ktZWdEd3cwaDJvZTZ6R0NvcU1sbGQ2VUQ4N2Q3QmZBUHhZNjh1WUs4YWlEekpid0hRRWVObU5LRGszV3c?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
