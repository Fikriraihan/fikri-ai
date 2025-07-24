# 📁 Project: OTB Suite

- **Periode:** 2024
- **Perusahaan:** Planet Surf (PT Planet Selancar Mandiri)
- **Peran:** Frontend Developer

## 🧩 Problem / Pain Points

- Tim OTB kesulitan mengelola data estimasi stok secara real-time.
- Proses forecasting masih dilakukan manual di spreadsheet besar.
- Tidak ada sistem filtering dan validasi yang cepat untuk analisis data besar.
- Sulit menampilkan data dalam jumlah besar secara responsif.

## 💡 Solution

- Membangun platform web dengan fitur upload, filter, dan tampilan tabel interaktif.
- Menyediakan validasi otomatis untuk data yang diunggah.
- Implementasi infinite scroll, pagination, dan fitur export Excel.
- Penyusunan tampilan IHB & PD secara modular per fase agar mudah diekspansi.

## ✨ Features

- Upload file retur, target, dan closing stock.
- Tabel interaktif dengan pagination, zoom, dan filter.
- Laporan IHB, PD1/PD2/PD3 dan parameter berdasarkan data upload.
- Validasi format dan konten file sebelum proses lebih lanjut.
- Export data hasil olahan ke Excel.

## 📈 Success Metrics

- ⏱️ 80% lebih cepat dibanding proses forecasting manual sebelumnya.
- 🧩 Mengurangi human error pada proses input data secara signifikan.
- 📊 Meningkatkan adopsi tools internal oleh tim OTB sejak minggu ke-2 deploy.
- 🧠 Dapat menangani ribuan baris data tanpa lag.

## 🔧 Tools & Stack

- React.js + TypeScript + Vite
- Zustand (state), React Query (data)
- Tailwind CSS + Mantine UI
- Backend: API internal perusahaan
