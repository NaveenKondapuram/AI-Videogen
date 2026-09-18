from __future__ import annotations

from pathlib import Path
import sqlite3
from typing import Any

DB_PATH = Path(__file__).resolve().parents[1] / "data" / "studio.db"
DB_PATH.parent.mkdir(parents=True, exist_ok=True)


def get_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db() -> None:
    conn = get_connection()
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS generations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            prompt TEXT NOT NULL,
            input_image TEXT,
            result_url TEXT,
            generation_type TEXT NOT NULL,
            status TEXT NOT NULL,
            provider TEXT NOT NULL,
            metadata TEXT,
            created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
        )
        """
    )
    conn.commit()
    conn.close()


def save_generation(record: dict[str, Any]) -> int:
    conn = get_connection()
    cursor = conn.execute(
        """
        INSERT INTO generations (prompt, input_image, result_url, generation_type, status, provider, metadata)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (
            record["prompt"], record.get("input_image"), record.get("result_url"),
            record["generation_type"], record["status"], record["provider"],
            str(record.get("metadata", {})),
        ),
    )
    conn.commit()
    generation_id = cursor.lastrowid
    conn.close()
    return int(generation_id)


def list_generations() -> list[dict[str, Any]]:
    conn = get_connection()
    rows = conn.execute(
        "SELECT id, prompt, input_image, result_url, generation_type, status, provider, created_at FROM generations ORDER BY id DESC"
    ).fetchall()
    conn.close()
    return [dict(row) for row in rows]


def delete_generation(generation_id: int) -> bool:
    conn = get_connection()
    cursor = conn.execute("DELETE FROM generations WHERE id = ?", (generation_id,))
    conn.commit()
    conn.close()
    return cursor.rowcount > 0
