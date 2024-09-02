# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Five telling stats from the Miami Hurricanes’ season-opening win over the Florida Gators**

You can read more about it [here](https://news.google.com/rss/articles/CBMikgFBVV95cUxPMUxCM3czRlFDRDAxR19FQTdOM2thRUdnTklYa3ZaRkJ4SzEzTkNpRzQwd21UM21RR1lYek4tdkxYc2RVbTlHUTZyMi1TRWtjckp3TnlTSlo0bGRuZFZTS3pmTkZKZkVwOFk2dWZ0V25kRTZ2bGh4djBybnY4dTV0VmNyLVAxUVk5dlVfSUUwOWVJUdIBkgFBVV95cUxOM3JBVldUd3R4bEw4VVgtS01XMU55ZElTWDhSUFdfSUMzRDdBRXROMF94MUl2YTUyMzRWNkFQQ2Y3T1NJLUJrZzE5ODRLR0ozQU0ydkl1MkN6QXE3bEpLaE1JN1A5ZDF3SkxUY3lUMTdtOHQtcnNjams0cEZTdXFZbFBmenE2YUxEZFkzV3VETjg4QQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
