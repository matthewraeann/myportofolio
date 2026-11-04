from django.utils.html import strip_tags
from rest_framework import serializers

from main.models import Education, Project


class StarFieldsMixin(serializers.Serializer):
    """Field star read-only yang dipakai bersama oleh Project dan Education.

    Model yang memakai mixin ini wajib punya relasi ``starred_by`` ke User.
    Ketiga field dihitung dari ``obj.starred_by.all()``, sehingga jika view
    memakai ``prefetch_related("starred_by")`` tidak ada query tambahan per
    objek. Hanya username yang ditampilkan; email dan password tidak ikut.
    """

    star_count = serializers.SerializerMethodField()
    is_starred = serializers.SerializerMethodField()
    starred_by_names = serializers.SerializerMethodField()

    def get_star_count(self, obj):
        return len(obj.starred_by.all())

    def get_is_starred(self, obj):
        request = self.context.get("request")
        if request is None or not request.user.is_authenticated:
            return False
        return any(user.pk == request.user.pk for user in obj.starred_by.all())

    def get_starred_by_names(self, obj):
        return ", ".join(user.username for user in obj.starred_by.all())


class ProjectSerializer(StarFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = [
            "id", "title", "description", "tech_stack",
            "project_url", "project_image_url",
            "star_count", "is_starred", "starred_by_names",
        ]
        read_only_fields = ["id"]

    def validate_title(self, value):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError("Title cannot be empty.")
        return value

    def validate_description(self, value):
        return strip_tags(value)

    def validate_tech_stack(self, value):
        return strip_tags(value)


class EducationSerializer(StarFieldsMixin, serializers.ModelSerializer):
    """Representasi dan validasi data Education untuk API /api/v1/educations/.

    Input teks dibersihkan dengan ``strip_tags`` seperti ``clean_<field>`` di
    ``EducationForm``. ``starred_by`` sengaja tidak dimasukkan ke ``fields``,
    sehingga star hanya bisa diubah lewat endpoint star.
    """

    is_ongoing = serializers.ReadOnlyField()

    class Meta:
        model = Education
        fields = [
            "id", "institution", "degree", "start_year", "end_year",
            "is_ongoing", "description", "logo",
            "star_count", "is_starred", "starred_by_names",
        ]
        read_only_fields = ["id"]

    def validate_institution(self, value):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError("Nama institusi tidak boleh hanya berisi tag HTML.")
        return value

    def validate_degree(self, value):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError("Degree tidak boleh hanya berisi tag HTML.")
        return value

    def validate_description(self, value):
        return strip_tags(value or "").strip()

    def validate(self, attrs):
        # Saat PATCH, field yang tidak dikirim diambil dari data lama (self.instance)
        start_year = attrs.get("start_year", getattr(self.instance, "start_year", None))
        end_year = attrs.get("end_year", getattr(self.instance, "end_year", None))
        if start_year and end_year and end_year < start_year:
            raise serializers.ValidationError(
                {"end_year": "Tahun selesai tidak boleh lebih awal dari tahun mulai."}
            )
        return attrs
