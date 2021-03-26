from hero_factory import HeroFactory
if __name__=="__main__":
    hero_factory = HeroFactory()
    timo = hero_factory.create_hero("timo")
    police = hero_factory.create_hero("police")
    police.fight(timo)
    timo.speak_lines()
    police.speak_lines()