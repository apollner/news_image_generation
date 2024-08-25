# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Boeing Starliner’s astronauts have been in limbo for months. NASA may soon make a decision on their return from space**

You can read more about it [here](https://news.google.com/rss/articles/CBMikwFBVV95cUxQVzRTZHVJdFhFY05jUXpicVduUDBpX1lVaU5FNHhlUGF3bmRBNnBlcW9QcGFNZ3NjVzNpTlVWVE5hVW9fUkpIa1hvZVFEYzF1VWZFZlZTelNsQjNLdmUzdnZFbDJCcVlQSGstaG9qLXR5d2E5bnNEMVkzRVRWSmpMeEg5VTdiek9wMm5VX0dmcFhRVlnSAYoBQVVfeXFMT2dnRGJxRWp6Ym9hNmhrMEk4cm5ucTQxVVBVZDRsd3p4T0s3OUNXQU9TWlM5MGxjZUt2M3Aza290Y0JPVkNrWDZWaHRvaEE2Y0hGTlZiUTh0ckRDMXdnTG4yeVROR0lRc25QZVFSM1NTMzhhalhVNDBnRGdLZzZIdjViaDYtRzNSQVpR?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
