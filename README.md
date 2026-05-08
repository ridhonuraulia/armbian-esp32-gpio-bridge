# armbian-esp32-gpio-bridge
A lightweight Serial-to-GPIO bridge turning an ESP32 into a physical I/O extension for Armbian-based Set-Top Boxes (e.g., ZTE B860H) via UART.
# Armbian ESP32 GPIO Bridge

Sebuah antarmuka ringan untuk memberikan kemampuan pin GPIO fisik pada Single Board Computer atau Set-Top Box (seperti ZTE B860H) yang menjalankan OS Linux/Armbian, dengan memanfaatkan ESP32 sebagai *slave* melalui komunikasi serial (UART).

Proyek ini tidak peduli apakah Anda menggunakannya untuk menyalakan relay, membaca sensor, atau sekadar menyalakan LED. Fokus repository ini hanya satu: mengirim perintah dari terminal Linux ke ESP32 secara stabil dan mudah di-compile.

## ⚠️ Limitasi & Peringatan
Mari bersikap realistis sebelum menggunakan *bridge* ini:
1. **Bukan untuk High-Speed Data:** Mengingat ini menggunakan protokol Serial (UART) standar, jangan gunakan *bridge* ini untuk membaca sinyal PWM frekuensi tinggi atau protokol I2C/SPI yang sangat cepat. Ada latensi komunikasi yang harus diperhitungkan.
2. **Logic Level 3.3V:** Pin GPIO ESP32 beroperasi pada tegangan 3.3V. Gunakan *logic level converter* jika Anda menghubungkannya ke komponen 5V.

## Arsitektur Singkat
`[Armbian SBC/STB] <---(Kabel USB-to-TTL / UART)---> [ESP32] <---> [Komponen Fisik]`

## 1. Instalasi Sisi ESP32 (Microcontroller)
Kompilasi kode ini dibuat sesederhana mungkin tanpa *toolchain* yang berat.
1. Buka file `esp32_firmware/esp32_firmware.ino` menggunakan Arduino IDE.
2. Pastikan Anda memilih board **ESP32 Dev Module**.
3. *Compile* dan *Upload* ke ESP32.

## 2. Koneksi Perangkat Keras (Wiring)
Hubungkan STB ke ESP32 menggunakan modul USB-to-TTL (CP2102/CH340) atau langsung melalui pin UART yang tersedia di STB.

| USB-to-TTL / STB | ESP32 Pin | Catatan |
| :--- | :--- | :--- |
| TX | RX0 | Silang (Crossover) |
| RX | TX0 | Silang (Crossover) |
| GND | GND | Wajib terhubung (Common Ground) |

*Catatan: Jangan hubungkan pin 5V dari USB-to-TTL ke pin 3.3V ESP32 jika ESP32 sudah mendapat daya dari port USB-nya sendiri.*

## 3. Penggunaan di Sisi Armbian (Host)
Pastikan perangkat terdeteksi di lingkungan Linux Anda. Buka terminal (CLI) dan jalankan:

```bash
ls /dev/ttyUSB*


perlu diperhatikan juga ini pengguaan menggunakan brige ROS 2 HUMBEL DIDASARI OLEH MICRO-ROS.KAMU JUGA BISA MENGGUNAKAN LAPTOP/KOMPUTER SEBAGAI BRIGE UNTUK INI.
