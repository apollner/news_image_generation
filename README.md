# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Some ditching Uber, Airbnb: Millennial brands have gotten expensive**

You can read more about it [here](https://news.google.com/rss/articles/CBMinwFBVV95cUxPdV9vbjc2OEZCTWxNS3hoWnJBX204VDd4djNCaGVMcTRLaUZ5R2huQTJHV19vUDVxblhPUG9kTDdVSXNUeldFT1B4SnJCR252Nks5TjZGTjI1am1fbm1ZVTVRdDhiYy13LWtCMGxGdF93RVUxU3ZvUl9YRkJjVUo3Z19KbHVNM2labXMtc0hnUmxnRC1rdHl0Z2FIN3MyVXPSAaQBQVVfeXFMTnF4cFMyeUhnOE55aVV5VlZITXRJSkZsRkgzSVN1QldOQVI5dWtqLVk0VTNnekVrc1ZtUVowQ2oyZUt5TUtWUGVxcnMwZkk3X1V6SFdiNjNBdS1vdUxLODQ1SVhMUDRFT21TdmIyVm9KajQwWnRMcGpDZG1YTzk4aHZ5eDRkVldOdnJXOGVKSzBleEp0akg5RU5Ha1NkOWtRUFgwWHI?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
