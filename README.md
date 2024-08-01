# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**How early homo sapiens shaped neanderthal genetics: Study**

You can read more about it [here](https://news.google.com/rss/articles/CBMixAFBVV95cUxOY1lEZVFSc19jYWRFNjRVVjVBNWlHV0p6TENoNUtLUDkxUDZ2YmN2RDhCbVd3UmlGX0xZUmpFczd1VjNLTVQtNDExYWdwZGw2YnpXT0lwenpkYXRjUW5BVWZBZmw4NWMwUXVDenhwOFY1bXh0NUxFVmVSN1E1SHNCaC0xMGJ5dlNhNk1zMFRIYVZrTUsxOHdHbnhHNUFVNjd2WlJ4dzlCZHFpdlBqSDdfd0NhNXBoWnY3eHpLNlF5aGZOVDNw0gHKAUFVX3lxTE5mcWpXUVlZWENnOEtUV0dIa2c2OWZxVHJUU0liX0lpU1dLdkgyLURYT2R0bVBHaFktNVZXelRFZHQ3ZEtMU05lMl9OMVlRU2dkQllVTTBRUFJYOGlTaElQTmJueGRLMGNRU05GMXpwN2lFR2pkdHQ5dUVYWG9NQ2h5NU5tVm5mUW42ekV3NGlWTHFVbjZicDhIbHc2Qm1ZZHYwaFRoazhBalNGVWRPZVR6Z294Mm44SVROb3lBb05ZY1BPYlhhYlBNR2c?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
