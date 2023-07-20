# News Image Generation
This repository contains a script that generates an image based on a news headline. The image is then saved and displayed in this README.
The news headline is fetched from the NewsAPI and the image is generated using the DiffusionPipeline from the `diffusers` Python package. The image generation process is performed on a GPU.
The script runs every few minutes, fetching a new headline and generating a new image each time.

---

![Generated Image](image.png)

Prompt: 'Better never rests': What winningest team in sports taught Georgia's football program

[Read more](https://247sports.com/college/georgia/article/better-never-rests-what-winningest-team-in-sports-taught-georgias-football-program-212948999/)