#!/usr/bin/env python3
"""
Lecture du capteur de température et d'humidité DHT22.
"""

import time
import board
import adafruit_dht

# Configuration
DHT_PIN = board.D4  # GPIO 4 (pin physique 7)
dht = adafruit_dht.DHT22(DHT_PIN)

def lire_temperature():
    """
    Lit la température en degrés Celsius.
    Returns: float ou None
    """
    try:
        return dht.temperature
    except RuntimeError as e:
        print(f"Erreur de lecture température: {e}")
        return None

def lire_humidite():
    """
    Lit l'humidité relative en pourcentage.
    Returns: float ou None
    """
    try:
        return dht.humidity
    except RuntimeError as e:
        print(f"Erreur de lecture humidité: {e}")
        return None

def afficher_mesures():
    """Affiche les mesures de température et d'humidité."""
    print("Capteur DHT22 - Température et Humidité")
    print("Appuyez sur Ctrl+C pour quitter")
    print("-" * 40)

    while True:
        try:
            temperature = lire_temperature()
            humidite = lire_humidite()

            if temperature is not None and humidite is not None:
                print(f"Température: {temperature:.1f} °C")
                print(f"Humidité: {humidite:.1f} %RH")
                print("-" * 40)
            else:
                print("Échec de la lecture. Réessai...")
                print("-" * 40)

            time.sleep(2)  # minimum 2 secondes entre lectures

        except KeyboardInterrupt:
            print("\nAu revoir!")
            break

        except Exception as e:
            print(f"Erreur: {e}")
            print("Vérifiez que:")
            print("  - Le capteur est correctement câblé")
            print("  - DATA est sur GPIO 4 (pin physique 7)")
            print("  - Une résistance 10K relie DATA à VCC")
            break

def main():
    afficher_mesures()

if __name__ == "__main__":
    main()
