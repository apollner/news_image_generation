# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**NASA weighs Boeing vs. SpaceX choice in bringing back Starliner astronauts**

You can read more about it [here](https://news.google.com/rss/articles/CBMimAFBVV95cUxNQjBGZThhdnc4eERLblZPV2dlZ2JUODBxQ2RLLWlFSDNvNGM4d195aU5EYlJ4Q1FSamp3cUdOSlVVN2Z3eTlKRWUxLUI2TzlFeUNvdUNiYmUxczdxU0twZ2MwbnJnQWFweFJFQ2tjdUFCRzFsdE9vbVlsc0NEbDEyYzFMbmxqSzgxVGp4OGZReWZXX29FRl91R9IBngFBVV95cUxQb1JzRmNuOWF4UXFzT0FIOFNFdzlGNEVnNG5RUHhUalpvX1NEVkUtZ3Q0WUhPZUNpVmJoVGticXdaWXNrYXVObHNmSmh5QzMzeWFGc2Q4YmxINmRfcWYxa25BUTg3N0hfRWxoS05rRnZnNURCcTRmMHVkV0JhZUhabHR2RjJZYTVYUk9BWF9kN09kZ050YUJaRDEyNnlZZw?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
