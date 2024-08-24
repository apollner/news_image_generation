# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Fact-checking Day 4 of the DNC: Roundup from PolitiFact**

You can read more about it [here](https://news.google.com/rss/articles/CBMimAFBVV95cUxQZ1hhOWM2MHlGZkt3QW94cnFvS1ozSHkwRDJRdkpGcTVpQWk5QVozV25yQUNqSTBxUjVXWU50LUNNUHg3eHRTWWdmR1F3RW8tdEVJM1NsdUotQkVqbEp1UXhpTXk5amtOZE9PYS1JQ21GbDB3dlFDM2xPaGR3ODhrZmVRcVAzQjBQNlNsYXlNeERNd045RG1ZcNIBngFBVV95cUxQa1BiMjlkUERjdnhXam9FZG1aem5LRFItUmdUZ1haeFplN0IteHNTWkRVOU8wbzBPVEF5N3JRR2ZMU3hPQzgxWGIxZFcwNHZYYzBqYktPNjB2OGQ2WlFUaEpqRjI0WmJTRUJTdURSU2NMR2lqZVpPaDdySnJFNzBtNVh3VUdCS3Ntb1RWeng4a2RzQVFWa0tWWlVJbzVmUQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
