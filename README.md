# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Ford shares, on pace for worst day since 2009, lead autos rout after company's disappointing earnings**

You can read more about it [here](https://news.google.com/rss/articles/CBMinAFBVV95cUxQRDVjVlVObktzYm9ObEdIRTZhb244VG9YbGlNUFI2cnN6ajc2YnhOMUtKd2VxYWJRNFBMUzhXWmpKN1JEXzZadGVjSFZxSVBleHMxcEZzQ0lULTJYakh6ay0xcVk4YUc1X2FKeDdzZGZzY0ZwVFJVVllTZlkxSHVITUFpUGFkZ1RuMEY4ZUNxazFJTVVySzVYd2cwZEzSAaIBQVVfeXFMTkpNaDRuOFF4LS1PX2FkUU8zcGNTRjBaRVpEcjNsdW43RW9PeE94YlY0UVJ6blp2bGFmMk5qTk1tYWkyUW5mMS1sR0s4LXQ5SGVrSjdaN0ROVURrTkNVSkxPcUVmNmlwQkU5b1hzYzQ5VHFzVHc0azd3Y3liaXZjckRtZHJrQ2pyZkpjclFHLTd0Z3pTZ1kxU2dRb04tbDlmWndR?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
