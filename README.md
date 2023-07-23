# News Image Generation
This repository contains a script that generates an image based on a news headline. The image is then saved and displayed in this README.
The news headline is fetched from the NewsAPI and the image is generated using the DiffusionPipeline from the `diffusers` Python package. The image generation process is performed on a GPU.
The script runs every few minutes, fetching a new headline and generating a new image each time.

---

![Generated Image](image.png)

Prompt: Box Office: ‘Barbie’ Breaks Ground With Biggest Opening Day of 2023, ‘Oppenheimer’ Dolling Up to $77 Million Debut

[Read more](https://variety.com/2023/film/box-office/box-office-barbie-oppenheimer-opening-day-projections-1235676681/)