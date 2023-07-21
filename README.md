# News Image Generation
This repository contains a script that generates an image based on a news headline. The image is then saved and displayed in this README.
The news headline is fetched from the NewsAPI and the image is generated using the DiffusionPipeline from the `diffusers` Python package. The image generation process is performed on a GPU.
The script runs every few minutes, fetching a new headline and generating a new image each time.

---

![Generated Image](image.png)

Prompt: Transform Your Health in Two Days: Weekend Workouts May Be As Effective as Exercising All Week

[Read more](https://scitechdaily.com/transform-your-health-in-two-days-weekend-workouts-may-be-as-effective-as-exercising-all-week/)