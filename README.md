# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**New body cam video shows moment police officer saw Trump shooter just before assassination attempt**

You can read more about it [here](https://news.google.com/rss/articles/CBMikAFBVV95cUxOVGFZX0R2Qy1BYlY4UHBMSWxqclBqSDZfdXVGeWtEejIwM2lLVmhqYWc0dTF3dEN5T1I3MXNZaFk4dlRVVVZ5d3BGUFM0am50dlc5dDRLVVhwdjR1UFZqWWUtMFVueEZqVnNQSDF1R2dKVTFfZlVGNmF4T1ByS1VYY0I2WFFwUXhwbjFhZmpwQ2_SAYcBQVVfeXFMTUg3THktVVNvT09wR0NGVlBOWmlVUXNhOHJyR2dfUk90QWtYQnRpdkxTQTl0Y09RUW82bVNUR0VMMFhlZlVwNDZ0b1hBVU42dW9tQURad2ZJdmJOLXRHR3A2bENMME5tQS14anVkeTh6dkJTc3BZMUdGQUV0WS1GV1pielFxdE5N?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
