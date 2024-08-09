# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**White Sox manager candidates: Ozzie Guillén, Grady Sizemore and more possible Pedro Grifol replacements**

You can read more about it [here](https://news.google.com/rss/articles/CBMi0wFBVV95cUxPRldFdkYxdzB4STYxR1BlWUE0WlE1ajNDb25fNG5ZMWVEaTlMVUJRcEd6VlhJTlBva0ZVSUl2M2gydU90c05Wb1ZkdkgwY0RRMmZnUWJtYTN3dlQta3I0cFRzZ3B2NUNmUkstUlJsX0RjSHZac1pCUTl6cVVMMm4tVlpDWFlVOHF4X0FsRVNMbkZTQ2RmR0J2Tm9uT0trR05VVFhMTkdCMDNlWmRKZ0NQNDcwb0s1eGRYaHpTbFFMaFpwY1k3U3BvUlFPdlNtck9kaFd30gHYAUFVX3lxTFBBclp3cWZNdWg0a20wNHlja0l0eWJSNFRXdGl0ZFJiVGVEcVF0ZWpqMUoxbFBJSnQ3VEFSbF96dGFEVTBBYXZQeHFnbGZhRVVLOXVIT1hKa1FiS1NyZUVEWkJsbXFUSUxnanNSYWFyNWttMHNBRGZudGZ3RG9lQ1dFOEt1dzg1OXlXdDJmUndIRFBYZkZzdlg1N0UyNkZZbjFzYTRUSHpod05EOS1UemZtOTlNektVbDZsd3hCSlIzOEpfcTE3RUlZWnhHRlVJVlNkb3lpSWdFeA?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
