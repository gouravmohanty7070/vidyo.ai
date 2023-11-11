![Capture](https://be.farazdev.com/wp-content/uploads/2023/10/vidyo-ai-1024x576.png)

# Vidyo Processing Service - vidyo.ai
---

Contents
---

* [Overview](#overview)
* [Installation](#installation)
* [Database Schema Description](#database-schema-description)
* [Efficient Architecture Design](#efficient-architecture-design)
* [Demo Vidyo](#demo-vidyo)



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
Install FFmpeg
- On Windows:
```
Download FFmpeg:

Go to the FFmpeg Official Website and download the latest build for Windows.
Extract the Files:

Extract the downloaded ZIP file to a location on your computer (e.g., C:\FFmpeg).
Add FFmpeg to the System Path:

Right-click on 'This PC' or 'My Computer' and select 'Properties'.
Click on 'Advanced system settings' and then 'Environment Variables'.
Under 'System Variables', find and select the 'Path' variable, then click 'Edit'.
Click 'New' and add the path to the bin folder inside the extracted FFmpeg folder (e.g., C:\FFmpeg\bin).
Click 'OK' to close all dialog boxes.
Verify the Installation:

Open Command Prompt and type ffmpeg -version to check if FFmpeg is installed correctly.
```

- On macOS:

```
brew install ffmpeg
```

- On Linux:

```
sudo apt install ffmpeg
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

### Efficient Architecture Design 
---

![Capture](https://res.cloudinary.com/divr26z8e/image/upload/v1699696290/Efficient_Architecture_for_Video_Processing_Service_xqrqkj.png)

<ul>
  <li>Load Balancer : This will be the entry point for incoming video processing requests. It distributes the load evenly across multiple servers in the service cluster, ensuring no single server is overwhelmed.</li>
  <li>Video Processing Service Cluster: A cluster of servers that handle the actual video processing tasks. This cluster can be scaled horizontally to increase capacity.</li>
  <li>Resource Allocation Manager: This component dynamically allocates tasks to different queues based on the nature of the task (CPU or memory intensive).</li>
  <li>CPU Intensive Task Queue & Memory Intensive Task Queue: Separate queues for tasks that are CPU intensive and those that are memory intensive. This separation allows for more efficient processing.</li>
  <li>CPU Optimized Servers & Memory Optimized Servers: Dedicated servers optimized for either CPU or memory intensive tasks. This ensures that each task is handled by a server that is best suited for its requirements.</li>
  <li>Database for Processed Videos: After processing, the videos are stored in a database. This could be a cloud-based storage solution for scalability and ease of access.</li>
  <li>Cache Layer: A caching mechanism to quickly serve frequent requests, reducing the load on the processing servers and the database.</li>
  <li>Client Response: The final processed video or relevant data is sent back to the client.</li>
</ul>

This architecture is designed to optimize resource usage and maintain responsiveness under high load. By separating tasks based on their resource requirements and using a mix of optimized servers, the system can handle a large number of concurrent video processing requests efficiently.

### Demo Vidyo
---

[vidyo.ai assignement demo video](https://drive.google.com/file/d/1PnR9k0gLxZD28Btysv_tVGGp8q_NdUVK/view?usp=sharing)
