# Smart Traffic Optimization System
<p align="center">
  <img src="assets/yolo_detection_idd_sample.webp" width="30%"/>
  <img src="assets/dijkstra_overlay.webp" width="30%"/>
  <img src="assets/shortest_path_vehicle_routing.webp" width="30%"/>
</p>

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

## Overview

An AI-powered system that detects vehicles from road images, estimates lane-level congestion using a grid model, and computes optimal emergency routing paths using Dijkstra's algorithm — all powered by computer vision and graph algorithms.

---

## Features

- **Vehicle Detection** — YOLOv8-based real-time detection on IDD dataset images
- **Congestion Estimation** — Grid-based pixel-area congestion scoring per frame
- **Shortest Path Routing** — Dijkstra's algorithm for optimal ambulance/emergency routing
- **Visual Outputs** — Annotated overlays for detection, congestion heatmaps, and path overlays

---

## Project Structure

```
smart-traffic-optimization/
├── src/
│   ├── detection.py       # YOLO vehicle detection
│   ├── congestion.py      # Grid congestion estimation
│   ├── path_planning.py   # Dijkstra shortest path
│   └── visualization.py   # Output rendering
├── demo/
│   └── demo_script.py     # End-to-end pipeline demo
├── assets/                # Sample output images
├── data/                  # Input images (not tracked in Git)
├── outputs/               # Generated results (not tracked in Git)
├── requirements.txt
└── README.md
```

---

## Setup & Run

```bash
# Install dependencies
pip install -r requirements.txt

# Run the demo pipeline
python demo/demo_script.py
```

> **Note:** Place your input image at `data/sample.jpg` before running.

---

## Console Outputs

<p align="center">
  <table>
    <tr>
      <td align="center"><img src="assets/console_detection.png" width="400"/><br/><b>Vehicle Detection</b></td>
      <td align="center"><img src="assets/console_vehicles.png" width="400"/><br/><b>Vehicle List</b></td>
    </tr>
    <tr>
      <td colspan="2" align="center"><img src="assets/console_congestion.png" width="400"/><br/><b>Congestion Analysis</b></td>
    </tr>
  </table>
</p>
---

## How It Works

1. **Detection** — YOLOv8 runs on the input image and returns bounding boxes for each vehicle.
2. **Congestion** — The image is divided into a grid; each cell is scored by the pixel area occupied by detected vehicles.
3. **Path Planning** — The congestion grid is treated as a weighted graph; Dijkstra finds the lowest-cost path from source to destination.
4. **Visualization** — Results are rendered as annotated images saved to `outputs/`.

---

## Requirements

See [`requirements.txt`](requirements.txt) for full dependency list. Key libraries:

- `ultralytics` — YOLOv8
- `opencv-python` — Image processing
- `networkx` — Graph operations
- `torch` / `torchvision` — Deep learning backend

---

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.