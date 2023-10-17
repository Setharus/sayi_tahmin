import random

def tahmin_et():
    rastgele_sayi = random.randint(1, 100)
    tahmin_hakki = 5

    print("1 ile 100 arasinda bir sayiyi tahmin et.")
    print(f"Tahmin hakkin: {tahmin_hakki}")

    while tahmin_hakki > 0:
        tahmin = int(input("Tahminin: "))

        if tahmin < rastgele_sayi:
            print("Daha büyük bir sayi dene.")
        elif tahmin > rastgele_sayi:
            print("Daha küçük bir sayi dene.")
        else:
            print(f"Tebrikler! {rastgele_sayi} sayisini doğru tahmin ettin.")
            return

        tahmin_hakki -= 1
        print(f"Tahmin hakkin: {tahmin_hakki}")

    print(f"Uzgunum, tahmin hakkin bitti. Doğru sayi {rastgele_sayi} idi.")

if __name__ == "__main__":
    tahmin_et()