# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Caitlin Clark Thrills Fans in WNBA Return After Olympic Snub as Fever Beat Mercury**

You can read more about it [here](https://news.google.com/rss/articles/CBMixgFBVV95cUxNMExuMHFKTzlJUF9hSEV1aHVqTHlkb05BNHRjNkFxSXJDRkpGelZjZVF4YzVmR2o5ZERMN0tlbUFkVE1icUpGb25jZFZnX0xoTUZQTFZ1b25sTDVERk9xamxmbHdpbElmWFNZMFE4Mmw1Vi1TU1BFdU5xWERTUDJjMlBybloyekNJWEU3YmpSbVJFVzdZNV8zVDc0MERhR202VFl4YnB3eXc2ZndMN1pzNDdxQ21RaC1Yak1rU1dwWGhreTQtN2fSAdsBQVVfeXFMTnBLcTJJaDRLczdERGNtUTREOWp5SGZ5c0xRVXFwRzFockZ6dGhMbjZ1TUU3aHpGT3JSQUdhN2NwTGh4UV9VVjZ5Wlc1bGtyTDI2MndPNWg4MXd2T25UTXBGMHBzZXhydWJhRjgyWHJHb2o1MjF5b1VsdC10YmpxRkRtTUEySk1xdHNDYlZaM01keTk5OGw2Y1d2VWtva3NFek1wcDV5NDZ0OVhWenVtRWxUajM3ak5ZR21hcVUwQzZnS0VVdkNtWU96cm11am83UWJjZDFOSUNvTk1R?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
