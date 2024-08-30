# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Exclusive: Top Ukrainian pilot killed when US-made F-16 fighter jet crashed**

You can read more about it [here](https://news.google.com/rss/articles/CBMifkFVX3lxTE15bTNPXzNNUVhobDVMenhJYko5OWcwa2R1ZFJNWTlqQ182SWdhLWptY19kVUh1aHNmaVpTdHlZRVpHV3N3VEp1dzVpenkyam1WN3JfcHBRV0JzSTN1Q3hpYS1iRHN5MGZpNEQ1dF9ncjhLMml2d3BwWktQbVVaZ9IBdEFVX3lxTE9HLWdlMUswNGRaeF9ZTWlLRHhuREpSTU5jU1M4dWltREw0c1pDWGlMbmo4bkxpb3pPLU52OWt2anJ3ek0zNEVHLXNqb2hXd3ZhVnJmRXpZaExjTnVzOG1HV3JpSkluQmlZdThUS1Z3dDg5TnpP?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
