import random

def load_words(filename="words.txt"):
    with open(filename, "r") as f:
        return [w.strip().lower() for w in f if len(w.strip()) == 5]

def pilih_kata(words):
    return random.choice(words)

def cek_jawaban(secret, guess):
    result = []
    for i in range(5):
        if guess[i] == secret[i]:
            result.append("🟩")
        elif guess[i] in secret:
            result.append("🟨")
        else:
            result.append("⬛")
    return "".join(result)

def main():
    words = load_words()
    secret = pilih_kata(words)
    attempts = 6

    print("=== WORDLE MINI (KAMUS MODE) ===")
    print("Tebak kata 5 huruf. Kamu punya 6 kesempatan.")

    while attempts > 0:
        guess = input(f"\nTebakan ({attempts} sisa): ").lower()

        if len(guess) != 5:
            print("⚠️ Harus 5 huruf!")
            continue
        if guess not in words:
            print("⚠️ Kata tidak ada di kamus!")
            continue

        print(cek_jawaban(secret, guess))

        if guess == secret:
            print("🎉 Kamu MENANG!")
            return

        attempts -= 1

    print(f"\n❌ Kamu KALAH. Jawabannya: {secret}")

if __name__ == "__main__":
    main()
