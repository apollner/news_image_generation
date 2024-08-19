# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**As Blinken arrives in Israel, Netanyahu vows to stick to demands on hostage talks**

You can read more about it [here](https://news.google.com/rss/articles/CBMisgFBVV95cUxQYU9XOER4bDlnRlFiVnJmbkZta094WXJvVTFOS1JTREhISkJOUzdVUDZqZWs2ZmtwWENnbmh1Zmx6RGFDUXhwRUpTU3Z6ZDdMUFRWQjZ4WUFhSHpPNkw1VGFUNkRLUFZkTWlwR2Q0MGkwMWdpR2RuSEl0SGZ1bERQdG1oSFZVNE1UTDVCTjh3aVZSQ2NMMGpON3lybmJ0YkZORmJyUHVfYm03NDlVeTlYTFVn0gG3AUFVX3lxTFBOSm05TGZqZ0FGRXZnbmNJdWpMX0Y0eXhoenhKLTZiOTVDZ0NOelAxZGZlQm91RlVfWXRLall6ekxmeGI0cVI3MERXREpTaER5OTl5STZYaV9fb2JyTndMdXhHR0ttLUZ0d0EtUWRfVmdQYzV6OGNVdjVzUG8wYjJGZG10cDlGT3ZCblJWdmdPRnBmTGxGd1JES2pxeW1nMEV4d2hOZzdVS3R4V1k1b21ZWmd6QUNzWQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
