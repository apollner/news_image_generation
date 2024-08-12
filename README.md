# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Steph Curry shows otherworldly skills as USA beat France for basketball gold**

You can read more about it [here](https://news.google.com/rss/articles/CBMisgFBVV95cUxQWTJjdDVBbEp3azVpYXIwNHoxMVl0cXY1WEtFUU9rVGtfMlVMQ2UzZkJvbWUtakowQlZFaWF2T0hnbEpaNV9fdkhNYnBSUHZOcmlsY2VzWTRJMW81Y2ZBSUR1dmh5Z09PTVNIdFlwQVRFSnRiUmlZZU0xb1dCVGZVd2RmS2IxVlhuVllINUhESUprRTAzZkc4eUZ6bWZfUUZpNzJQTUwwNDc2UXFXNEJHMmdB0gGyAUFVX3lxTE1rUWxMY29qV3lPTGlrS0wwMjJZT2l1eHVfMnc2VUJtMkZNWWRBcEpxU18wS0VqZDZOLTRlQWl1N2N4VE5BQ1I5dFpEQzB3ZkNiM1BJRFpjUzJxM1N6aVhCTVh3MkVSOFVIN240aV96RWxjUWIxOUhEb3JMUS02UFh0N3hqakZkYXpkWm5IQnI4clNjVnQybWJLM2J5MVRodXNPQ2lDRk5aanEteXlMTkY1bmc?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
