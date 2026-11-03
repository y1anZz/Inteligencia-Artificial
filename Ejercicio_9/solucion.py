import yaml
import re

def analizar_atomo(s):
    m = re.match(r"(\w+)\(([^)]+)\)", s)
    return m.group(1), [x.strip() for x in m.group(2).split(',')]

def unificar(a1, a2):
    p1, args1 = analizar_atomo(a1)
    p2, args2 = analizar_atomo(a2)
    if p1 != p2 or len(args1) != len(args2): return None
    sub = {}
    for x, y in zip(args1, args2):
        if x[0].islower():
            if x in sub and sub[x] != y: return None
            sub[x] = y
        elif x != y: return None
    return sub

def evaluar_premisas(premisas, hechos, sub, idx, resultados):
    if idx == len(premisas):
        resultados.append(sub.copy())
        return
    pb, pa = analizar_atomo(premisas[idx])
    subbed = f"{pb}({','.join(sub.get(a, a) for a in pa)})"
    for f in hechos:
        s = unificar(subbed, f)
        if s is not None:
            nueva_sub = sub.copy()
            nueva_sub.update(s)
            evaluar_premisas(premisas, hechos, nueva_sub, idx+1, resultados)

def hacia_adelante(hechos, reglas):
    conocidos = list(hechos)
    traza = []
    while True:
        nuevos_ronda = []
        for r_id, premisas, cabeza in reglas:
            resultados = []
            evaluar_premisas(premisas, conocidos, {}, 0, resultados)
            for res in resultados:
                hb, ha = analizar_atomo(cabeza)
                hsub = f"{hb}({','.join(res.get(a,a) for a in ha)})"
                if hsub not in conocidos and hsub not in nuevos_ronda:
                    nuevos_ronda.append(hsub)
                    traza.append(f"Regla {r_id} -> {hsub}")
        if not nuevos_ronda:
            break
        conocidos.extend(nuevos_ronda)
    return conocidos, traza

def hacia_atras(meta, hechos, reglas, visitados=None):
    if visitados is None: visitados = []
    if meta in hechos: return True, [f"Hecho: {meta}"]
    if meta in visitados: return False, [f"Ciclo evitado: {meta}"]
    traza = [f"Buscando meta: {meta}"]
    for r_id, premisas, cabeza in reglas:
        s = unificar(cabeza, meta)
        if s is not None:
            traza.append(f"Probando {r_id}")
            ok = True
            sub_traza = []
            for p in premisas:
                pb, pa = analizar_atomo(p)
                psub = f"{pb}({','.join(s.get(a,a) for a in pa)})"
                ok_p, t_p = hacia_atras(psub, hechos, reglas, visitados + [meta])
                sub_traza.extend(t_p)
                if not ok_p:
                    ok = False
                    break
            if ok: return True, traza + sub_traza + [f"Aceptado: {meta}"]
            traza.extend(sub_traza)
            traza.append(f"Fallo en {r_id}")
    return False, traza + [f"No se pudo probar: {meta}"]

if __name__ == '__main__':
    with open('biblioteca.yaml', 'r', encoding='utf-8') as f:
        kb = yaml.safe_load(f)
    hechos = kb['hechos']
    reglas = [(r['id'], r['si'], r['entonces']) for r in kb['reglas']]
    
    print("--- ENCADENAMIENTO HACIA ADELANTE ---")
    conocidos, tr = hacia_adelante(hechos, reglas)
    print("Atomos agregados:")
    for x in tr: print("  +", x)
    for q in ["AccesoNoche(Ana)", "AccesoNoche(Luis)", "AccesoNoche(Marta)"]:
        print(f"Consulta {q}: {'SI (Probada)' if q in conocidos else 'NO (No probada)'}")

    print("\n--- ENCADENAMIENTO HACIA ATRAS ---")
    for q in ["AccesoNoche(Ana)", "AccesoNoche(Luis)", "AccesoNoche(Marta)"]:
        ok, tr = hacia_atras(q, hechos, reglas)
        print(f"\nConsulta {q}: {'SI' if ok else 'NO'}")
        for t in tr: print("  ", t)
