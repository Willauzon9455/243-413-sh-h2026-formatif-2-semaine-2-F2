#!/usr/bin/env python3
"""
Effet chenillard sur 3 LEDs via GPIO.
"""

import time
import RPi.GPIO as GPIO

# Configuration des broches GPIO
LED_ROUGE = 14
LED_VERTE = 15
LED_JAUNE = 18

LEDS = [LED_ROUGE, LED_VERTE, LED_JAUNE]

def chenillard(delai=0.3):
    """
    Effet chenillard : les LEDs s'allument successivement
    et s'éteignent avant la suivante.
    """
    for led in LEDS:
        GPIO.output(led, GPIO.HIGH)
        time.sleep(delai)
        GPIO.output(led, GPIO.LOW)

def chenillard_allume(delai=0.3):
    """
    Effet chenillard où les LEDs restent allumées
    puis s'éteignent toutes ensemble.
    """
    for led in LEDS:
        GPIO.output(led, GPIO.HIGH)
        time.sleep(delai)

    time.sleep(delai)

    for led in LEDS:
        GPIO.output(led, GPIO.LOW)

def main():
    """Fonction principale."""
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LEDS, GPIO.OUT)

    # Éteindre toutes les LEDs au départ
    for led in LEDS:
        GPIO.output(led, GPIO.LOW)

    print("Effet chenillard sur 3 LEDs")
    print("Appuyez sur Ctrl+C pour quitter")

    try:
        while True:
            chenillard(0.3)           # Effet normal
            # chenillard_allume(0.3)  # Décommente si tu veux tester l'autre

    except KeyboardInterrupt:
        print("\nAu revoir!")
    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    main()
