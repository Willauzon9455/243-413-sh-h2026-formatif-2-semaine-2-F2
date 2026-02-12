#!/usr/bin/env python3
"""
Contrôle simple de 3 LEDs via GPIO.

- LED rouge sur GPIO 17
- LED verte sur GPIO 27
- LED jaune sur GPIO 22

Câblage :
- LED rouge : GPIO 17 → résistance 330Ω → GND
- LED verte : GPIO 27 → résistance 330Ω → GND
- LED jaune : GPIO 22 → résistance 330Ω → GND
"""

import time
import RPi.GPIO as GPIO

# Configuration des broches GPIO
LED_ROUGE = 14
LED_VERTE = 15
LED_JAUNE = 18

# Configurer le mode BCM
GPIO.setmode(GPIO.BCM)

# Configurer les broches en sortie
GPIO.setup(LED_ROUGE, GPIO.OUT)
GPIO.setup(LED_VERTE, GPIO.OUT)
GPIO.setup(LED_JAUNE, GPIO.OUT)

def allumer_toutes():
    """Allume toutes les LEDs."""
    GPIO.output(LED_ROUGE, GPIO.HIGH)
    GPIO.output(LED_VERTE, GPIO.HIGH)
    GPIO.output(LED_JAUNE, GPIO.HIGH)

def eteindre_toutes():
    """Éteint toutes les LEDs."""
    GPIO.output(LED_ROUGE, GPIO.LOW)
    GPIO.output(LED_VERTE, GPIO.LOW)
    GPIO.output(LED_JAUNE, GPIO.LOW)

def main():
    """Fonction principale."""
    print("Contrôle de 3 LEDs")
    print("Rouge = GPIO 17, Verte = GPIO 27, Jaune = GPIO 22")
    print("Appuyez sur Ctrl+C pour quitter")

    try:
        while True:
            # Allumer rouge
            eteindre_toutes()
            GPIO.output(LED_ROUGE, GPIO.HIGH)
            time.sleep(1)

            # Allumer verte
            eteindre_toutes()
            GPIO.output(LED_VERTE, GPIO.HIGH)
            time.sleep(1)

            # Allumer jaune
            eteindre_toutes()
            GPIO.output(LED_JAUNE, GPIO.HIGH)
            time.sleep(1)

    except KeyboardInterrupt:
        print("\nAu revoir!")
    finally:
        eteindre_toutes()
        GPIO.cleanup()

if __name__ == "__main__":
    main()
