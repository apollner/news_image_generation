# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**D’Vontaye Mitchell death: Four Milwaukee hotel workers are charged with felony murder**

You can read more about it [here](https://news.google.com/rss/articles/CBMiggFBVV95cUxPNkpFSU9RdnMyOEQ4ZkVkeEpIUENDVUoxTUFONTlqTms5dWFXT2o5OVo4V1ljT3VHbG5PeWZWcEpGVE1iMTg0ZDdQOV9FNHF2dkxKOWl4eUlTVmM2dHAtMmNiN185ZW11SEF3NWUtVG1zRkFGZWtudnM0RE9vMEc4XzN30gF4QVVfeXFMTUxSRURsTVhNR3g2LUJrSTVPWU1zRUs4VElUVnhwakdSWVFGYUtwZl9JVF9ZSnllMVVKVVZfNENaLWE4RnBfanhFMkdIRjdxTXotQUpkejFtcVhPVWFOWGFLazRMZXE3X1pMVm5samtNdE1HTHZqWU1i?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
