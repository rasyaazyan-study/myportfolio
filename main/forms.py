from django.forms import ModelForm, TextInput, Textarea, URLInput, Select, DateTimeInput

from main.models import Experience

from main.models import Education

class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = [
            "title",
            "organization",
            "description",
            "category",
            "thumbnail",
            "started_at",
            "ended_at",
        ]

        labels = {
            "title": "Posisi Pada Organisasi",
            "organization": "Organisasi/Instansi",
            "description": "Deskripsi Pengalaman",
            "category": "Kategori Pengalaman",
            "thumbnail": "File Foto Berkaitan",
            "started_at": "Tanggal Mulai",
            "ended_at": "Tanggal Akhir",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Pengurus Organisasi",
                    "maxlength": 255,
                }
            ),
            "organization": TextInput(
                attrs={
                    "placeholder": "Fasilkom UI",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Ceritakan Pengalamanmu",
                    "rows": 3,
                }
            ),
            "category": Select(
                choices={
                    "placeholder": Experience.EXPERIENCE_CHOICES,
                }
            ),
            "thumbnail": URLInput(
                attrs={
                    "placeholder": "https://...",
                }
            ),
            "started_at": DateTimeInput(
                attrs={
                    "placeholder": "datetime-local",
                }
            ),
            "ended_at": DateTimeInput(
                attrs={
                    "placeholder": "datetime-local",
                }
            ),
        }
        
class EducationForm(ModelForm):
    class Meta:
        model = Education
        fields = [
            "institution",
            "description",
            "category",
            "thumbnail",
            "started_at",
            "ended_at",
        ]

        labels = {
            "institution": "Institusi Pendidikan",
            "description": "Deskripsi Pengalaman",
            "category": "Jenjang Pendidikan",
            "thumbnail": "File Foto Berkaitan",
            "started_at": "Tanggal Mulai",
            "ended_at": "Tanggal Akhir",
        }

        widgets = {
            "institution": TextInput(
                attrs={
                    "placeholder": "Universitas Indonesia",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Ceritakan Pengalamanmu",
                    "rows": 3,
                }
            ),
            "category": Select(
                choices={
                    "placeholder": Education.EDUCATION_CHOICES,
                }
            ),
            "thumbnail": URLInput(
                attrs={
                    "placeholder": "https://...",
                }
            ),
            "started_at": DateTimeInput(
                attrs={
                    "placeholder": "datetime-local",
                }
            ),
            "ended_at": DateTimeInput(
                attrs={
                    "placeholder": "datetime-local",
                }
            ),
        }