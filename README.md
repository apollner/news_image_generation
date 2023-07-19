# News Image Generation
This repository contains a script that generates an image based on a news headline. The image is then saved and displayed in this README.
The news headline is fetched from the NewsAPI and the image is generated using the DiffusionPipeline from the `diffusers` Python package. The image generation process is performed on a GPU.
The script runs every few minutes, fetching a new headline and generating a new image each time.

---

![Generated Image](image.png)

Prompt: Running backs react to Saquon Barkley, Josh Jacobs, Tony Pollard not getting long-term deals

[Read more](https://www.nbcsports.com/nfl/profootballtalk/rumor-mill/news/running-backs-react-to-saquon-barkley-josh-jacobs-tony-pollard-not-getting-long-term-deals)