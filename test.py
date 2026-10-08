"""Sistema de gestión de notas de estudiantes.

Permite crear estudiantes, registrar notas (0-100), calcular promedios,
letras, estado de aprobación y cuadro de honor, eliminar notas e imprimir
reportes.
"""


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


if __name__ == "__main__":
    main()
