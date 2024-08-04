# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Freed American prisoners Gershkovich and Whelan may face ‘disruptive’ trauma, say mental health experts**

You can read more about it [here](https://news.google.com/rss/articles/CBMiuwFBVV95cUxNSm5PQUFCbVd6V2dOaWQta25IZWRtUkoyV01CM0pyQnQ0SldwNzd4SktOeTN3aFlsa2NwZU1MbmMwX0hPbUhxRGM0Mk92cmpUQUZmZFRXdHpkc0VMQkdZZ1lRU1JLWWlnMkZzRzlJa1J1TDNZaUdabjVVZ3lhTFRIUzFZdXlPd1VHaTNld1ZBZlJDelRLU2w2RTIySkp2ak9ud0RzSzRDNllJRlZtblI4RjIyOFIzQkNtLUQ40gHAAUFVX3lxTE5KTFZHQ2M5Q19zemk0aGw0djRpQnpldV92UHlYOGc4UDllc2hHNFJDbUZKa09OQUdNLTU1Z3JZaUx6cy12T0h4TXRET0ZSbm1qaDZqNTFYU1ltTjZpMEJLRGhkVXlZOFNZd2h4TU1XaTRvNWRXbjlLaGdldmhYaTNIQTNxLVZWa194WXBqMGswcHhUckg3UEtvVkpObHktY0FLWHV0T2psOTRLUmtjUzJSOU84SWZLMTQ2TFp5cWFQUg?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
