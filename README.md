# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Israel expects UK, France to help hit Iran if Tehran attacks, Katz tells counterparts**

You can read more about it [here](https://news.google.com/rss/articles/CBMitAFBVV95cUxPMGp6S09XOTd4c2VpTzdpb2s2ZGZHRGNpS1Q0MDd2UGdNQmJZTlh6aXNwYW5hajdFd3NCaEtXbUQ3YUJGUXJtQV9IV0dHZi0xbEpoNldQSDZGS2NFRlF5aW5ZUEJGNU9zX0ZOamFndDVsY29YYXBJMVpLZXVKSUZkdHNMMTVucFI5RTdlNl80Z2N6X0l6Ql9FbUQ5Ni1JcTk1MVY1andXNEtUaDFCU28yaW5nQ2PSAboBQVVfeXFMTjRVdXd6RFVESnJsb3AwYjAwQ3ZyRTV0NlFPUm5wRUZuY1J5Vk42WmY5N1pJZW9LRnBCQjBXNjdvS1FLSm11SFU4SWszSmZvanFPOWZJbTFKQzNET3VmY0N4VUljNzZRT2NIeTdhQzdmQl9MS2tsWG1XNWJZRTVhQ09vNHdoMDVSTnhTbVlUREhST29qZEYtemVIMGxxeUZqcVVsdkhULWNTNzNtempKYUhpVlNRNi1DUmdn?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
