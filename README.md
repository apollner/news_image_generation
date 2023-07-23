# News Image Generation
This repository contains a script that generates an image based on a news headline. The image is then saved and displayed in this README.
The news headline is fetched from the NewsAPI and the image is generated using the DiffusionPipeline from the `diffusers` Python package. The image generation process is performed on a GPU.
The script runs every few minutes, fetching a new headline and generating a new image each time.

---

![Generated Image](image.png)

Prompt: Oklahoma triple murder-suicide: Mom, 39, kills 10-month-old baby boy, 6-year-old son and 11-year-old daughter

[Read more](https://www.foxnews.com/us/oklahoma-triple-murder-suicide-mom-39-kills-10-month-old-baby-boy-6-year-old-son-11-year-old-daughter)