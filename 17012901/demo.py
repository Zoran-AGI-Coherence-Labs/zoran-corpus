import random
import math

def simulate_signal(n=100):
    """Simule n mesures radio, avec quelques 'signaux impossibles'."""
    data = []
    for i in range(n):
        energy = abs(random.gauss(1e18, 1e17))  # énergie en eV
        direction = random.uniform(-1, 1)       # -1 = remonte de la Terre
        if direction < -0.8 and energy > 5e18:
            anomaly = True  # signal impossible façon ANITA
        else:
            anomaly = False
        data.append({"energy": energy, "direction": direction, "anomaly": anomaly})
    return data

if __name__ == "__main__":
    signals = simulate_signal(50)
    anomalies = [s for s in signals if s["anomaly"]]
    print(f"Signaux simulés : {len(signals)}")
    print(f"Anomalies détectées : {len(anomalies)}")
    for a in anomalies:
        print(f"⚠️ Anomalie : énergie={a['energy']:.2e} eV, direction={a['direction']:.2f}")
