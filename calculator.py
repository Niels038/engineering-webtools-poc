# -*- coding: utf-8 -*-


def bereken_a_plus_b(input_data):
    a = input_data["a"]
    b = input_data["b"]

    c = a + b

    result_data = {
        "a": a,
        "b": b,
        "c": c,
        "status": "Berekend"
    }

    return result_data