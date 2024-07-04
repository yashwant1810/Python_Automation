# YouTube Downloader

A simple Python script to download YouTube videos or audio using the `pytube` library.

## Prerequisites

- Python 3.11
- `pytube` library

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/YouTube_Downloader.git
    cd YouTube_Downloader
    ```

2. Create a virtual environment and activate it:

    ```sh
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3. Install the required packages:

    ```sh
    pip install pytube certifi argparse
    ```

## Usage

1. **Video Download:**

    ```sh
    python main.py -v "https://www.youtube.com/watch?v=your_video_url"
    ```

2. **Audio Download:**

    ```sh
    python main.py -a "https://www.youtube.com/watch?v=your_video_url" 
    ```

## SSL Certificate Issues

If you encounter SSL certificate errors, uncomment the following line in the script:

```python
# Disable SSL certificate verification (run if SSL errors are thrown)
ssl._create_default_https_context = ssl._create_unverified_context
```

## Directory Structure

- Videos will be saved in the `./Videos` directory.
- Audio files will be saved in the `./Audio` directory.

## Script Details

- **VideoDownloader(url):** Downloads the highest resolution video from the provided URL.
- **AudioDownloader(url):** Downloads only the audio from the provided URL.

## Example

1. **Download Video:**

    ```sh
    python main.py -v "https://www.youtube.com/watch?v=example_video_url"
    ```

2. **Download Audio:**

    ```sh
    python main.py -v "https://www.youtube.com/watch?v=example_video_url" -a
    ```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements.

Features you can add - 
- Caption/Transcript Downloading
- Converting transcript to pdf 
- anything else
