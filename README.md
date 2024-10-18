# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**SpaceX Calls New Starship Test a Success, Captures Rocket at Landing**

You can read more about it [here](https://news.google.com/rss/articles/CBMiugFBVV95cUxOYlIyZmNHVnd1Z1B2dzRpSllpUWkxdVFtRDFNMjZtQUY5TmlWdDZhZDZHYXhzcnYyRWU3UTA4ZEN1Z21oOVl3RzRFa2ZrakZrOVNBRUtaNnJnbWp3NWFXSjQzZDZhOW5lYjhMWGo4bWJWUk0xOFFvS01EU1dLZUVCUExmMGV0TGVMYkFzQm5meU1aZnFYSDNxZUhxc1lWeDdYLXlROW1KVXpCRlpPSmdzZURVZzBrUWtXclHSAbwBQVVfeXFMUHNwMGY3cEc5UTZlVjg4bHQ4OFdXUVNTcm9wOC05bjVnSExEaU5TbjN2MFowdjlrc2ppTExwOURWT0hlOHMxUmpSS0VLREZacDAwWFc0MGhLUklVUWkxenBDcVdXS2xLUmJTNjVxS1J1LWRzdlBVUFBiM1pIcUI3bE9mdU85Uzh1ci13VERfNndCQjBKSUFZMjBaV3FkWHMzN0dmVXgtWEo1RWF1QmNBTkFsMHFDOWJuU1k0R0k?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
