# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Utica singer Sofronio Vasquez wins ‘The Voice,’ becomes 2nd winner from Upstate NY**

You can read more about it [here](https://news.google.com/rss/articles/CBMiywFBVV95cUxPSExhd21LTVpxZXJsclllemJMLUhqcUdtbk93U09fSEFjeUxyZkxpTVRFV2EwSFJpTnVkLS1fNmFvTk5HdVpHU0Qzdko0c3RJUnB5S0tKV2VUeF9iM2plYVZWSk1fY2dCUDU3TEltMTBxUnRBeGhkRWFfeGxOV3p3T2N2UHBLdUpxZHBzLWNPUkx5WE5RUXE2YndVX2hJQUZuV3JmRFFlMjBwN1FkVTBuU0lZUUFLSXlDd0pXY2VHTExnN1k0ejNURURJd9IB3wFBVV95cUxNTE9lZmtNV2VfOFlXSmVvdDBReGJDbmEwb2Vab2hoR01LSHozUDh0eHpqbC1JR1FfZWZlS3hTQzdDMi1BTjA0U3FRSm5kZnE4YUo2azlFYTlvWGFYRVREMGdpV2ZBb0VSelJtMnM5eU41TURWOXUyV0NBZU1lSlh1emQ2NUdQRzg3dHh3bktUV2tTSUotSVgyOVQ5TDBKc3BETkxCc3MwbFBINGNnWkVkUklOTzNPdkVUWG8wMnlQUkU2dDlWLUNXMVljZmhhbmljWElvMFVkWFJfUmRnZEZZ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
