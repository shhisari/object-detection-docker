# object-detection-docker

Simple demo on how to deploy deep learning models using docker and communicate with other containers in the pipeline.

We create two services - object detection service and pose estimation service.
In Object Detection service we use Darknet implementation of YOLO to detect objects in an image and pass the objects further down the pipeline.

To run, install docker desktop.

Open terminal
```
cd object_detection
docker build -t object_detection_service .
docker run -it -d --name object_detection_container object_detection_service
docker exec -it <container_id> sh
```

Open new terminal tab to run another container

```
cd pose_estimation
docker build -t pose_estimation_service .
docker run -it -d --name pose_estimation_container -p 5001:5001 pose_estimation_service
docker exec -it <container_id> sh
```

Run the flask app in the pose_estimation app
```
python app.py
```

Run the detect.py in the object_detection container
```
python3 detect.py test_img.jpg
```

On running the yolo detection algorithm, you should be able to see the bounding boxes sent over to the pose estimation container
