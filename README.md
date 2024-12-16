# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Manhunt for St. Johnsbury shooting suspect ends with arrest**

You can read more about it [here](https://news.google.com/rss/articles/CBMikAFBVV95cUxOcXItRUNuWnBYdVM0NFVaQWRCVTNWT09RcEZaLVlOQXNxX2RLUkJfZEJzT3IteFZrVHZ3TFo3VHZTUXpYOGZ2MjdrV0FWeWxILVBaSWFScTBPLW9IQW1sSjdKMi12R2FQcWxiNUtaN2d0eGZBMmtXd3VSaGRRYUo4aWRCYkFpM3lSZVdGX3lONETSAaQBQVVfeXFMT05HcTQtZDVrajRnZ3RQcmF4Z0N3Mm1Fek5qZVlvQTNYSm9wUTg5SDZmVlp3akQzMzZQbnlmMm53WUVvZDVTU1ZJZnZmZkdXM0VWTUJtRHJieVR1U0g4a05TMWFweGh3aTVsNzdBODBhRnhFTmZNRmIwaUhLZURQbHJaWlVkT3NvWDZkNDhTT2E0T1M4U2k1clhtTmNPeG5wREFRT2w?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
