from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import Group, User

from main.models import Experience, Education


class MainTest(TestCase):
    def setUp(self):
        self.experience = Experience.objects.create(
            title="Asisten Dosen PBP",
            description="Membantu mahasiswa memahami pengembangan web.",
            category="part-time",
        )
        self.education = Education.objects.create(
            institution="Universitas Indonesia",
            degree="S1 - Ilmu Komputer",
            start_year="2025-01-01",
        )

# Test Main
    def test_main_url_is_accessible(self):
        response = self.client.get(reverse("main:show_main"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertNotContains(response, self.experience.title)
        self.assertContains(response, f'href="{reverse("main:show_experience")}"')

    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/halaman-yang-tidak-ada/")

        self.assertEqual(response.status_code, 404)

# Test Experience
    def test_experience_model(self):
        self.assertEqual(str(self.experience), "Asisten Dosen PBP")
        self.assertEqual(self.experience.category, "part-time")
        self.assertTrue(self.experience.is_ongoing)

    def test_experience_page(self):
        response = self.client.get(reverse("main:show_experience"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience.html")
        self.assertContains(response, self.experience.title)
        self.assertContains(response, self.experience.description)
        self.assertContains(response, "Part-Time")
        self.assertContains(response, "Sedang berlangsung")
        self.assertContains(response, f'href="{reverse("main:show_main")}"')

    def test_empty_experience_page(self):
        Experience.objects.all().delete()
        response = self.client.get(reverse("main:show_experience"))

        self.assertContains(response, "Belum ada pengalaman yang ditambahkan.")

    def test_completed_experience(self):
        self.experience.ended_at = timezone.now()
        self.experience.save()
        response = self.client.get(reverse("main:show_experience"))

        self.assertFalse(self.experience.is_ongoing)
        self.assertContains(response, "Selesai")
        self.assertNotContains(response, "Sedang berlangsung")

# Test Education 
    def test_education_model(self):
        self.assertEqual(str(self.education), "S1 - Ilmu Komputer at Universitas Indonesia")
        self.assertEqual(self.education.start_year, "2025-01-01")
        self.assertTrue(self.education.is_ongoing)

    def test_education_page(self):
        response = self.client.get(reverse("main:show_educations"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "education.html")
        self.assertContains(response, 'id="grid"')
        self.assertContains(response, reverse("main:get_educations_json"))
        self.assertContains(response, f'href="{reverse("main:show_main")}"')

    def test_educations_json(self):
        response = self.client.get(reverse("main:get_educations_json"))

        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(len(data), 1)
        fields = data[0]["fields"]
        self.assertEqual(fields["institution"], self.education.institution)
        self.assertEqual(fields["degree"], self.education.degree)
        self.assertEqual(fields["start_year"], "2025-01-01")
        self.assertIsNone(fields["end_year"])
        self.assertTrue(fields["is_ongoing"])
        self.assertEqual(fields["logo"], "")
        self.assertEqual(fields["star_count"], 0)
        self.assertFalse(fields["is_starred"])

    def test_educations_json_star_info(self):
        user = User.objects.create_user(username="pengguna", password="Rahasia123!")
        self.education.starred_by.add(user)
        self.client.force_login(user)

        fields = self.client.get(reverse("main:get_educations_json")).json()[0]["fields"]

        self.assertEqual(fields["star_count"], 1)
        self.assertTrue(fields["is_starred"])
        self.assertEqual(fields["starred_by_names"], "pengguna")

    def test_educations_json_search(self):
        Education.objects.create(institution="SMA Negeri 8", degree="SMA", start_year="2022-07-01")

        data = self.client.get(reverse("main:get_educations_json"), {"institution": "sma"}).json()

        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["fields"]["institution"], "SMA Negeri 8")

    def test_empty_educations_json(self):
        Education.objects.all().delete()
        response = self.client.get(reverse("main:get_educations_json"))

        self.assertEqual(response.json(), [])

    def test_completed_education(self):
        self.education.end_year = "2029-01-01"
        self.education.save()
        self.education.refresh_from_db()

        fields = self.client.get(reverse("main:get_educations_json")).json()[0]["fields"]

        self.assertFalse(self.education.is_ongoing)
        self.assertFalse(fields["is_ongoing"])
        self.assertEqual(fields["end_year"], "2029-01-01")


class CreateEducationAjaxTest(TestCase):
    def setUp(self):
        self.url = reverse("main:create_education_ajax")
        self.valid_data = {
            "institution": "Universitas Indonesia",
            "degree": "S1 - Ilmu Komputer",
            "start_year": "2025-08-01",
            "end_year": "",
            "description": "Mahasiswa",
            "logo": "",
        }
        self.superuser = User.objects.create_superuser(username="pemilik", password="Rahasia123!")
        self.editor = User.objects.create_user(username="editor", password="Rahasia123!")
        self.editor.groups.add(Group.objects.create(name="Editor"))
        self.user = User.objects.create_user(username="biasa", password="Rahasia123!")

    def test_superuser_can_create(self):
        self.client.force_login(self.superuser)
        response = self.client.post(self.url, self.valid_data)

        self.assertEqual(response.status_code, 201)
        self.assertTrue(Education.objects.filter(pk=response.json()["pk"]).exists())

    def test_other_roles_are_forbidden(self):
        for user in [None, self.user, self.editor]:
            self.client.logout()
            if user:
                self.client.force_login(user)
            response = self.client.post(self.url, self.valid_data)
            self.assertEqual(response.status_code, 403)
        self.assertEqual(Education.objects.count(), 0)

    def test_invalid_data_returns_400_with_errors(self):
        self.client.force_login(self.superuser)
        data = dict(self.valid_data, institution="", start_year="bukan-tanggal")
        response = self.client.post(self.url, data)

        self.assertEqual(response.status_code, 400)
        errors = response.json()["errors"]
        self.assertIn("institution", errors)
        self.assertIn("start_year", errors)

    def test_end_year_before_start_year_rejected(self):
        self.client.force_login(self.superuser)
        response = self.client.post(self.url, dict(self.valid_data, end_year="2024-01-01"))

        self.assertEqual(response.status_code, 400)
        self.assertIn("end_year", response.json()["errors"])

    def test_html_tags_are_stripped(self):
        self.client.force_login(self.superuser)
        payload = '<img src="x" onerror="alert(\'XSS!\')">'

        response = self.client.post(self.url, dict(self.valid_data, institution=payload))
        self.assertEqual(response.status_code, 400)

        response = self.client.post(self.url, dict(self.valid_data, description="Halo <b>dunia</b>"))
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Education.objects.get(pk=response.json()["pk"]).description, "Halo dunia")

    def test_get_not_allowed(self):
        self.client.force_login(self.superuser)
        self.assertEqual(self.client.get(self.url).status_code, 405)
