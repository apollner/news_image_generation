# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**2024 DNC: Watch live coverage of Day 4 of the Democratic National Convention in Chicago**

You can read more about it [here](https://news.google.com/rss/articles/CBMi1gFBVV95cUxNckppYjhfUlNuSHlwNklSSDhOaHF3cTRCbkFHVzg0RDUzOFN2SXBBTnRCZGVUNkkzMDBIOHdBckIxMHlvUVZsZFFRa1pqNzk4ODNnaTlsMk9jMlJmeFVvcFZWV25LMndHRVhjNkdRMkdxeEFsUTgxM016VXB6ZzAzbVpNRmhnaTJtbVB1eXdCbDUyR3dqTGIxeE9ydFdRWFNVXzJ3T0hvOTdyOEkzc041Ni1TaUFOeFliZ2JRTGtESkktS2M3bGFxZmRPNHdzODV0azdBUHln0gHeAUFVX3lxTFBmZWlBbzJ3ZEdpZW5XM3RNOU5YejZmVUgtYUt4R3EtaGszWFNwU2xwZDRZUFB3MHlFTDVydHhWT0ZWQllQakgzX3hBVXdCWHp4VGVEY2FLWHhEZ2I5NHJXMGRKbE9lc2VmY1ZmTFFna0l3aWdkSDF2ZjFjSzVWN2NrbTV3ZHlxRWtfSXU4U045M2NrS1Q1M3EySVZRT254UG5OWHo0M1ktT3RwdTlsa1VFZTB2QlJadUlOeVlWMF90OFdGN24wa1dDQUxwVUZLU29aLWJLYXJEWjRyeE5kdw?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
