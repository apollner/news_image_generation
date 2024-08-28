# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Experts warn of mosquito-spread virus 'Triple E,' urge taking precautions**

You can read more about it [here](https://news.google.com/rss/articles/CBMijgJBVV95cUxNQk1teHczM1R6N1hOMGh4bHNUTmlXNWtoczZrTW1pX1EzZUo1WlFkUEV3RDFGS19tTXlUbWtkRUFad3NkTmx2S3g4MW1OSUJQSndYUi1Walk2dUVMeDRrUVYya3BYWkNGeXdEblNPcWJ6U0NwcWtPMFdWcnR0Xy0wWUNQRG81bHd6OXF0WFkwUVRkQUVNaEVLVmRzOGYwTEhrS2VwYlFLeGdVQ3FsLWphRnJoal9xU0pMZHY0T3h1aV9IOWU3cFIzUTRzRWJhRGZjejZYNFhRU2dWeTFYR2ZhMXpZTElqWDBFcUVFT0laN0x1aUJ6djhxRGNpSnhKOFBQZzVpb3hxUHRwdFZKR2fSAZMCQVVfeXFMTUlsV2ZnOHpTSDEwQXZsMzZXVTRJLVRURDZTZE1BMTFBX2lCcTRudldYSWZVdjN2TmtRVUVwOTF4ZmNUai1vR0JDRElSQmJNMEpCS0Jac3haRVJrUFBFWG1IUktObDJtZ1VHT3dFMUw5ZGhiTDdfTzFsSE9tZGM4ZUhVN1V0QjBJY3lKTHY1WkpwcDBZam5td1psX0dUOTd4cTU5bVJ3QjVLTHRNZDB3cS1YME9LS2V3SU43MEJocmpEQ2FWWXVSWEFkcVJkQXJjbHRQLUQxelBwaTZwbmpUNUx5cVNSOEtsa2FyNUdZQnhWWHJ6RFNlQlNqQ0hXY3JLVDh3N1h2dDJXTFpaMzNlTGE3Y2s?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
