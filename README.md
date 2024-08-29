# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**SpaceX Falcon 9 booster tips over, bursts into flames while landing on drone ship after Starlinks launch**

You can read more about it [here](https://news.google.com/rss/articles/CBMinwFBVV95cUxPN0RrRVJYclRXaWIyLXlpV1IzOXdHMUpKTENuVlBzd2F5Qko2TDJHby1TTWpTRlNObkFYRGo4LWhydlpPUG14c3M3WjFrSjl0d3lJVTVUU0hiOFJVQU9STk9YemU4ZERZdHF0ZkNZU201RHVDY3ZHdWR2RmFGOENyVlJKOUNGTUtnWmxxc0sxNkZhLWFVdlN2SjZXaUExalnSAaQBQVVfeXFMTVMzc1l1d0NkS3lnTDN3Yzd3WEdKN0x0TEZlZ0hDeS1rbHo0c3NJNFNuQUE1LU1MLTA3LWpzU0VUMHpJS21HdFQ4WFBYS0R2OEFyM1NHTlVHU2pSeU9MRlZZZVE4aUhpUk11b1dVMndTQl83NnpDM0x1dWxHUEdIY3FacExMNVd6a1NNYlM4VUZwRlZCV3BJUHpGUUFNc3NTYVVJTk4?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
