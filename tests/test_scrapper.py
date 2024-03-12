import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from video import video

test_url = 'https://www.youtube.com/watch?v=dF6CRulW4G0'
test_video = video.Video(test_url)

def test_data():
    assert type(test_video.data) == dict

def test_title():
    assert test_video.title == 'McDrive to Survive : GP Explorer 2022'

def test_channel():
    assert test_video.channel == 'Vilebrequin'
    
def test_wrong_channel():
    assert test_video.channel != 'Vilebrequin2'

def test_likes():
    assert test_video.likes >= 186926
    
def test_positive_number_likes():
    assert test_video.likes > 0

def test_description():
    assert test_video.description == "Un énorme merci à NordVPN, pour leur soutien sans faille même sur des contenus très créatifs.\nEn ce moment 4 mois gratuits en passant par ce lien 👉 https://nordvpn.com/vilebrequin\n( Satisfait ou remboursé pendant 30 jours )\n\nUn grand merci à tous les invités qui ont joué le jeu : Julien Fébreau, @SQUEEZIE , @SEB  @Kaatsup @Depielo @Manon Lanza @Amixem @Djilsi @Domingo @Deujna @LeBouseuh  @JOYCA @Sofyan \n\nÉquipes techniques :\nProduction : Anaelle Le Magorou ;\nJournalistes : Lauriane Dherbecourt, Julia Durrande, Elvire Le Doré, Masquelier Hélène, Nadia Saghro ; \nCadre : Lucas Martin, Hugo Leclerc, Axel Roguet, Léandre Beauregard, Kévin Guiboux ; \nSon : Alan Poirier, Lenny Louisy- Daniel, Anna, Matthieu, Hugo Boust ; \nRégie : Baptiste Seysen ; Eliott Fettweis ;\nDrone : Adrien Loison\n\n-------------------------------------------------------------------\n👍 POUCE BLEU, ABONNE TOI ET METS LA CLOCHE 🛎️\n\nPour nous suivre sur les réseaux :\n\n📲 INSTAGRAM    https://www.instagram.com/vbrequin/\n📲 TWITTER         https://twitter.com/VilebrequinAuto\n\n⚠️⚠️ Nos stickers, porte-clés et t-shirts ⚠️⚠️\nhttps://www.shop.benzin.fr/vilebrequin\n\n-------------------------------------------------------------------\n\nMontage : Lukasz Sledziewski ( qui n'est pas boulard man )\nTwitter : https://twitter.com/LukyKRN\n\n-------------------------------------------------------------------\n\nMerci de nous contacter par mail UNIQUEMENT pour des raisons professionnelles (propositions de voiture que vous possédez ou partenariats commerciaux uniquement), les autres sujets ne seront pas répondus (on a les réseaux pour ça)\n\n📩 MAIL :  vbrequin@gmail.com\n\nPour les propositions de voitures à essayer, merci de joindre une photo et une localisation, bisous\n\n--------------------------------------------------------------------\n\nMerci à tous les contributeurs depuis le début de la chaîne, vous êtes des dinguos.\n\nGros bisous\n\nP.S.: Cette vidéo n'est pas sponsorisée par McDonalds. Mais on remercie quand même le restaurant du Mans pour leur aide ( on a vraiment mis une F4 dans un McDrive )\n\n#gpexplorer #F4 #lacoupealamaison"
    
def test_description_url():
    assert test_video.description_urls == [
            "https://nordvpn.com/vilebrequin",
            "https://www.instagram.com/vbrequin/",
            "https://twitter.com/VilebrequinAuto",
            "https://www.shop.benzin.fr/vilebrequin",
            "https://twitter.com/LukyKRN"
            ]
    
def test_id():
    assert test_video.id == 'dF6CRulW4G0'
    