# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**AMD Ryzen 9000 official pricing is finally here: from $279 for 6-core 9600X to $649 for 16-core 9950X**

You can read more about it [here](https://news.google.com/rss/articles/CBMixAFBVV95cUxOV2FDOUdrRldLQllwSVJLd1BOOE50OHhScEg5Y1V5ZmFwWWlTS29xSG1lYXVjQWhUcmYzSGV0dzdHRURUWElFeU1XV2xQR19QYzBHQ3JxTEYzanUtQ0JLZnI4Q0dQYTdRWE1FX2JVNW9UNlRLcmEtODhPWmRMUDFMemp3aktoQktMbXlHejhGaDM2VWhoWUxHRTFWS09DbGJhcDNuZ1Q3bk13LWNIWnNyeWRfakhVUllGY1JCbjNWdDF2al9Y?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
