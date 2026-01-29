# MB_mule_app - Prompt 1: Recipe Storage API

## Descripcion del Caso de Uso

Aplicacion MuleSoft para recibir, almacenar y confirmar recetas de cocina.

---

## Prompt para el Workflow

```
Develop a MuleSoft application called "recipe-storage-sapi" that implements a Recipe Storage System API.

## Functional Requirements

1. **Endpoint**: POST /api/recipes
   - Receives recipe data in JSON format
   - Required fields: name, ingredients (array), instructions (string), servings (integer)
   - Optional fields: prepTime, cookTime, category, author

2. **Storage**:
   - Save each recipe as a JSON file to the local filesystem
   - File naming convention: {timestamp}_{recipe-name-kebab-case}.json
   - Storage directory: /recipes (configurable via properties)

3. **Response**:
   - Return HTTP 201 Created on success
   - Response body must include:
     - message: "Recipe successfully stored"
     - recipeId: unique identifier
     - filePath: full path where the recipe was saved
     - timestamp: when it was saved

## Non-Functional Requirements

- API Layer: System API (SAPI)
- Error handling for: invalid JSON, missing required fields, file system errors
- Use externalized configuration for the storage path
- Include logging at INFO level for each operation

## Example Request

POST /api/recipes
Content-Type: application/json

{
  "name": "Pasta Carbonara",
  "ingredients": ["spaghetti", "eggs", "pecorino cheese", "guanciale", "black pepper"],
  "instructions": "Cook pasta. Fry guanciale. Mix eggs with cheese. Combine all.",
  "servings": 4,
  "prepTime": "10 min",
  "cookTime": "20 min",
  "category": "Italian"
}

## Example Response

HTTP 201 Created

{
  "message": "Recipe successfully stored",
  "recipeId": "rec-20260129-093500",
  "filePath": "/recipes/20260129_093500_pasta-carbonara.json",
  "timestamp": "2026-01-29T09:35:00Z"
}
```

---

## Notas para el Workflow

- Este prompt está diseñado para el workflow `MB_mule_app`
- Los agentes consultarán la documentación en `mule-docs/` para seguir los estándares
- El QAVerifier validará contra las convenciones de naming y estructura de proyecto
