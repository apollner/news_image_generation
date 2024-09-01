# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Nikki Garcia asks for privacy for family after husband Artem Chigvintsev's arrest**

You can read more about it [here](https://news.google.com/rss/articles/CBMivgFBVV95cUxNQ2lzb1I3S0xrRjZ6T0NUOEkzcUtOMzJocmRVaWNHa3E3b0lVVlA0UjZXODFKSVByZUxvb25Oal9qbVBiZDdKSFdKc1pZbmJMZ0JrWUZ1bnBySlZsR0tyS3FhMWo3LUxMTVhuLWRHeWdrNVNqNmcwTG9MTm9SeVdzRHdWZmZJeE1kRXVNNEZJeFhlMGRfZERqRXROcnZ1UThEY2pPQ0JkWVdTUEVONktOdUtOOXc5TzBCWUUzMVd30gHDAUFVX3lxTE92MVZSM2FFUFJjMU5wWThTSzh5aFlzRkMxSE93Mk40WnlMcWx4UkhQMjRyX0hpdFliMUFNOVBScWl0NkJpeXUwZWVDeW1RZE40SUl0TnZDYzVCWHcxcGg2YkRpMy1uUmp6WmNaNVAtLWtESzBFbUdHLWZfTTBoVEVpSTR3dXdwbk9ja3RWZVQ1T3RLd3RwcUtRSmdpRldjM3lZU0lidXlxRDhMa2N5bmR5U2djY09rdmc4a0IyUldGbGwzaw?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
