import os
import subprocess
import sys
import venv
import platform

# Sanal ortam klasörü
VENV_DIR = "env"

# Gerekli kütüphaneler ve sürümleri
REQUIREMENTS = [
    "opencv-python>=4.5.0",
    "numpy>=1.21.0",
    "pandas>=1.3.0",
    "scikit-learn>=1.0.0",
    "deepface>=0.0.79",
    "matplotlib>=3.4.0",
    "Pillow>=9.0.0",
    "tk"
]

# Uygulama dosyası
APP_FILENAME = "face_app.py"

def enable_powershell_execution_policy():
    if os.name == "nt":
        print("🔐 PowerShell yürütme izni veriliyor...")
        subprocess.call([
            "powershell",
            "Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser -Force"
        ])

def create_virtual_env():
    if not os.path.exists(VENV_DIR):
        print("🔧 Sanal ortam oluşturuluyor...")
        venv.create(VENV_DIR, with_pip=True)
        print("✅ Sanal ortam oluşturuldu.")
    else:
        print("ℹ️ Sanal ortam zaten mevcut, atlanıyor.")

def install_requirements():
    print("📦 Gerekli kütüphaneler yükleniyor...")

    # Sanal ortam içindeki Python ve pip yolları
    python_executable = os.path.join(VENV_DIR, "Scripts", "python") if os.name == "nt" else os.path.join(VENV_DIR, "bin", "python")

    try:
        subprocess.check_call([python_executable, "-m", "pip", "install", "--upgrade", "pip"])
    except subprocess.CalledProcessError:
        print("⚠️ pip güncellenemedi, devam ediliyor...")

    subprocess.check_call([python_executable, "-m", "pip", "install"] + REQUIREMENTS)
    print("✅ Kütüphaneler yüklendi.")

def run_app():
    print("🚀 Uygulama başlatılıyor...")
    python_executable = os.path.join(VENV_DIR, "Scripts", "python") if os.name == "nt" else os.path.join(VENV_DIR, "bin", "python")
    subprocess.call([python_executable, APP_FILENAME])

if __name__ == "__main__":
    if os.name == "nt":
        enable_powershell_execution_policy()
    create_virtual_env()
    install_requirements()
    run_app()
