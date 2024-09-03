# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Ethan Page cheats Joe Hendry out of NXT championship at No Mercy**

You can read more about it [here](https://news.google.com/rss/articles/CBMi0gFBVV95cUxPS21ra3Znd2p2M0lRRS1xeEFxa0d2SWZEZnVkbXdDUC1hNkwwSXB0ME1uQnA1R0NfUGRQb3ZVak0yamp3b01EVE9sb1ZJZWhNM3FCTWQzZFR1NEhxLW1neFBaTEh5bHJsUTRidk82Yk1jTll0alR2NzhWaDBTR0gtU2VLRVM3VGk1NlZ2NnJaeEtINkJRQ21vcFVqM2tZMHZ2Mlo1cjFGZ1pQRzNPcTNROGR3UWNoZUhVWDZwX05tMklOUUEyTFZkUmI0azQzaTJ4R2c?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
