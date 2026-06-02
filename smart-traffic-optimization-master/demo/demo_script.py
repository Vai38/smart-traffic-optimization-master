from src.detection import detect_vehicles
from src.congestion import compute_congestion
from src.path_planning import dijkstra
from src.visualization import show_detection, show_congestion, show_path

IMAGE_PATH = "data/sample.jpg"

vehicles, image = detect_vehicles(IMAGE_PATH)

print("Vehicles detected:", len(vehicles))

congestion = compute_congestion(image, vehicles)

print("Congestion Matrix:\n", congestion)

path = dijkstra(congestion.tolist(), (1,0), (0,1))

print("Optimal Path:", path)

show_detection(image.copy(), vehicles)
show_congestion(congestion)
show_path(congestion, path)