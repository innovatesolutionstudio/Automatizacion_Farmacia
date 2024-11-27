import requests

# Definir la URL de la API de ejemplo
url = "https://www.thecocktaildb.com/api/json/v1/1/search.php?s=margarita"

# Realizar la solicitud GET
payload = {}
headers = {}
response = requests.request("GET", url, headers=headers, data=payload)

# Imprimir el código de estado de la respuesta
print(response.status_code)

# Test case 1: Verificar status code 200
def test_status_code():
    esperado = 200
    actual = response.status_code
    assert esperado == actual, f"Falla: Esperado: {esperado}, actual: {actual}"

# Test case 2: Verificar que el nombre strDrink sea "margarita"
def test_verify_drink_name():
    response_json = response.json()
    esperado = "Margarita"
    actual = response_json["drinks"][0]["strDrink"]
    assert esperado == actual, f"Falla: Esperado: {esperado}, actual: {actual}"

# Test case 3 (Opcional): Verificar un valor anidado, en este caso el primer ingrediente sea "Tequila"
def test_verify_ingredient():
    response_json = response.json()
    esperado = "Tequila"
    actual = response_json["drinks"][0]["strIngredient1"]
    assert esperado == actual, f"Falla: Esperado: {esperado}, actual: {actual}"

# Ejecutar los test cases
test_status_code()
test_verify_drink_name()
test_verify_ingredient()
