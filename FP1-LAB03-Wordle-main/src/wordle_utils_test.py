from wordle_utils import obtener_pistas,marcar_verdes,marcar_amarillos


def test_es_palabra_valida():
    print("Probando es_palabra_valida...")
    assert es_palabra_valida("casar") == True
    assert es_palabra_valida("casa") == False
    assert es_palabra_valida("casarr") == False
    assert es_palabra_valida("c4sar") == False
    assert es_palabra_valida("casa ") == False
    assert es_palabra_valida(" casa") == False
    assert es_palabra_valida("CASAR") == True



def test_marcar_verdes():
    print("Probando marcar_verdes...")
    assert marcar_verdes("casar", "polio") == ("_____", "casar")
    assert marcar_verdes("casar", "casar") == ("VVVVV", "")
    assert marcar_verdes("casar", "cazar") == ("VV_VV", "s")
    assert marcar_verdes("casar", "secta") == ("_____", "casar")
    assert marcar_verdes("casar", "sacar") == ("_V_VV","cs")
    assert marcar_verdes("casar", "peras") == ("___V_", "csar")

def test_marcar_amarillos():
    print("Probando marcar_amarillos...")
    assert marcar_amarillos("polio", "_____", "casar") == "_____"
    assert marcar_amarillos("casar", "VVVVV", "") == "VVVVV"
    assert marcar_amarillos("cazar", "VV_VV", "s") == "VV_VV"
    assert marcar_amarillos("secta", "_____", "casar") == "A_A_A"
    assert marcar_amarillos("sacar", "_V_VV", "cs") == "AVAVV"
    assert marcar_amarillos("peras", "___V_", "csar") == "__AVA"

def test_obtener_pistas():
    print("Probando obtener_pistas...")
    assert obtener_pistas("casar", "polio") == "_____"
    assert obtener_pistas("casar", "casar") == "VVVVV"
    assert obtener_pistas("casar", "cazar") == "VV_VV"
    assert obtener_pistas("casar", "secta") == "A_A_A"
    assert obtener_pistas("casar", "sacar") == "AVAVV"
    assert obtener_pistas("casar", "peras") == "__AVA"


print("✅Todas las pruebas pasaron correctamente.")
