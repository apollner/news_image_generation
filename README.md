# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**WNBA All-Star Game 2024: Caitlin Clark dishes no-look pass to Angel Reese as rookies shine in Team WNBA win**

You can read more about it [here](https://news.google.com/rss/articles/CBMijwFodHRwczovL3d3dy5jYnNzcG9ydHMuY29tL3duYmEvbmV3cy93bmJhLWFsbC1zdGFyLWdhbWUtMjAyNC1jYWl0bGluLWNsYXJrLWRpc2hlcy1uby1sb29rLXBhc3MtdG8tYW5nZWwtcmVlc2UtYXMtcm9va2llcy1zaGluZS1pbi10ZWFtLXduYmEtd2luL9IBkwFodHRwczovL3d3dy5jYnNzcG9ydHMuY29tL3duYmEvbmV3cy93bmJhLWFsbC1zdGFyLWdhbWUtMjAyNC1jYWl0bGluLWNsYXJrLWRpc2hlcy1uby1sb29rLXBhc3MtdG8tYW5nZWwtcmVlc2UtYXMtcm9va2llcy1zaGluZS1pbi10ZWFtLXduYmEtd2luL2FtcC8?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
