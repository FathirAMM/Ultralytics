### Ultralytics YOLO Usage
from ultralytics import YOLO

# Load the model (https://docs.ultralytics.com/models)
# model = YOLO("yolo11n.pt")

# results = model.predict(source="image.png")
# results = model.predict(source="image.png",save=True) # save the results image

# Extract the results (https://docs.ultralytics.com/modes/predict/#working-with-results)
# for result in results:
#     print(result.boxes.xyxy)


# segmentation
# model = YOLO("yolo11n-seg.pt")
# results = model.predict(source="image.png",save=True)
# for result in results:
#     print(result.masks.xy)


# pose estimation
model = YOLO("yolo11n-pose.pt")
results = model.predict(source="image.png",save=True)
for result in results:
    print(result.keypoints)