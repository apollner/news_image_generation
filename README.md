# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Oasis reunion latest: Liam and Noel Gallagher tease comeback with announcement hours away**

You can read more about it [here](https://news.google.com/rss/articles/CBMizgFBVV95cUxOVFBXSnVibEZOdnZoZWVsamp4VTVIU2pyYVVHRjc2Nk5ybmhGbXhLSTZyQlhlRmxKbGdjWjdwVGZOdDJlaUhFS1FHSDhxQWdZS3JuTk5KcTlQcFhqaFhGOFRUUWQ0VVoyM3JNQm1Vd1JzWE5SVFdRdFF1bHhmY2wzTUtlUi16VGVzQ1daWkpjZnRLS1VYSzk0WF9QS0VPcDk0R2VGVXRjTktveEJDeGdjZDF0ZkdqcGVKWnhGdndoVDczVnpOd2Uyei1kNEZjUQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
