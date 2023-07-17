# News Image Generation
This repository contains a script that generates an image based on a news headline. The image is then saved and displayed in this README.
The news headline is fetched from the NewsAPI and the image is generated using the DiffusionPipeline from the `diffusers` Python package. The image generation process is performed on a GPU.
The script runs every few minutes, fetching a new headline and generating a new image each time.

---

![Generated Image](image.png)

Prompt: Los Angeles Angels Do Something Not Done in More Than 90 Years in Win vs. Astros

[Read more](https://www.si.com/fannation/mlb/fastball/history/los-angeles-angels-do-something-not-done-in-more-than-90-years-of-baseball-history-in-win-vs-houston-astros)