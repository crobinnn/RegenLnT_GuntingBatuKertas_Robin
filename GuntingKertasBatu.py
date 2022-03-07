import random

while True:
    suit = input("Pilih (gunting, kertas, batu): ")
    pilihan_suit = ["gunting", "kertas", "batu"]
    suit_bot = random.choice(pilihan_suit)

    print(f"\nLu pilih {suit}, bot pilih {suit_bot}\n")

    if suit == suit_bot:
        print(f"Yah kok bisa sama2 {suit}, gada yang menang\n")
    elif suit == "gunting":
        if suit_bot == "kertas":
            print("Wihh menang lawan bot kerenn\n")
        else:
            print("Cupu lu, bisa kalah lawan bot doang\n")
    elif suit == "batu":
        if suit_bot == "gunting":
            print("Wihh menang lawan bot kerenn\n")
        else:
            print("Cupu lu, kalah sama kertas\n")
    elif suit == "kertas":
        if suit_bot == "batu":
            print("Wihh menang lawan bot kerenn\n")
        else:
            print("Cupu lu kalah sama bot, kena gunting\n")

    main_lagi = input("Mau main lagi? (ya/ga): ")
    if main_lagi == "ya":
        print("\nYey main suit lagi!")
    else:
        break
