import os
import subprocess
import sys
import venv

VENV_DIR = "env"
REQUIREMENTS = [
    "opencv-python",
    "numpy",
    "pandas",
    "scikit-learn",
    "deepface",
    "tk"  # çoğu zaman sistemde yüklüdür ama garanti olsun diye ekledik
]

APP_FILENAME = "face_app.py"  # Ana uygulamanın dosya adı

def create_virtual_env():
    if not os.path.exists(VENV_DIR):
        print("🔧 Sanal ortam oluşturuluyor...")
        venv.create(VENV_DIR, with_pip=True)
        print("✅ Sanal ortam oluşturuldu.")
    else:
        print("ℹ️ Sanal ortam zaten var, atlanıyor.")

def install_requirements():
    print("📦 Gerekli kütüphaneler yükleniyor...")
    pip_executable = os.path.join(VENV_DIR, "Scripts", "pip") if os.name == "nt" else os.path.join(VENV_DIR, "bin", "pip")
    subprocess.check_call([pip_executable, "install", "--upgrade", "pip"])
    subprocess.check_call([pip_executable, "install"] + REQUIREMENTS)
    print("✅ Kütüphaneler yüklendi.")

def run_app():
    print("🚀 Uygulama başlatılıyor...")
    python_executable = os.path.join(VENV_DIR, "Scripts", "python") if os.name == "nt" else os.path.join(VENV_DIR, "bin", "python")
    subprocess.call([python_executable, APP_FILENAME])

if __name__ == "__main__":
    create_virtual_env()
    install_requirements()
    run_app()
