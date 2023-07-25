# News Image Generation
This repository contains a script that generates an image based on a news headline. The image is then saved and displayed in this README.
The news headline is fetched from the NewsAPI and the image is generated using the DiffusionPipeline from the `diffusers` Python package. The image generation process is performed on a GPU.
The script runs every few minutes, fetching a new headline and generating a new image each time.

---

![Generated Image](image.png)

Prompt: Korea Box Office: ‘Barbie’ Limps to Fourth Place Debut

[Read more](https://variety.com/2023/film/box-office/korea-box-office-barbie-fourth-place-opening-1235678139/)