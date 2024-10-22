from django.test import TestCase
from django.contrib.auth.models import User
from .models import Note

class NoteTestCase(TestCase):

    def setUp(self):
        # Crear un usuario para asignar a las notas
        self.user = User.objects.create_user(username='testuser', password='12345')
        # Crear dos notas de ejemplo
        self.note1 = Note.objects.create(user=self.user, title="Nota 1", content="Contenido de la nota 1")
        self.note2 = Note.objects.create(user=self.user, title="Nota 2", content="Contenido de la nota 2")

    def test_create_note(self):
        """Test para la creación de una nueva nota"""
        note = Note.objects.create(user=self.user, title="Nueva Nota", content="Contenido de la nueva nota")
        self.assertEqual(note.title, "Nueva Nota")
        self.assertEqual(note.content, "Contenido de la nueva nota")

    def test_update_note(self):
        """Test para la actualización de datos de una nota existente"""
        self.note1.title = "Nota 1 Actualizada"
        self.note1.content = "Contenido actualizado"
        self.note1.save()

        updated_note = Note.objects.get(pk=self.note1.pk)
        self.assertEqual(updated_note.title, "Nota 1 Actualizada")
        self.assertEqual(updated_note.content, "Contenido actualizado")

    def test_view_note_detail(self):
        """Test para la visualización de detalles de una nota"""
        note = Note.objects.get(pk=self.note1.pk)
        self.assertEqual(note.title, "Nota 1")
        self.assertEqual(note.content, "Contenido de la nota 1")

    def test_delete_note(self):
        """Test para la eliminación de una nota"""
        note_id = self.note1.pk
        self.note1.delete()
        with self.assertRaises(Note.DoesNotExist):
            Note.objects.get(pk=note_id)

    def test_list_notes(self):
        """Test para la carga de la lista de notas"""
        notes = Note.objects.filter(user=self.user)
        self.assertEqual(notes.count(), 2)
        self.assertIn(self.note1, notes)
        self.assertIn(self.note2, notes)