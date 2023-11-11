![Capture](https://be.farazdev.com/wp-content/uploads/2023/10/vidyo-ai-1024x576.png)

# Video Processing Service - vidyo.ai
---

Contents
---

* [Overview](#overview)
* [Installation](#installation)
* [Database Schema Description](#database-schema-description)



### Overview 
---
This Python web service, built using Django, provides functionalities for video processing, including audio extraction and video watermarking. It integrates FFmpeg for media processing and uses a SQLite database to store information about processed videos.

### Installation:
---

#### Local Setup

Clone the Repository

```
git clone https://github.com/gouravmohanty7070/vidyo.ai
```

Setup Virtual Environment

To ensure a clean and isolated environment for your application, it's recommended to use a virtual environment. Here's how you can set it up:

```
cd vidyo.ai
python -m virtualenv venv
```
Activating the Virtual Environment
- On Windows:
```
venv\Scripts\activate
```

- On macOS and Linux:

```
source venv/bin/activate
```

Install Dependencies
With the virtual environment activated, install the required dependencies using pip and the requirements.txt file:
```
pip install -r requirements.txt
```

Start the Application
Navigate to the "vidyo" directory, which contains the application code:
```
cd vidyo
```

Run Migrations
```
python manage.py migrate
```

Run the following command to start the application:
```
python manage.py runserver
```

Access the Application

```
Open your web browser and go to http://127.0.0.1:8000/
```

Testing

```
Use tools like Postman or cURL to test the API endpoints.
```




#### Running with Docker

Clone the Repository

```
git clone https://github.com/gouravmohanty7070/vidyo.ai
cd vidyo.ai
```

Build the Docker Image

```
docker build -t vidyo .
```

Run the Docker container

```
docker run -p 8000:8000 vidyo
```
Access the Application

```
Open your web browser and go to http://localhost:8000
```

Testing

```
Use tools like Postman or cURL to test the API endpoints.
```

Note

```
Audio Extraction Endpoint: POST /extract-audio
Video Watermarking Endpoint: POST /watermark-video
```

### Database Schema Description

The service uses a SQLite database with the following tables and fields to store information about processed videos:

Video Table - This table stores information about both audio-extracted and watermarked videos.

<ol>
  <li>user: String field storing the username of the user who uploaded the video.</li>
  <li>upload_time: DateTime field to record the time of video upload.</li>
  <li>processed_time: Records the timestamp when the video processing was completed, automatically set to the current time when the record is updated.</li>
  <li>processing_type: Indicates the type of processing done on the video ('audio_extraction' or 'watermarking').</li>
  <li>original_video_name: Stores the name of the original video file that was uploaded.</li>
  <li>processed_video_name: Stores the name of the processed video or audio file. This is relevant for both audio extraction and watermarking functionalities.</li>
  <li>watermark_image: Stores the name of the watermark image used in the video watermarking process. This field is only applicable for watermarking.</li>
  <li>watermark_position: Indicates the position of the watermark on the video. This field is only applicable for watermarking.</li>
</ol>

Additional Tables:

Depending on your application's requirements, you may have additional tables, especially if we are implementing user authentication, logging, or other features.

Database Setup Instructions:

After setting up your Django project, run the following commands to create and apply migrations for your database schema:

```
python manage.py makemigrations
python manage.py migrate
```

