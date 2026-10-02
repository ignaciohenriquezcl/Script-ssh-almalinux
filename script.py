import os
import subprocess
import sys

def ejecutar(comando):
    print(f"\nEjecutando: {comando}")
    resultado = subprocess.run(comando, shell=True)

    if resultado.returncode != 0:
        print(f"Error al ejecutar: {comando}")
        sys.exit(1)

def main():
    print("=========================================")
    print("     INSTALACIÓN SSH - ALMA LINUX")
    print("=========================================")

    if os.getuid() !=0:
        print("Debes ejecutar este script como root.")
        print(" Usa: Sudo python3 __main__.py")
        sys.exit(1)

    print("Actualizando repositorios...")
    ejecutar("dnf update -y")

    print("Instalando OpenSSH Server...")
    ejecutar("dnf install openssh-server -y")

    print("Iniciando servicios SSH...")
    ejecutar("systemctl start sshd")

    print("Configurando inicio automático...")
    ejecutar("systemctl enable sshd")

    print("Configurando Firewall...")
    ejecutar("firewall-cmd --permanent --add-service=ssh")
    ejecutar("firewall-cmd --reload")

    print("Comprobando servicio SSH...")
    ejecutar("systemctl --no-pager status sshd")

    print("=============================================")
    print("      SSH INSTALADO CORRECTAMENTE")
    print("=============================================")
