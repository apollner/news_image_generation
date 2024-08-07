# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**‘Several’ US personnel injured in rocket attack on Iraq base**

You can read more about it [here](https://news.google.com/rss/articles/CBMikwFBVV95cUxNbFFYME1QMHJ0U2hKa25ybXl2V0plUXNmRFlVYzZSeVBTS3VHeHhuWmQ0VVM0NG92TndjXzlybE4tWUk2SkVtcmRnLW1ET2MxajBnUjR6V1hwampGWk9LYUpwa29xWENrNTZCYThXY2piOVFkcEoxak9Zd3ZxZkhER1c4cU5sLWFXaWNGM0RkVHNXbmvSAYoBQVVfeXFMTWxsdDB4SlNwN2RrcDFBSHJDakx6UkFaMTlTc3o3VzN4enRLSG1ZWmpnR0RNOWhKeTZ6ZUtFeGxZOGlFM05xck5qcUVVaDhhTFJFajJ5NG1WSTl0eHRtUG9RY3dtaFFtMFZteXUwNHJPcV9BbTZUOTVPWllyMWlLWlZGalpZT1IyLVdR?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
