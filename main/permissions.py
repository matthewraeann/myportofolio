from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsPortfolioOwnerOrReadOnly(BasePermission):
    message = "Only the portfolio owner can change projects."

    def has_permission(self, request, view):
        return (
            request.method in SAFE_METHODS
            or request.user.is_superuser
        )


class IsPortfolioOwnerOrEditorOrReadOnly(BasePermission):
    """Hak akses empat peran dari Tugas 4 untuk endpoint daftar dan detail.

    - Pengunjung dan pengguna biasa: hanya boleh membaca (GET, HEAD, OPTIONS).
    - Editor (anggota Group "Editor"): boleh membaca dan mengubah (PUT, PATCH).
    - Pemilik portofolio (superuser): boleh semua method, termasuk POST dan DELETE.

    Star tidak diatur di sini, karena endpoint star memakai IsAuthenticated.
    """

    message = (
        "Hanya pemilik portofolio yang dapat menambah atau menghapus data. "
        "Editor hanya dapat mengubah data."
    )

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        if not request.user.is_authenticated:
            return False
        if request.user.is_superuser:
            return True
        return (
            request.method in ("PUT", "PATCH")
            and request.user.groups.filter(name="Editor").exists()
        )
