# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Son says Aryeh Zalmanovich, 86, ‘was murdered’ in Gaza hospital next to Farhan al-Qadi**

You can read more about it [here](https://news.google.com/rss/articles/CBMiswFBVV95cUxQUHhZQXVNNTJoTnk1bDd3NFF1VWIwX3NTNzJON19lc0hoOEhrSzB2ek04U1planFndmhoeHJqdDEzSFl4NUhINlFwSFU5a2ozWUpUaVhZOWhOX1pwb0FLWkd5aTVtOGd1NzZBc1loSkhRYmszbFBLUVhhM2FCWFJQYWMtajdYREduWU1YWE1PbVdIelJqREZPMWFiRzhtZVluWGd1RFFFYzd3WEVyZlY1TDg4QdIBuAFBVV95cUxOWHAtM3J3cXdGYUt4TTN2T0VpSmMwc3BCeVFpUFFQYm1RNTZRM2RXX3h4RmM4ZmlhR3BKWHFBNXNUMW5vLWw2X0t3M1BBRUZXV3VidFFwdWs2di1nV0toSGdiaVFTN0hDZXNXVnU3cEpnck12NzU0b2U2VTBKa29uWHNvTkZ5NnY3NFBPVFFHZFVON2lJZlZLNVBJUTNIQ0hoTXBQRGZ6LWNHTXhGNlN4NnhFN2ZuTmVL?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
