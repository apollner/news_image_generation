# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Cause of Zac Efron's hospitalization in Spain revealed; A-list star is 'fine'**

You can read more about it [here](https://news.google.com/rss/articles/CBMiogFBVV95cUxOMF9RSEpHdnlQNWJaMnJQSU5SbHJIOWF4elpocDA4LVJhMTgxV3c2UUdlZUliY1YtMklKM2stMk9IV0JhVTFVd243TmtCWVo5cTZFOFNlQjd2YzdQOWRyNmc3eEJjbW1uSGl2TU9uWHEtQVg1aHVEVHJiU0lLdy1Gb0w5UkZkNmdRUHpvV0t4UlQyVzRzMzh2VFBRR29STGdDUXfSAacBQVVfeXFMTUtCZjBzNDF1UlU1VmtpR055SkRPbEdJaFFaa3liMjUydUktaGhnVUtnNTZFYWUtVXRsS21yTnNOb2huN3ZRSnVCSTF5OUVlcTJ5RUJhRl8tdmxFQ0V6OEFHRUNudHVnWHpTTTkzU2dNcmRNRWxZOXZ6bUhHeEFEV2FFcy1QeE1BdnN3Rl9jdk5BcXpTV1lVQ3pjRXlaenBWamRPZ19relU?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
