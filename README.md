# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**German police say 26-year-old man has turned himself in, claiming to be behind Solingen knife attack**

You can read more about it [here](https://news.google.com/rss/articles/CBMipgFBVV95cUxPenFhRVhsdTMyVXFBLUhsYk5HTVd4cE1KQlU2UmlxWDRTNFk0eVQzSW9OR1Y2R2NoMDI3WUxYcmtiNVhwamt5Y2dfOGpRU19hNkg1cDFCNWowNk5SV3FtMHY5bDF3TGZtNEQ2MFFsbk4tZmtZcVp4MjBmSG40UnNDLTVLQkNLTVlDdm9CVDR3TVh2bWJ5MVp3NTFNYmJyanlCc29WLUpn?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
