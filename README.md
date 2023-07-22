# News Image Generation
This repository contains a script that generates an image based on a news headline. The image is then saved and displayed in this README.
The news headline is fetched from the NewsAPI and the image is generated using the DiffusionPipeline from the `diffusers` Python package. The image generation process is performed on a GPU.
The script runs every few minutes, fetching a new headline and generating a new image each time.

---

![Generated Image](image.png)

Prompt: British Open: Brian Harman runs away with lead Friday at Royal Liverpool as Billy Horschel stops protester

[Read more](https://sports.yahoo.com/british-open-brian-harman-runs-away-with-lead-friday-at-royal-liverpool-as-billy-horschel-stops-protester-165743223.html)