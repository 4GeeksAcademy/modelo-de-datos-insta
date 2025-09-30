import sys
import os
from eralchemy2 import render_er
from models import db, User, Post, Comment, Like  # importar mis modelos

try:
    # Generar el diagrama directamente a partir de los modelos de SQLAlchemy
    render_er(db.Model, 'diagram.png')
    print("✅ Diagrama generado correctamente en diagram.png")
except Exception as e:
    print("❌ Error al generar el diagrama:", e)
    raise e
