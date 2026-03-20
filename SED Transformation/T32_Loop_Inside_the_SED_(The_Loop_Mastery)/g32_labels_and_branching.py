def generate_g32_data():
    # İç içe geçmiş, karmaşık kirli veriler
    data = [
        "  ... ,,, --- DATA_ALPHA --- ...  ",
        "---...---DATA_BETA---...---",
        " , , , DATA_GAMMA . . . ",
        " . - . - . ", # Tamamen çöp, veri yok
        "      ",       # Sadece boşluk
        ",,,CLEAN_ME,,,",
        "  ... ,,, --- DATA_ALPHA --- ...  ",
        "---...---DATA_BETA---...---",
        " , , , DATA_GAMMA . . . ",
        " . - . - . ", # Tamamen çöp, veri yok
        "      ",       # Sadece boşluk
        ",,,CLEAN_ME,,,",
        "  ... ,,, --- DATA_ALPHA --- ...  ",
        "---...---DATA_BETA---...---",
        " , , , DATA_GAMMA . . . ",
        " . - . - . ", # Tamamen çöp, veri yok
        "      ",       # Sadece boşluk
        ",,,CLEAN_ME,,,",
        "  ... ,,, --- DATA_ALPHA --- ...  ",
        "---...---DATA_BETA---...---",
        " , , , DATA_GAMMA . . . ",
        " . - . - . ", # Tamamen çöp, veri yok
        "      ",       # Sadece boşluk
        ",,,CLEAN_ME,,,"
    ]
    with open("g32_dirty_data.csv", "w") as f:
        for line in data:
            f.write(line + "\n")

if __name__ == "__main__":
    generate_g32_data()
    print(">>> 'g32_dirty_data.csv' (İnatçı kirler) üretildi.")
