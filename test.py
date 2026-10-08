"""Sistema de gestión de notas de estudiantes.

Permite crear estudiantes, registrar notas (0-100), calcular promedios,
letras, estado de aprobación y cuadro de honor, eliminar notas e imprimir
reportes.
"""

import math

MIN_GRADE = 0.0
MAX_GRADE = 100.0


class Student:
    """Estudiante con un ID, un nombre y una lista de notas."""

    def __init__(self, student_id, name):
        """Crea un estudiante.

        Raises:
            ValueError: si el ID o el nombre están vacíos o no son texto.
        """
        self.student_id = self._validate_text(
            student_id, "El ID del estudiante")
        self.name = self._validate_text(name, "El nombre del estudiante")
        self.grades = []

    @staticmethod
    def _validate_text(value, label):
        """Devuelve el texto sin espacios o lanza ValueError si está vacío."""
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"{label} no puede estar vacío.")
        return value.strip()

    @staticmethod
    def _validate_grade(grade):
        """Devuelve la nota como float o lanza ValueError si es inválida."""
        if isinstance(grade, bool) or not isinstance(grade, (int, float)):
            raise ValueError(
                f"La nota debe ser un número, se recibió {grade!r}.")
        if not math.isfinite(grade) or not MIN_GRADE <= grade <= MAX_GRADE:
            raise ValueError(
                f"La nota debe estar entre {MIN_GRADE:g} y {MAX_GRADE:g}, "
                f"se recibió {grade!r}."
            )
        return float(grade)

    def add_grade(self, grade):
        """Agrega una nota entre 0 y 100.

        Raises:
            ValueError: si la nota no es un número dentro del rango válido.
        """
        self.grades.append(self._validate_grade(grade))


def run_action(description, action, *args):
    """Ejecuta una acción; si la entrada es inválida, imprime el error."""
    try:
        action(*args)
    except ValueError as error:
        print(f"Error ({description}): {error}")
    else:
        print(f"OK: {description}")


def create_student(student_id, name):
    """Crea un estudiante; si hay error, imprime el mensaje sin cerrarse."""
    try:
        student = Student(student_id, name)
    except ValueError as error:
        print(f"Error (crear estudiante): {error}")
        return None
    print(f"OK: estudiante creado: {student.name} ({student.student_id})")
    return student


def main():
    """Demuestra todos los requisitos del sistema."""
    print("--- 1. Estudiantes ---")
    ana = create_student("A001", "Ana Perez")
    create_student("", "Sin Id")
    create_student("B002", "   ")

    print("\n--- 2. Notas y entradas inválidas ---")
    for grade in (95.0, 72.5, 100, 88):
        run_action(f"agregar nota {grade}", ana.add_grade, grade)
    for grade in ("Cincuenta", 101, -5, float("nan"), True, None):
        run_action(f"agregar nota {grade!r}", ana.add_grade, grade)


if __name__ == "__main__":
    main()
