# Geospatial Labeling Pipeline for Computer Vision Training

**Author:** Marcel Joseph

## Project Overview

This project demonstrates a production-ready **QGIS workflow** designed to generate high-fidelity training data for Semantic Segmentation AI models. It focuses on urban feature extraction (buildings and infrastructure) with a high emphasis on topological integrity and metadata enrichment.

## Technical Implementation

### 1. Mathematical Feature Engineering

I utilized the QGIS Raster Calculator and Field Calculator to derive environmental variables for the AI feature stack:

* **NDVI Analysis:** Standardized vegetation indexing for precise land-cover classification.
* **Geometric Attributes:** Automated calculation of polygon area and perimeter-to-area ratios to help models distinguish between residential and commercial structures.

### 2. Topology & Data Quality

To ensure the dataset is compatible with supervised learning, I implemented a strict validation pipeline:

* **Zero-Overlap Policy:** Using the QGIS Topology Checker to ensure no polygon intersections.
* **Co-registration:** Ensuring all vector labels are perfectly aligned with 0.5m resolution satellite imagery.

### 3. Automation (PyQGIS)

The repository includes a Python script (`scripts/ai_cleaning_pipeline.py`) that handles:

* **Geometry Validity Checks:** Programmatic filtering of invalid GEOS geometries.
* **Metadata Enrichment:** Automated population of feature tables for machine learning input.

## Key Tools & Technologies

* **QGIS 3.x:** Primary GIS environment.
* **PyQGIS (Python 3):** For scriptable data cleaning and pipeline automation.
* **Remote Sensing:** NDVI calculation and satellite imagery processing.

## Repository Structure

* `/data`: Sample metadata schemas and attribute definitions.
* `/models`: QGIS Graphical Modeler files (`.model3`).
* `/scripts`: Automated Python cleaning pipelines.

## How to Use

1. Open the `.model3` file in the QGIS Graphical Modeler.
2. Load your raw satellite imagery and vector layers.
3. Run the Python script in the QGIS console to generate the cleaned, AI-ready output.

---

### **Final Polish Tip**

Once you've pasted this, scroll to the bottom and click **"Commit changes"**. Your repository is now fully documented and ready to be shared in the "Portfolio" section of your application!
