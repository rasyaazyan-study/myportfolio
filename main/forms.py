from django.forms import ModelForm, TextInput, Textarea, Select, DateTimeInput, URLInput

from main.models import Experience, Education, Contact, Message, Project, Design

class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = [
            "title",
            "organization",
            "description",
            "category",
            "thumbnail",
            "thumbnail_url",
            "started_at",
            "ended_at",
        ]

        labels = {
            "title": "Posisi Pada Organisasi",
            "organization": "Organisasi/Instansi",
            "description": "Deskripsi Pengalaman",
            "category": "Kategori Pengalaman",
            "thumbnail": "File Foto Berkaitan",
            "thumbnail_url": "Link Foto Berkaitan",
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
            "thumbnail_url": URLInput (
                attrs={
                    "placeholder": "https://rasya-azyan.png"
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
            "thumbnail_url",
            "started_at",
            "ended_at",
        ]

        labels = {
            "institution": "Institusi Pendidikan",
            "description": "Deskripsi Pengalaman",
            "category": "Jenjang Pendidikan",
            "thumbnail": "File Foto Berkaitan",
            "thumbnail_url": "Link Foto Berkaitan",
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
            "thumbnail_url": URLInput (
                attrs={
                    "placeholder": "https://rasya-azyan.png"
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

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            "title",
            "role",
            "description",
            "tech_stack",
            "project_url",
            "project_image_url",
        ]

        labels = {
            "title": "Nama Proyek",
            "role": "Peran Saya",
            "description": "Deskripsi Proyek",
            "tech_stack": "Teknologi yang Digunakan",
            "project_url": "URL Proyek",
            "project_image_url": "URL Gambar Proyek",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Portfolio Website",
                    "maxlength": 255,
                }
            ),
            "role": Select(
                choices={
                    "placeholder": Project.ROLE_CHOICES,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Ceritakan Proyekmu",
                    "rows": 3,
                }
            ),
            "tech_stack": TextInput(
                attrs={
                    "placeholder": "Django, Python, HTML, CSS",
                }
            ),
            "project_url": URLInput(
                attrs={
                    "placeholder": "https://github.com/rasyaazyan/pacilisthebest",
                }
            ),
            "project_image_url": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000",
                }
            ),
        }
        
class DesignForm(ModelForm):
    class Meta:
        model = Design
        fields = [
            'title',
            'tools',
            'category',
            'project_url',
            'project_image_url'
        ]
        
        labels = {
            "title": "Nama Desain",
            "tools": "Alat yang Digunakan",
            "category": "Jenis Pekerjaan",
            "project_url": "URL Proyek",
            "project_image_url": "URL Gambar Proyek",
        }
        
        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Nama Desain",
                    "maxlength": 255,
                }
            ),
            "tools": TextInput(
                attrs={
                    "placeholder": "Software Yang Digunakan",
                    "maxlength": 255,
                }
            ),
            "category": Select(
                choices={
                    "placeholder": Design.CATEGORY_CHOICES,
                }
            ),
            "design_url": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000",
                }
            ),
            "design_image_url": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000",
                }
            ),
        }
        
class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = [
            "sender",
            "to",
            "value",
        ]
        
        labels = {
            "sender": "Dari",
            "to": "Untuk",
            "value": "Pesan",
        }
        
        widgets = {
            "sender": TextInput(
                attrs={
                    "placeholder": "Anonim (Opsional)",
                }
            ),
            "to": TextInput(
                attrs={
                    "placeholder": "Semua (Opsional)",
                }
            ),
            "value": TextInput(
                attrs={
                    "placeholder": "Tulis pesanmu"
                }
            )
        }