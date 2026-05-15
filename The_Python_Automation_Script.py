from qgis.core import QgsProject, QgsField, QgsExpression, QgsFeatureRequest
from PyQt5.QtCore import QVariant

def run_ai_cleaning_pipeline(layer_name):
    # Load the layer
    layer = QgsProject.instance().mapLayersByName(layer_name)[0]
    
    # 1. Add a 'valid_geom' flag for AI filtering
    if layer.fields().indexFromName('valid_geom') == -1:
        layer.startEditing()
        layer.addAttribute(QgsField("valid_geom", QVariant.Int))
        layer.updateFields()

    # 2. Add 'area_sqm' for feature engineering
    if layer.fields().indexFromName('area_sqm') == -1:
        layer.startEditing()
        layer.addAttribute(QgsField("area_sqm", QVariant.Double))
        layer.updateFields()

    # 3. Process features
    layer.startEditing()
    for feature in layer.getFeatures():
        # Check if geometry is valid (Crucial for AI training)
        is_valid = 1 if feature.geometry().isGeosvalid() else 0
        area = feature.geometry().area()
        
        layer.changeAttributeValue(feature.id(), layer.fields().indexFromName('valid_geom'), is_valid)
        layer.changeAttributeValue(feature.id(), layer.fields().indexFromName('area_sqm'), round(area, 2))
    
    layer.commitChanges()
    print(f"Pipeline complete for {layer_name}. Metadata updated.")

# Usage
# run_ai_cleaning_pipeline('your_layer_name')
