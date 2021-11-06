## Pedoman Kontribusi
1. Fork repositori ini dan clone di komputer anda
2. Buat virtual environment dengan menulis `python -m venv venv` di terminal/cmd
3. Buat branch baru dari `development` brach dan checkout pada branch yang baru anda buat
4. Install package yang dibutuhkan. Package ini disimpan di file requirements.txt dengan menulis `pip install -r requirements.txt` di terminal/cmd
5. Setelah packagenya selesai di install, lakukan migrasi untuk pertama kali dengan menulis `python manage.py makemigrations`, dan finalisasi migrasi dengan menulis `python manage.py migrate`
6. Buka file `settings.py` yang ada pada folder `ads_api`. Cari variabel `DEBUG` dan ubah nilainya menjadi `TRUE`
7. Jalankan project dengan menuliskan `python manage.py runserver` di terminal/cmd
8. Create and commit your changes Buat dan commit perubahan yang telah anda lakukan
9. Push commit yang telah anda buat ke repositori yang telah anda fork di GitHub
10. Buat Pull Request dengan membandingkan branch yang anda buat terhadap branch `development`
