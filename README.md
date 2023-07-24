# News Image Generation
This repository contains a script that generates an image based on a news headline. The image is then saved and displayed in this README.
The news headline is fetched from the NewsAPI and the image is generated using the DiffusionPipeline from the `diffusers` Python package. The image generation process is performed on a GPU.
The script runs every few minutes, fetching a new headline and generating a new image each time.

---

![Generated Image](image.png)

Prompt: As it happened: Jonas Vingegaard celebrates Tour de France victory as Meeus wins Champs Elysees sprint

[Read more](https://www.cyclingnews.com/races/tour-de-france-2023/stage-21/live-report/)