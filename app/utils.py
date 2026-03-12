def soil_recommendation(nitrogen, phosphorus, potassium):

    suggestions = []

    if nitrogen < 50:
        suggestions.append("Nitrogen is low. Add nitrogen fertilizer.")

    if phosphorus < 40:
        suggestions.append("Phosphorus is low. Add phosphate fertilizer.")

    if potassium < 40:
        suggestions.append("Potassium is low. Add potash fertilizer.")

    if not suggestions:
        suggestions.append("Soil nutrients appear balanced.")

    return suggestions