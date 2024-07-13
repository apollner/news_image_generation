# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Groom Anant Ambani arrives with family, celebs like John Cena Ananya Panday, Rajkummar Rao, Sara Ali Khan**

You can read more about it [here](https://news.google.com/rss/articles/CBMioAJodHRwczovL3RpbWVzb2ZpbmRpYS5pbmRpYXRpbWVzLmNvbS9lbnRlcnRhaW5tZW50L2hpbmRpL2JvbGx5d29vZC9uZXdzL2dyb29tLWFuYW50LWFtYmFuaS13aXRoLWZhbWlseS1jZWxlYnMtbGlrZS1qb2huLWNlbmEtYW5hbnlhLXBhbmRheS1yYWprdW1tYXItcmFvLXNhcmEtYWxpLWtoYW4taWJyYWhpbS1hbGkta2hhbi1jZWxlYnMtYXJyaXZlLWZvci1hbmFudC1hbWJhbmktcmFkaGlrYS1tZXJjaGFudHMtd2VkZGluZy1pbi1tdW1iYWktd2F0Y2gtdmlkZW9zL2FydGljbGVzaG93LzExMTY4OTgzMy5jbXPSAaQCaHR0cHM6Ly90aW1lc29maW5kaWEuaW5kaWF0aW1lcy5jb20vZW50ZXJ0YWlubWVudC9oaW5kaS9ib2xseXdvb2QvbmV3cy9ncm9vbS1hbmFudC1hbWJhbmktd2l0aC1mYW1pbHktY2VsZWJzLWxpa2Utam9obi1jZW5hLWFuYW55YS1wYW5kYXktcmFqa3VtbWFyLXJhby1zYXJhLWFsaS1raGFuLWlicmFoaW0tYWxpLWtoYW4tY2VsZWJzLWFycml2ZS1mb3ItYW5hbnQtYW1iYW5pLXJhZGhpa2EtbWVyY2hhbnRzLXdlZGRpbmctaW4tbXVtYmFpLXdhdGNoLXZpZGVvcy9hbXBfYXJ0aWNsZXNob3cvMTExNjg5ODMzLmNtcw?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
