# News Image Generation
This repository contains a script that generates an image based on a news headline. The image is then saved and displayed in this README.
The news headline is fetched from the NewsAPI and the image is generated using the DiffusionPipeline from the `diffusers` Python package. The image generation process is performed on a GPU.
The script runs every few minutes, fetching a new headline and generating a new image each time.

---

![Generated Image](image.png)

Prompt: Tesla earnings: EV maker reports Q2 revenue and earnings beat; Musk says Q3 production will decrease slightly

[Read more](https://finance.yahoo.com/news/tesla-earnings-ev-maker-reports-q2-revenue-and-earnings-beat-musk-says-q3-production-will-decrease-slightly-201947764.html)