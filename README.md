# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Harris-Trump debate rules include muted mics and no audience**

You can read more about it [here](https://news.google.com/rss/articles/CBMinwFBVV95cUxOaWk4ZkMxcG1BUU1jaURVclJNblRMN1BtVkVGRmhVMm1Mdm5ZMXFuaXB0WXZxMGFmaDlrRGlvTm4tSEtKTnVLWDlINkxhYks0eDN2NUN5N1dmS2RWUndCcm1Ldm9qcFF3ZWlHZnFMenpEa0pKNXdFcDBmOEx6NlZHcGhURmZKcWhib1Q1aGFUclFhMXJ3Q0NaRTlUT1B5eFnSAaQBQVVfeXFMUHR3VmFjcUQ5S2RSTDlCWlhxMjlielJndTl4WGJyc3dwbElSbU5mRXlmMjg3UWFvTVFXQndTemt1RVhjVlZJZ0xBSFVlQ3VoNkxOS0JJNDFpTE9vV1pyTmpZRkp2ckZtSzVwUUFuemJXMmIybm9YalpKU0Q1WTZ3Tkg2aGNZUDNlRjJqUi1MVkFCZ2FyYmItbWtBUzlnVmxRNHJnNng?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
