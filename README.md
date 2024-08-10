# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Fed Seen Rejecting Calls for Jumbo Rate Cut in Economist Survey**

You can read more about it [here](https://news.google.com/rss/articles/CBMitAFBVV95cUxQTmNXOHRqWVNobF81c05wakxJc1pqTnNkU3BtSGlfY3JOVlNIbG9hX3RFb0NYR2VyTUVrdGJSMkZGV0VoajVTQ3JqNjNpMzE4dE1yQVlZcWhZbEItQjZMMFlmc3AzWGVMZmdPb21zN3YxdVowYTVmdTNaSWFkUjU1Yk94eWRzQldyTE82Y0xXV1FhR2pNRkJOQ1VIRk1EMXRrTGVpcmNaSXNBN1VEaXJZcDMtSTc?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
