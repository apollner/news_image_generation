# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Israel attacks southern Lebanon, Hezbollah launches rockets at Israel**

You can read more about it [here](https://news.google.com/rss/articles/CBMisgFBVV95cUxQVl9jamN0dkx2c1dkUUVnODFqaTZxeEUwUUU2WXlmbVA5dmlNT2ZGLXBtSHY4b0J5Z21aTE85SDRlaGVIODNKb1R5Vnk2akQzSkdoZ0YtSGV1V2JmNTA1WE5rRDZteTFwSGhZZVJWdC1LdnBNTm02VWFTVVp0c3I0XzZKSzhXY1lvdGZYSzFYN1ltTllDWk1tOUpPcllvcUtPN1VHb1dPdWxDNk9GeVZGaU9n0gG3AUFVX3lxTFBnVFlsdXlFQnlJamZPV0RkS09UYlJvTk9qb0I4UXgwTEwwaGN3WGtsMUVmdTg2NHBjWHI1SDJNbU1tVmU3SGFBZEN6NmtLWDlfamVuNEZjN3BKNF9IdERfZExZTVlLNDJGM1hCRnppTVBKclNJYXBOWWxTWk9tb3ZYRERCZnp0RVl0aWlCMDRESi1zUXlJaTRMaWF2d3BlYndqdi1MQ29TOXpheTRFTm5fTHNYX21TYw?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
