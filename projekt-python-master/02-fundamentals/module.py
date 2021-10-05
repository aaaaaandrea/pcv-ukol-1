EARTH_GRAVITY = 9.807  # ? normální pozemské tíhové zrychlení
MOON_GRAVITY = 1.62  # ? měsíční gravitace
SPEED_OF_LIGHT = 299792458  # ? rychlost světla ve vakuu
SPEED_OF_SOUND = 343  # ? rychlost zvuku při teplotě 20 °C v suchém vzduchu


def vypocet_rychlosti(vzdalenostVypocet):
    """
    Vypocet rychlosti svetla a zvuku pro zadanou vzdalenost
    """
    print('Rychlost svetla na ' + str(vzdalenostVypocet) + 'm je: ' + str(int(vzdalenostVypocet) * SPEED_OF_LIGHT))
    print('Rychlost Zvuku na ' + str(vzdalenostVypocet) + 'm je: ' + str(int(vzdalenostVypocet) * SPEED_OF_SOUND))


def vaha_na_mesici(vaha):
    """
    Vypocet hmotnosti ojektu na mesici
    """
    print('Objekt bz na mesici vazil:' + str(int(vaha) / EARTH_GRAVITY * MOON_GRAVITY) + 'kg')
