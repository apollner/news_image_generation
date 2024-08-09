# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**The end of Airbnb? Once-popular rentals site's shares tumble 14% thanks to retro travel trend**

You can read more about it [here](https://news.google.com/rss/articles/CBMizwFBVV95cUxQbzhkUmc1clFBQURqbTFWVDJ4emF4emVmeUMxeWxvUFh1ZGc5aGJ2TjMxSEZ1WGg5QlN0MHJMaUZTU0pvd0JlT2Vtc3NlMmJTTTFTMHN5ZmgwSElzdWRRNlhvV0FodXVFVC1JdUVuRDBBVTdES3V2Ti1jN0NrWU8zRnlhV1lvRXZUWWozWHJIMV9BcnJqM0FDdWJmdXUyZkd5UWVZUXBTVV9LekppVE0ybHZTMTRscjlxVU1xOXZRQjhUSHloNE1maW9fSWZRWVHSAdQBQVVfeXFMT0h4NTdRUWY3X3RIVW8xY0ZLa0pRX0w5Y0k0Zk5oYTRhMVgwQlV4ZnZCT1Q2cDFSdUU1MnJrODFoVDd4YmN5dlFicHhCYXFMOFUyeERydTJsMWFXT1lRbjEwYWNoamNFYURtTWdLTTBSWDZkVkItY0E2WTZtUmlPejZIdVNmV1RaTUljTnhpRU5Ea0daX1UxaVN5OVlDZ05xUVJwcWtaRUNHZ25sbURMaEFFcFBTMEJnRmUyeDdfVTFLZVJheEZNOWlLMTFvMDE5aFhzNnA?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
