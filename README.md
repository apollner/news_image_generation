# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**West Nile Virus cases triple in GA within the past week. Here are symptoms to look out for**

You can read more about it [here](https://news.google.com/rss/articles/CBMi4AFBVV95cUxPUHptRmluY21jR0Z4QmdJU0tabGxwSmVHT004UjE5eWhIZGpBUFBHWDR0UnFKb2o4TUxtOTBJb2dmWEtXc1lXVXYtRDllSEZLWVVXSTdJZkphWmhaMzhwSDJUVlZpUjhSTGJ5SERxX0wwMmtaTGR1TU9tWEdWZS1VZENWMmdMZUQ2VW9PQVZkWUVJU3B4NFFlVnowd1JzcmxNWnNzZVZSNTkzT3UtaFFISEpuX2U5Qkk3M0twV1pqZERoam5CRmVtZFVnV19fbmtuZFB4QXRSMF9EeEZSZGFMc9IB9AFBVV95cUxOVEVJOXVrRUhIMDNIZlV3aThnWVByT1BkTmtVZE12SzV5eExKak1TcGEtZ2cwQVlyak9uWUlNWFk5bHowcEtBREFHbWNfNjluUVNyNkJjWGliYTBBVmkyYzVKTkl6V3pNU2U1ODZ5alRRU3FwTS0zRktTcThmNFZDNWNJVzRrYVZJNTluYVJPZDNCR1libl9JTEJmU3JELTJUc2VOaXBmM0ZIY0RTdy15SHdDN0Q5N1J4SHQ0RlBGQ01jV2VILU9CbjAyeE9DQlN3ZFdoUVo5Vk4xaGJCbjAwdjhQQ1RzdkRmUE5UME9vc194NGh6?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
