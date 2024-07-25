# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Plane explosion in Nepal captured on shocking video leaves 18 dead, 1 survivor**

You can read more about it [here](https://news.google.com/rss/articles/CBMiogFBVV95cUxOX042UExudUdQdFYxLU1oQlhWNjVvMTc3ZTkxaUh4bWpzZkxBRVV1dnhTNGhweXg4RmlpaDlSODZsOGJLUUM5Mmh0WW82OS1HczlTT0VKRnBfNlNvWW1oS1RIQV9EaEJxT0JQNEZjSlhmUkMtMTAxVHhMS3AtdXlmMVRZekFFbE14WEtpSnBxM1kxSnZldjRvT0VjbEMwem5uX2fSAacBQVVfeXFMTVdoWVV4dk1ZNmtTYURkQlRkT1F0S0cyY1l1cWpOZHl2dlhiTGg4bldpLWVXczV2MU1IdUJOYUJUaGJfYTVUSTF6dXliY2ZGQzZYdjVCdkVkVW5HU1dkV2tDU0luTzE4YWxNNWVYeWl2VmVlY1RacHh0dEhJYzBIaldxbDZ1czlIX1ptS2w0d210M2wwSEFaNWgwRzBodXZvajlHSDNMem8?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
