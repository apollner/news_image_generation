# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Who is speaking at the DNC in Chicago? Here's what we know so far**

You can read more about it [here](https://news.google.com/rss/articles/CBMitwFBVV95cUxPWmtaZzlWMlI5MHZTSUd6UlBzemd3VHN2dnVUZ3FEQUxvS3pvT3kyQmR3WVBCYjUxVlhkWjU3QTJ2NlFMdlJ3OVk5S3lCMm0tNllmY0d3Ul81c2xzSE5nbTkxRkkwQ1EzS29DWHdLa3dqM2o4LXA0aXl2MV9Pd2dXcXhxVWwxLXB2c2oxNmNnZ3NTZ1BEM0ZnQnZxZlRJSzcyb2pfaWFzN2JacHJTLW9kQ0F1bkZYcGPSAb8BQVVfeXFMUFpFOWdaSlBlZC1reXZvbkd0UFpNcGtUT0JGMWluSTNMVlVGa2tCb3JHNlNlQ2dTYkswbVkyMERveklLSUtWbENROHV0M25ESE43NDJHalJtM29XaTFaa1VKVGUyenZxTm90VXVPUkVKUXhlS1hWc3doOVBobXgxTGNFLVFRcWxXaGRJZ3RfX3h2YlFEVlhPb2RJenJDa19GMEpNTURBTTBrWkw3RTViSU5yS0YtOHN1UjdGeVhwX0E?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
