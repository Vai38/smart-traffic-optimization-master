import matplotlib.pyplot as plt
import cv2

def show_detection(image, vehicles):
    for (cx, cy, area) in vehicles:
        cv2.circle(image, (cx, cy), 5, (0,255,0), -1)

    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title("Vehicle Detection")
    plt.axis('off')
    plt.savefig("outputs/detection.png")
    plt.show()


def show_congestion(congestion):
    plt.imshow(congestion, cmap='Reds')
    plt.title("Congestion Heatmap")
    plt.colorbar()
    plt.savefig("outputs/congestion.png")
    plt.show()


def show_path(grid, path):
    plt.imshow(grid, cmap='Blues')

    for (x,y) in path:
        plt.text(y, x, '●', color='red', ha='center')

    plt.title("Optimal Path")
    plt.savefig("outputs/path.png")
    plt.show()