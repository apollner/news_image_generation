# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Diplomacy takes center stage as Iran holds off retaliation against Israel**

You can read more about it [here](https://news.google.com/rss/articles/CBMipgFBVV95cUxPZ0RQOVNreHpwSlZyYTFodHV3OVFVZU5sT2JoYlM5OWJpWDBjWW00UVVJdk5PTDJKYUMzaWxTVjlSc3dOQnl4cXdTaDRleE9LR0hId1hSUUZIdmZOemFLR3ExN19EWVlWMndSRTU3aGxkMm9kYjdiSzhPSGQ2d2kxMy1STTB3TWszWkdycWhsMkpFOXV2Wm5JVlV0cXdkNjJQVGp3ejlR0gGrAUFVX3lxTE9tT0pwUVdIMmNyckJPU0YtZ0g0TDhtNTF1c3l3b2JzVGlsb1pSbUthT0puSkFLS250dHZwS0RScDNZRHI1Yi1nWTRGOW5mUXdIc3g5UWcySUFxbHJYMEZlelZSR1RXSWZ1eVBWNXJYakpRcHZvb1pCWmNycUJTTExfRmFLQ083eHBXTzBiY3g3eFFnMjE3LS1JM1FrMXFFTnVoN1ZmUDFnQ1NUNA?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
