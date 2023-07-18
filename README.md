# News Image Generation
This repository contains a script that generates an image based on a news headline. The image is then saved and displayed in this README.
The news headline is fetched from the NewsAPI and the image is generated using the DiffusionPipeline from the `diffusers` Python package. The image generation process is performed on a GPU.
The script runs every few minutes, fetching a new headline and generating a new image each time.

---

![Generated Image](image.png)

Prompt: Christopher Nolan On Why He Cast Eldest Daughter In ‘Oppenheimer’ As Girl Who Gets Blown Up

[Read more](https://deadline.com/2023/07/christopher-nolan-why-cast-eldest-daughter-oppenheimer-1235439408/)