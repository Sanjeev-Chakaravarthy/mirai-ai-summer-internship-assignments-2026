# 🎨 Assignment 4 - AI Image Studio

AI Image Studio is a simple AI-powered image generation web application built with **Streamlit** and the **Pollinations AI API**. Users can describe an image, customize the art style and dimensions, and generate artwork in seconds.

## Features

- Generate AI images from text prompts
- Choose from multiple art styles
- Customize image width and height
- Enable Magic Enhance mode for richer prompts
- Use Surprise Me for a random creative prompt
- Download generated images as PNG files

## Tech Stack

- Python
- Streamlit
- Requests
- Pollinations AI API

## Project Structure

```text
.
├── assignment4.py
├── requirements.txt
├── demo/
│   └── demo-video
└── README.md
```

## Run Locally

```bash
pip install -r requirements.txt
python3 -m streamlit run assignment4.py
```

## Demo

A short demonstration video of the application is included in the `demo/` folder.

## What I Learned

- Working with REST APIs using Python
- Passing URL query parameters
- Prompt engineering for AI image generation
- Using Python's `random` module to build interactive features
- Developing user-friendly web applications with Streamlit
