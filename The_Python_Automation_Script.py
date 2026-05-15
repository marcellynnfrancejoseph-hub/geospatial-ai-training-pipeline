from qgis.core import QgsProject, QgsField, QgsExpression, QgsFeatureRequest
from PyQt5.QtCore import QVariant

def run_ai_cleaning_pipeline(layer_name):
    # Load the layer
    layers = QgsProject.instance().mapLayersByName(layer_name)
    if not layers:
        print(f"Error: Layer '{layer_name}' not found.")
        return
    layer = layers[0]
    
    # Track if fields need to be added
    fields_to_add = []
    
    # 1. Check 'valid_geom' flag for AI filtering
    idx_valid = layer.fields().indexFromName('valid_geom')
    if idx_valid == -1:
        fields_to_add.append(QgsField("valid_geom", QVariant.Int))

    # 2. Check 'area_sqm' for feature engineering
    idx_area = layer.fields().indexFromName('area_sqm')
    if idx_area == -1:
        fields_to_add.append(QgsField("area_sqm", QVariant.Double))

    # Add fields if they don't exist
    if fields_to_add:
        layer.startEditing()
        layer.addAttributes(fields_to_add)
        layer.updateFields()
        layer.commitChanges()
        
        # Re-index fields after updates
        idx_valid = layer.fields().indexFromName('valid_geom')
        idx_area = layer.fields().indexFromName('area_sqm')

    # 3. Process features in a single clean editing block
    layer.startEditing()
    for feature in layer.getFeatures():
        geom = feature.geometry()
        
        # Fixed capitalization: .isGeosValid()
        is_valid = 1 if geom.isGeosValid() else 0
        area = geom.area() if geom else 0.0
        
        layer.changeAttributeValue(feature.id(), idx_valid, is_valid)
        layer.changeAttributeValue(feature.id(), idx_area, round(area, 2))
    
    layer.commitChanges()
    print(f"Pipeline complete for '{layer_name}'. Topological and geometric metadata updated.")

# Usage
# run_ai_cleaning_pipeline('your_layer_name')
