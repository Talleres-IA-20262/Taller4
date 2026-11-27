"""Punto 5. Inferencia mediante encadenamiento hacia adelante."""
from models.logic import match_premises, substitute


def forward_chain(kb):
    """Retorna una tupla con los hechos originales y derivados, sin duplicados.

    Cada ronda usa los hechos disponibles al comenzarla. La base de entrada
    debe conservarse.
    kb.facts contiene objetos Atom; kb.rules contiene objetos Rule con los
    atributos premises y conclusion. Los hechos se comparan directamente.

    Tips:
    - match_premises(regla.premises, hechos) genera (sustitución, hechos usados).
      Si no hay coincidencias, no genera resultados. La sustitución es un
      diccionario, por ejemplo {'?p': 'ana'}.
    - substitute(regla.conclusion, sustitución) retorna un nuevo objeto Atom
      con las variables reemplazadas por los valores de la sustitución.
    """
    facts = list(dict.fromkeys(kb.facts))
    known = set(facts)

    while True:
        new_facts = []
        new_set = set()

        for rule in kb.rules:
            for substitution, _ in match_premises(rule.premises, facts):
                conclusion = substitute(rule.conclusion, substitution)

                if conclusion not in known and conclusion not in new_set:
                    new_facts.append(conclusion)
                    new_set.add(conclusion)

        if not new_facts:
            return tuple(facts)

        facts.extend(new_facts)
        known.update(new_set)
