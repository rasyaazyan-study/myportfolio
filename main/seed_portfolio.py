from main.models import Experience
from main.models import Education
import datetime

Experience.objects.create(
    title="Product & Project Management Member",
    organization="RISTEK Fasilkom UI 2026 | #AmplifyingExcellence",
    description="Sebagai PM member, saya bertanggungjawab dalam mengelola proses enhancement & maintenance fitur Bikun Tracker bersama Lead & Peer. Tahun ini, Bikun Tracker telah mendeploy beberapa fitur yang kami develop berdasarkan market research yang kami lakukan, seperti ETA (Estimated Time of Arrival), Integrasi Bikun Listrik, sampai Nearest Bus Stop Finder untuk memudahkan user mencari halte terdekat. Selain itu, saya juga sempat bertanggungjawab atas proses RISTEK's Main Web Revamping, dimana tahun ini kami membawa penyegaran dan tampilan baru yang lebih playful dan colorful pada web utama RISTEK Fasilkom UI. Pada RISTEK Townhall Q1, saya juga menerima penghargaan Best Growth for PM pada Kuartal I Kepengurusan RISTEK 2026",
    category="part-time",
    thumbnail="/static/img/RISTEK.png",
    started_at=datetime.datetime(2026, 3, 1, tzinfo=datetime.timezone.utc),
    ended_at=None,
)

Experience.objects.create(
    title="App Technology Intern",
    organization="Badak LNG | Member of Pertamina SHU",
    description="Selama menjalankan 2 bulan sesi magang di Badak LNG, saya berpartisipasi aktif dalam mendukung proses desain kebutuhan aplikasi perusahaan bersama Internal System Analyst, dengan membantu menyiapkan draft FDD (Functional Design Document) untuk kebutuhan programmer internal. Selain itu, saya juga ikut berpartisipasi dalam sesi Requirement Elicitation, Demo, dan UAT bersama user dari berbagai departemen (Maintenance, Technical, SHE-Q, dll.). Serta, saya juga membantu IT Section dalam mempersiapkan dokumen TKI dan BPM untuk kebutuhan Audit Internal.",
    category="internship",
    thumbnail="/static/img/Badak LNG.webp",
    started_at=datetime.datetime(2024, 6, 1, tzinfo=datetime.timezone.utc),
    ended_at=datetime.datetime(2024, 8, 1, tzinfo=datetime.timezone.utc),
)

Experience.objects.create(
    title="Ketua OSIS",
    organization="DEVIFO 2023/2024 (OSIS SMA YPVDP)",
    description="Saya terpilih menjadi Ketua OSIS SMA YPVDP selama 1 tahun 1 bulan pada periode 2023/2024 setelah sebelumnya 1 tahun bergabung dengan Devifo sebagai Humas III. Selama periode ini, kami berhasil menjalankan 10 event tahunan dan 1 event bulanan, menjadikan kami sebagai kepengurusan OSIS dengan jumlah kegiatan kerja terbanyak setelah pandemi Covid-19 berakhir.",
    category="part-time",
    thumbnail="/static/img/Logo Devifo.png",
    started_at=datetime.datetime(2023, 10, 1, tzinfo=datetime.timezone.utc),
    ended_at=datetime.datetime(2024, 11, 1, tzinfo=datetime.timezone.utc),
)

Experience.objects.create(
    title="Ketua Panitia",
    organization="GASTRA 2024 (Gebyar Apresiasi Seni Vidatra)",
    description="GASTRA (Gebyar Apresiasi Seni Vidatra), merupakan acara seni tahunan yang menampilkan bakat seni siswa SD, SMP, dan SMA Vidatra. Dalam kegiatan ini, kami berhasil mengelola berbagai tantangan besar seperti perubahan anggaran dan periode pergantian manajemen sekolah dalam waktu yang sama, dengan tetap menjaga ekspektasi audiens dalam rangka meningkatkan euphoria kembalinya GASTRA setelah Pandemi Covid-19 berakhir.",
    category="part-time",
    thumbnail="/static/img/GASTRA.png",
    started_at=datetime.datetime(2024, 2, 1, tzinfo=datetime.timezone.utc),
    ended_at=datetime.datetime(2024, 10, 1, tzinfo=datetime.timezone.utc),
)

#Tugas Individu 2
Education.objects.create(
    institution="SD YPVDP",
    description="SD YPVDP menjadi salah satu bagian penting dalam hidup saya. Di sini, saya bertemu dengan banyak sekali teman-teman yang ternyata saya temui sampai saya lulus SMA. Sekolah ini juga terasa sangat besar, kalau dihitung menggunakan Google Earth, luasnya hampir 50.000 meter persegi, dan sebagian besar wilayahnya adalah taman dan lapangan terbuka, jadi banyak tempat bermain petak umpet, walaupun saya sering tertangkap pertama karena besar, susah bersembunyi, dan susah berlari.",
    thumbnail="/static/img/sd-vidatra.jpeg",
    started_at=datetime.datetime(2013, 6, 1, tzinfo=datetime.timezone.utc),
    ended_at=datetime.datetime(2019, 6, 1, tzinfo=datetime.timezone.utc),
)

Education.objects.create(
    institution="SMP YPVDP",
    description="Terus terang tidak banyak yang berkesan dari sekolah ini, karena dua tahun terakhir saya habiskan dengan bersekolah dari rumah akibat Pandemi Covid-19. Tapi dari sini saya jadi belajar untuk berorganisasi dengan bergabung bersama OSIS. Di tahap ini juga saya mulai mendalami fotografi dan desain grafis, kalau ditanya alasannya jelas karena banyak dispensasi datang dari kegiatan ini, dan workloadnya juga tidak sesusah menjad videographer atau video editor.",
    thumbnail="/static/img/smp-vidatra.jpeg",
    started_at=datetime.datetime(2019, 6, 1, tzinfo=datetime.timezone.utc),
    ended_at=datetime.datetime(2022, 6, 1, tzinfo=datetime.timezone.utc),
)

Education.objects.create(
    institution="SMA YPVDP",
    description="Bagi saya SMA adalah fase terseru selama 19 tahun saya hidup. Di SMA, saya sangat aktif mengikuti organisasi dan kepanitiaan, bahkan saya sempat menjadi Ketua OSIS dan Ketua Panitia beberapa kali. Tapi, yang membuat SMA jadi sangat berkesan adalah karena teman-temannya, setelah 2 tahun kita tidak pernah bertemu, SMA menjadi masa yang paling tepat untuk menghabiskan sisa 3 tahun kebersamaan kami. Bersama dengan teman-teman saya, kami sempat membuat band bernama 'Labirin' yang membawakan lagu-lagu band kenamaan Indonesia tahun 90an sampai 2000an awal.",
    thumbnail="/static/img/sma-vidatra.jpg",
    started_at=datetime.datetime(2022, 6, 1, tzinfo=datetime.timezone.utc),
    ended_at=datetime.datetime(2025, 6, 1, tzinfo=datetime.timezone.utc),
)

Education.objects.create(
    institution="Fasilkom UI",
    description="Setelah menghabiskan 12 tahun di Vidatra (YPVDP), saya akhirnya memutuskan untuk lanjut berkuliah pada program studi S-1 Sistem Informasi, Fakultas Ilmu Komputer Universitas Indonesia. Sejujurnya sangat berat rasanya untuk meninggalkan Bontang, hidup sendiri jauh dari keluarga, dan harus berkenalan dengan teman-teman yang sepenuhnya baru. Tapi, di sini saya rasa orang-orangnya sangat baik, dan saya salut bahwa setiap orang yang saya temui adalah orang-orang ambisius yang sudah memiliki interest atau spesialisasi tersendiri, yang membuat saya menjadi termotivasi untuk bisa lebih career-oriented dan fokus membangun masa depan yang lebih baik bagi saya pribadi, dan itu yang membuat saya sangat bersyukur bisa berada di lingkungan ini",
    thumbnail="/static/img/fasilkom.webp",
    started_at=datetime.datetime(2025, 6, 1, tzinfo=datetime.timezone.utc),
    ended_at=None,
)

print("Seeding selesai:", Experience.objects.count(), "experience total.")