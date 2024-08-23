# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Alleged ringleader among 7 arrested in deaths of 53 migrants smuggled into Texas in tractor trailer in 2022**

You can read more about it [here](https://news.google.com/rss/articles/CBMitAFBVV95cUxQME9lR21zQklvYzhsbHNwbm9qM0YxcVJ3WkRsMDNveGlRbzNQSFU1bDRHS3pnaXdrc1IyZXBxOWlZOWVvU2ZJM1dkS3pCelYtRUpEaWRPNDNKalpCRklqOGxMR3MzT0tTSlJQdUJ1VjB4a1RsT0psNVhqYWE1aWxIT2FhZ0ZRZ2oyQVNvUm9HUDEwT3dzR0Noa011UEg5Z2h4NGpoRjhqdzRpX1Z0NHJoWDl3SVPSAboBQVVfeXFMTklaS3JaZXdubnVEYlc5VnBIRnBuVWx4VnYzVDJiVDBvb1RlcFdqR1hxS21FRFFyWEdUUHFIVTNvY1JSY01HUk1pY214aDFSQy1zdkw2bTBJM0NmRkVtc0l4dlYxbzFDczBES2tNekQ2eW9ZQ25hR3dzT3NsR0wzUzE2SVVubEQtWkwxc2RhRlhmNkc4bTd4MGdUY0RGVlUta1dRMElvNXh5WkMyRl9NUTVOVC1iSkZWUXF3?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
