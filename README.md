# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Florida works to cull invasive Burmese python population in the Everglades: "We can't do this alone"**

You can read more about it [here](https://news.google.com/rss/articles/CBMihgFBVV95cUxOcFViMVBBend5TEV5N2dKUWUyTlFaTnF1Wkh2aG1xZk1ack0zQjRRWFV4czBKdFgyWTB2N1d3Y1MtX1UtWF9MS2N6Z3Y3NDFWNzVZNWRmSS1ROWdLaGU0bVFCMFZxMTZLV0NndzhvdlpfY3Z2OGU1X0U4UWFRT3V3ZHA3Z1otZ9IBiwFBVV95cUxOVHVlOEs0cWZTMTJnTHVMMDNiT2xCYWJoR0g4amt3RHB4NUdmT3BUSHRVemRfZ1VkLWViclZXZjNFeU1JWnpFUnVRbXNaeWlwT2UxT0o5ZFhad2FsYzM1dUdFNDZiMk5oWGxqM0Zad0VrcWV3dHdFak5NbVJidlRyZzFHWjR1czNrRmpr?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
