# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**An unusual object is moving so fast it could escape the Milky Way. Scientists aren’t certain what it is**

You can read more about it [here](https://news.google.com/rss/articles/CBMijgFBVV95cUxNaldVYUxUcVVqaGhjamhhVFg3QWVTcnpqYXFHWnk2QW9KMi0yS2FQNE5ZY0pUcWhjN3N4akY4akE0OTNhdmtEZzBzV3lEczhPSmp4TU0wNElkMnRma2REY3NxUS1PLTd0R3htdTZCT29aaE1XeUFtWC1SYUZ4cFlNdDdLdWp2RXBrSTdDN0J30gGEAUFVX3lxTE9GQlJSQURyMVNReWFleGJNWWdPLThacW1Fa0NBTlBjY0V3NkRkQ3ZVNHdIM1VzTDhvWDFuNGVoREFnYmhMU2Z0Nkw4VUN3S0h1anBzX3RIMENuOHNwRFlsUG1vbGNObkdaVzY1S3VCbTh6WnVBejZGRkw4ZXg1THRveHVYOQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
