def soil_recommendation(nitrogen, phosphorus, potassium):

    suggestions = []

    if nitrogen < 50:
        suggestions.append("Nitrogen is low. Consider nitrogen fertilizer.")

    if phosphorus < 40:
        suggestions.append("Phosphorus is low. Add phosphate fertilizer.")

    if potassium < 40:
        suggestions.append("Potassium is low. Use potash fertilizer.")

    if not suggestions:
        suggestions.append("Soil nutrients look balanced.")

    return suggestions