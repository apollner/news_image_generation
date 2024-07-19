# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Microsoft: Windows 11 23H2 now available for all eligible devices**

You can read more about it [here](https://news.google.com/rss/articles/CBMicWh0dHBzOi8vd3d3LmJsZWVwaW5nY29tcHV0ZXIuY29tL25ld3MvbWljcm9zb2Z0L21pY3Jvc29mdC13aW5kb3dzLTExLTIzaDItbm93LWF2YWlsYWJsZS1mb3ItYWxsLWVsaWdpYmxlLWRldmljZXMv0gF1aHR0cHM6Ly93d3cuYmxlZXBpbmdjb21wdXRlci5jb20vbmV3cy9taWNyb3NvZnQvbWljcm9zb2Z0LXdpbmRvd3MtMTEtMjNoMi1ub3ctYXZhaWxhYmxlLWZvci1hbGwtZWxpZ2libGUtZGV2aWNlcy9hbXAv?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
