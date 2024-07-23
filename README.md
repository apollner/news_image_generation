# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**‘Twisters’ Box Office: How 4DX Screenings and Midwestern Moviegoers Propelled the Sequel to Blockbuster Status**

You can read more about it [here](https://news.google.com/rss/articles/CBMib2h0dHBzOi8vdmFyaWV0eS5jb20vMjAyNC9maWxtL2JveC1vZmZpY2UvdHdpc3RlcnMtNGR4LXNjcmVlbmluZ3MtYm94LW9mZmljZS1ibG9ja2J1c3Rlci1nbGVuLXBvd2VsbC0xMjM2MDc5NDkyL9IBc2h0dHBzOi8vdmFyaWV0eS5jb20vMjAyNC9maWxtL2JveC1vZmZpY2UvdHdpc3RlcnMtNGR4LXNjcmVlbmluZ3MtYm94LW9mZmljZS1ibG9ja2J1c3Rlci1nbGVuLXBvd2VsbC0xMjM2MDc5NDkyL2FtcC8?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
