# News Image Generation
This repository contains a script that generates an image based on a news headline. The image is then saved and displayed in this README.
The news headline is fetched from the NewsAPI and the image is generated using the DiffusionPipeline from the `diffusers` Python package. The image generation process is performed on a GPU.
The script runs every few minutes, fetching a new headline and generating a new image each time.

---

![Generated Image](image.png)

Prompt: Fred McGriff, Scott Rolen inducted into Baseball Hall of Fame - ESPN

[Read more](https://www.espn.com/mlb/story/_/id/38059864/fred-mcgriff-scott-rolen-inducted-baseball-hall-fame)