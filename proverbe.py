import random

quotes = [
    "Le succès n’est pas final, l’échec n’est pas fatal : c’est le courage de continuer qui compte.",
    "N’abandonne jamais, les grandes choses prennent du temps.",
    "Travaille en silence, laisse ton succès faire du bruit.",
    "Chaque jour est une nouvelle opportunité.",
    "La discipline dépasse la motivation."
]

def get_random_quote():
    return random.choice(quotes)

def main():
    print("✨ Citation du jour :\n")
    print(get_random_quote())

if __name__ == "__main__":
    main()
