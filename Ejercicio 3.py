from typing import List, Dict

def operar_conjuntos(a: List[int], b: List[int]) -> Dict[str, List[int]]:
    """
    Calcula intersección, unión y diferencia simétrica usando conjuntos.
    Devuelve listas ordenadas para que el resultado sea estable.
    """
    s1, s2 = set(a), set(b)                 # quitar duplicados
    return {
        "interseccion":        sorted(s1 & s2),  # AND de conjuntos
        "union":               sorted(s1 | s2),  # OR de conjuntos
        "diferencia_simetrica": sorted(s1 ^ s2), # XOR de conjuntos
    }

if __name__ == "__main__":
    # Prueba 
    l1 = [1, 2, 2, 3, 5, 8]
    l2 = [2, 3, 4, 8, 8, 9]
    resultado = operar_conjuntos(l1, l2)
    for k, v in resultado.items():
        print(f"{k}: {v}")

    # Asserts mínimos (sirven de “test”)
    assert resultado["interseccion"] == [2, 3, 8]
    assert resultado["union"] == [1, 2, 3, 4, 5, 8, 9]
    assert resultado["diferencia_simetrica"] == [1, 4, 5, 9]
    print("✅ Tests OK")
