# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Tropical Storm Debby expected to rapidly strengthen to a Category 1 hurricane and could bring historic rainfall to Southeast**

You can read more about it [here](https://news.google.com/rss/articles/CBMimwFBVV95cUxPOVRJcEhLT1QxcEVySS1FU3Blc21OVUFjeExRNnJBMzhuYmV3eHhZY1RrUVFaZGVyYTNsRTdsUHlucHdPbm5GNXZLeWdsbE1BdlRZTnB4Y1ZySVF3SXYxSktjajBXSTNzLUhGSl9wNm5VTTlmZTlRMzdnZHBCZUNlQzY5QXBjZVQwa2I0VDdaY0RxYmVxUlJ1RzNDa9IBkgFBVV95cUxNYm5sM3ltU29TbzF2b0dOUl9fM3lVMEMxWWktWm9rNDJiYkczbkhYeWtQNzlnUXUxTDJWSkE3MldRSVVaV2tmNWI5UXlKSkp5WW9yMjNQa3M2amZYdDUyNU1kSlZKQjRXNUU0YVVKX0k2NUR1TFk3UDdYd3BDYnE5ZDVnWGw2NEthT3prMlJEZUw4QQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
