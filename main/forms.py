from django.forms import ModelForm, TextInput, Textarea, URLInput
from django.core.exceptions import ValidationError
from django.utils.html import strip_tags

from main.models import Education, Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            "title",
            "description",
            "tech_stack",
            "project_url",
            "project_image_url",
        ]

        labels = {
            "title": "Nama Proyek",
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
                    "placeholder": "https://github.com/kakBurhan/burhanquestv4",
                }
            ),
            "project_image_url": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000",
                }
            ),
        }

    def clean_title(self):
        title = strip_tags(self.cleaned_data["title"]).strip()
        if not title:
            raise ValidationError("Nama proyek tidak boleh hanya berisi tag HTML.")
        return title

    def clean_tech_stack(self):
        tech_stack = strip_tags(self.cleaned_data["tech_stack"]).strip()
        return tech_stack
    
    def clean_description(self):
        description = strip_tags(self.cleaned_data["description"]).strip()
        return description


class EducationForm(ModelForm):
    class Meta:
        model = Education
        fields = [
            "institution",
            "degree",
            "start_year",
            "end_year",
            "description",
            "logo",
        ]

        labels = {
            "institution": "Nama Institusi",
            "degree": "Jenjang Pendidikan",
            "start_year": "Tahun Mulai",
            "end_year": "Tahun Selesai",
            "description": "Deskripsi",
            "logo": "Logo Institusi",
        }

        widgets = {
            "institution": TextInput(
                attrs={
                    "placeholder": "Universitas Indonesia",
                    "maxlength": 255,
                }
            ),
            "degree": TextInput(
                attrs={
                    "placeholder": "S1 - Ilmu Komputer",
                    "maxlength": 255,
                }
            ),
            "start_year": TextInput(
                attrs={
                    "placeholder": "tahun-bulan-tanggal",
                    "maxlength": 255,
                }
            ),
            "end_year": TextInput(
                attrs={
                    "placeholder": "tahun-bulan-tanggal",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "deskripsi",
                    "rows": 3,
                }
            ),
            "logo": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000",
                }
            ),
        }

    def clean_institution(self):
        institution = strip_tags(self.cleaned_data["institution"]).strip()
        if not institution:
            raise ValidationError("Nama institusi tidak boleh hanya berisi tag HTML.")
        return institution

    def clean_degree(self):
        degree = strip_tags(self.cleaned_data["degree"]).strip()
        if not degree:
            raise ValidationError("Degree tidak boleh hanya berisi tag HTML.")
        return degree

    def clean_description(self):
        description = strip_tags(self.cleaned_data["description"] or "").strip()
        return description

    def clean(self):
        cleaned_data = super().clean()
        start_year = cleaned_data.get("start_year")
        end_year = cleaned_data.get("end_year")
        if start_year and end_year and end_year < start_year:
            self.add_error("end_year", "Tahun selesai tidak boleh lebih awal dari tahun mulai.")
        return cleaned_data