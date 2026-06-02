from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")

def detect_vehicles(image_path):
    image = cv2.imread(image_path)
    results = model.predict(image, conf=0.25)

    vehicle_classes = ['car', 'bus', 'truck', 'motorcycle']
    vehicles = []

    for box in results[0].boxes.data:
        cls_id = int(box[5])
        label = model.names[cls_id]

        if label in vehicle_classes:
            x1, y1, x2, y2 = map(int, box[:4])
            area = (x2 - x1) * (y2 - y1)
            cx, cy = (x1 + x2)//2, (y1 + y2)//2

            vehicles.append((cx, cy, area))

    return vehicles, image