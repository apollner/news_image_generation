# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Jay Kanter, Agent for Marlon Brando, Grace Kelly and Marilyn Monroe, Dies at 97**

You can read more about it [here](https://news.google.com/rss/articles/CBMixAFBVV95cUxON2pSdHg2U3luRWhqNndUT2JMQ09uSXRSMVMzZDdUSlFFbG14TWJvTUdjWi1XSlN1TWpyLXZBMFd6UXNhUGZENnhrTG1yaEd0WENqeFJJTHd0aTlrMDZUZWpva3JlM1ROUldUNEpEanpHQXc0c25kc3ItcEUxeURiT0lzczNkOHJ4cUV3WnlLSUpqZi1LX2U0RzNPTmJiejlKSXBOMDFLMG5LQU5QVXpUV0hGbjNxclpSdVRUUUdURTc5cjVl0gHKAUFVX3lxTE5feHpfU1YwcGtXSVg5M2U4ZkMyS0ItUGRKMkx0WWdLaU5xcjNaMmR2OTJmakJOT2NVRldOMV9XSmFiaGNDWEowRFFobXJYemhzeElQNHlEQ0ZOUk1Nc0N3ckliVFgyYXloM3BDWVBvMFB6T2huNTRJV3owY3NkR1dDTkQyYUpGUWNLbVBtck9LOS0wbnE1VzJVR2JFTW5iZV9kem9ZdGFKRUM0UXpHOW1vdEdEUVYySDdNckdGZHlkaW9nS2haSDRjelE?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
