# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Two meteor showers will flash across the sky around the same time in late July**

You can read more about it [here](https://news.google.com/rss/articles/CBMisgFodHRwczovL3d3dy5sb2NhbDEyLmNvbS9uZXdzL25hdGlvbi13b3JsZC9zb3V0aGVybi1kZWx0YS1hcXVhcmlpZC1tZXRlb3Itc2hvd2VyLWFscGhhLWNhcHJpY29ybmlkcy1kZWx0YS1tZXRlb3JzLXNob3dlcnMtc2t5LXNhbWUtdGltZS1sYXRlLWp1bHktcGVhay1wZWFrcy1jaW5jaW5uYXRpLWNhcHJpY29ybmlk0gGyAWh0dHBzOi8vbG9jYWwxMi5jb20vYW1wL25ld3MvbmF0aW9uLXdvcmxkL3NvdXRoZXJuLWRlbHRhLWFxdWFyaWlkLW1ldGVvci1zaG93ZXItYWxwaGEtY2Fwcmljb3JuaWRzLWRlbHRhLW1ldGVvcnMtc2hvd2Vycy1za3ktc2FtZS10aW1lLWxhdGUtanVseS1wZWFrLXBlYWtzLWNpbmNpbm5hdGktY2Fwcmljb3JuaWQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
