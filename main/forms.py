from django.forms import ModelForm, TextInput, Textarea, Select, DateTimeInput, URLInput

from main.models import Experience
from main.models import Education
from main.models import Contact

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
        
class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = [
            "name",
            "category",
            "value",
            "url"
        ]
        
        labels = {
            "name": "Nama Kontak",
            "category": "Jenis Kontak",
            "value": "Nomor/Username Kontak",
            "url": "Link Kontak"
        }
        
        widgets = {
            "name": TextInput(
                attrs={
                    "placeholder": "Linkedin Pribadi",
                    "maxlength": 100,
                }
            ),
            "value": TextInput(
                attrs={
                    "placeholder": "Linkedin Pribadi",
                    "maxlength": 255,
                }
            ),
            "url": URLInput(
                attrs={
                    "placeholder": "https://linkedin.com/in/rasyaazyan"
                }
            )
        }