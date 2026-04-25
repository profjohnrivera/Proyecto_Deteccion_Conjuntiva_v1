from ultralytics import YOLO

model = YOLO("yolov8s.pt")  # si no existe, lo descarga
results = model("ruta/a/tu/imagen.jpg")
