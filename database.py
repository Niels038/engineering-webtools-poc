# -*- coding: utf-8 -*-

import os
import json
import sqlite3
from datetime import datetime


base_folder = os.path.dirname(__file__)
data_folder = os.path.join(base_folder, "data")
database_path = os.path.join(data_folder, "calculations.db")


def init_database():
    if not os.path.exists(data_folder):
        os.makedirs(data_folder)

    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS calculations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            projectnummer TEXT,
            berekening_naam TEXT,
            tool_naam TEXT,
            input_json TEXT,
            result_json TEXT,
            created_at TEXT
        )
    """)

    conn.commit()
    conn.close()


def save_calculation(projectnummer, berekening_naam, tool_naam, input_data, result_data):
    init_database()

    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    input_json = json.dumps(input_data)
    result_json = json.dumps(result_data)
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
        INSERT INTO calculations (
            projectnummer,
            berekening_naam,
            tool_naam,
            input_json,
            result_json,
            created_at
        )
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        projectnummer,
        berekening_naam,
        tool_naam,
        input_json,
        result_json,
        created_at
    ))

    conn.commit()
    conn.close()


def load_calculations():
    init_database()

    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            id,
            projectnummer,
            berekening_naam,
            tool_naam,
            input_json,
            result_json,
            created_at
        FROM calculations
        ORDER BY id DESC
    """)

    rows = cursor.fetchall()
    conn.close()

    calculations = []

    for row in rows:
        calculations.append({
            "id": row[0],
            "projectnummer": row[1],
            "berekening_naam": row[2],
            "tool_naam": row[3],
            "input_data": json.loads(row[4]),
            "result_data": json.loads(row[5]),
            "created_at": row[6]
        })

    return calculations