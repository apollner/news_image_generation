# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Sean ‘Diddy’ Combs ‘gang raped’ woman as payback after she claimed he was involved in Tupac Shakur’s murder, new lawsuit claims**

You can read more about it [here](https://news.google.com/rss/articles/CBMi_AFBVV95cUxNQ3pQVEVwYjNTZFJwdk9LWEdNYWI4QmZjVDUyYWF1eFBtak5LSmZ6MlZDYXpJTWN2LTFnNkVoT1JXNWlxalZtZ1dPdjQ5ZXo1OWpjbmRmZ3Q4VURDaE5wLUJhdXFTdlg2Q2wwME5HbElQSmVKV2JXX0JiVTNHb01yT3c1bC1MMm9Ic3QxOW9wcExWNTNHQUJUREowVlNDRmhPcTQ3eVhOMGxjRi0zRTRRcnVobXllLXlrTlpibTVzS2xfUk5pZTRSMTlxVW5CTzFIUTdJZmpoUml0UjI3TGZIVjUwOWNvYjZGMkZTekp4dlVFSlRZNFNPdG1aUjk?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
