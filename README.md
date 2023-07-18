# News Image Generation
This repository contains a script that generates an image based on a news headline. The image is then saved and displayed in this README.
The news headline is fetched from the NewsAPI and the image is generated using the DiffusionPipeline from the `diffusers` Python package. The image generation process is performed on a GPU.
The script runs every few minutes, fetching a new headline and generating a new image each time.

---

![Generated Image](image.png)

Prompt: RFK Jr. accused of making antisemitic, racist claims about COVID-19 but insists he was misunderstood

[Read more](https://abcnews.go.com/Politics/rfk-jr-accused-making-antisemitic-racist-claims-covid/story?id=101323851)