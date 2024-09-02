# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**San Francisco 49ers player Ricky Pearsall shot in chest during attempted robbery, 17-year-old suspect in custody, police say**

You can read more about it [here](https://news.google.com/rss/articles/CBMixAFBVV95cUxOWjhCeExnTHYxX2s3aWM5NVdvUVdmQWJxTE1fWlZ0UmZOZ3hhSlRkUEd0cS11QlNFNENHM3ZRdHBpekU0cUs3QktFb1N1M21YbG80MHBnbUkycnBGTXNXcnF3V3paZ1U0YjVCVGZ6ZGtRaUZOckZzMEpBV2xjNDBvY1ZRRk41cFNlR3J6VG8tMmVodEZ5N2NpdmJYMkpham1scjExMVNuMkpNVC0ybXFiVUxwRHJzLUo1SmdlMUpjelNKVXlv0gG7AUFVX3lxTFBQaHFEbGRqUGdQUllORXMydlpTM2M1Skl5MHdsVzBGSERaUkJ0OW9yaVZ3aDZMb0hlZGgxZnNkeHFlMEZfVU1KQXF0aUJla3RxT3hIS0pmVmN6eUFId0FtNng0ejB5aFkwZUk4SU5GOTZQa1N1VVhhVFUyRUpQZ01hVDlPS0szS1FKdGJhUk5tMVVLZVNnZ05ycWtJcEZKY0VMaVJjNExKc1NnWTNtellVS0NxSFU3dG1aWDA?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
