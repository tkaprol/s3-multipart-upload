This standalone example demonstrates uploading large files to S3 object storage using BOTO client. 

How to Run
==========

1. Just clone the project and build the container.

    docker-compose build

2. Place some large file into the following path. 

    files/test.pdf

3. Then edit docker-compose.yml

    docker-compose up

4. Check Logs and S3 

```
    [+] Building 0.0s (0/0)
    [+] Running 1/0
    ✔ Container s3-chunked-upload-s3-uploader-1  Created                      0.0s
    Attaching to s3-chunked-upload-s3-uploader-1
    s3-chunked-upload-s3-uploader-1  | Uploading /files/test.pdf to upload-test-container/path/test.pdf
    s3-chunked-upload-s3-uploader-1  | File size: 60.99 MB, Parts: 1
    s3-chunked-upload-s3-uploader-1  | Upload completed successfully!
    s3-chunked-upload-s3-uploader-1 exited with code 0
```