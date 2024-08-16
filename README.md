# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Gena Rowlands, veteran actor who brought husband John Cassavetes' films to life, dies at 94**

You can read more about it [here](https://news.google.com/rss/articles/CBMijwFBVV95cUxNRm1BU0dxWjZCUkYtb3p3bDk1NkRBMk9RSmpPenN4eDFNYnlfSHNPMDE2aHlQREZtZFNvUkhSekxWMWlKMC1NazFmUDVrUFZJMTJnN3A5Z2xmMVF1bWdvT0c1ODM0TzlPTlBreVB0c2Y3Z2w2aDEtRVllYVloN2RqZnRNUjlpbFVIUlhCV0xRcw?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
