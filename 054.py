""" The wavelength of visible light ranges from 380 to 750 nanometers (nm). While the
spectrum is continuous, it is often divided into 6 colors as shown below: Write a program that
reads a wavelength from the user and reports its color. Display an appropriate error message
if the wavelength entered by the user is outside of the visible spectrum."""
lunghezza_onda = int(input("Inserisci Lunghezza d'Onda: "))
if lunghezza_onda >= 380 and lunghezza_onda < 450:
    print("Colore: Viola")
elif lunghezza_onda >= 450 and lunghezza_onda < 495:
    print("Colore: Blu")
elif lunghezza_onda >= 495 and lunghezza_onda < 570:
    print("Colore: Verde")
elif lunghezza_onda >= 570 and lunghezza_onda < 590:
    print("Colore: Giallo")
elif lunghezza_onda >= 590 and lunghezza_onda < 620:
    print("Colore: Arancione")
elif lunghezza_onda >= 620 and lunghezza_onda <= 750:
    print("Colore: Rosso")
else:
    print("Colore non trovato.")
