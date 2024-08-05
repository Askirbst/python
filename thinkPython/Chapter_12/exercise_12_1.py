def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if inverse.setdefault(val, [key]) != [key]:
            inverse[val].append(key)
    return inverse

def most_frequent(s):
    d = {}
    s = s.lower()
    non_alpha = (' ', "'", '.', ',', '-', "’")

    for char in s:
        if char not in non_alpha:
            d[char] = d.get(char, 0) + 1

    d = invert_dict(d)
    t = d.items()
    t = reversed(sorted(t))
    letter_by_frequency = tuple()
    for item in t:
        number, elements = item
        for element in elements:
            letter_by_frequency = letter_by_frequency[:] + (element,)
    print(letter_by_frequency)

english = "As I was driving home from work stuck in the usual rush hour traffic on the highway\
I couldn't help but think about all the things I still needed to do when I got home\
like preparing dinner helping the kids with their homework taking the dog for a walk\
and then finally if I had any energy left catching up on that new show everyone's\
been talking about but before I could even get started on any of that I realized I\
needed to stop by the grocery store to pick up some milk and bread"

mandarin = "Zài yī gè yáng guāng míng mèi de zhōu mò zǎo chén\
wǒ hé wǒ de péng yǒu men yī qǐ qù gōng yuán sàn bù wǒ men yán\
zhe hú biān de xiǎo jìng màn màn zǒu xīn shǎng zhe zhōu wéi de\
měi lì jǐng sè, tán lùn zhe gè zì de shēng huó hé gōng zuò wǒ\
men hái tíng xià lái pāi le hěn duō zhào piàn jì lù xià zhè měi\
hǎo de shí guāng rán hòu wǒ men zài gōng yuán de cháng yǐ shàng \
zuò xià fēn xiǎng dài lái de xiǎo chī hé yǐn liào xiǎng shòu\
zhe wēi fēng fú miàn de gǎn jué zhè yàng de shí guāng ràng wǒ\
men gǎn dào wú bǐ fàng sōng hé yú kuài ràng wǒ men zàn shí wàng\
jì le gōng zuò hé shēng huó zhōng de fán nǎo chōng mǎn le néng\
liàng hé dòng lì qù yíng jiē xīn de tiǎo zhàn hé jī yù"

japan = "Nichi-yōbi no asahi ga mabushī asa tomodachi to issho ni kōen o sanpo\
shita toki watashitachi wa mizuumi no kishi ni sotta komichi o yukkuri aruki\
nagara shūi no utsukushī keshiki o kanshō shi otagai no seikatsu ya shigoto ni\
tsuite hanashi mashita. Watashitachi wa takusan no shashin o toru tame ni tachi yori\
kono subarashī jikan o kiroku shimashita Soshite kōen no benchi ni suwari motte\
kita okashi ya nomimono o wakachiaishi kaze ga hoho o naderu kanji o tanoshimi\
kono yō na jikan wa watashitachi o hijō ni rirakkusu saseru yō ni kanjisa se shigoto\
ya seikatsu no nayami o shibaraku wasure saseru koto ga deki aratana chōsen ya kibonō\
o mukaeru tame no enerugī to yaruki ni afure sasemashita."

spanish = "En una soleada mañana de fin de semana, mis amigos y\
yo fuimos al parque a caminar, recorriendo lentamente el sendero\
junto al lago, admirando el hermoso paisaje a nuestro alrededor y\
hablando sobre nuestras vidas y trabajos. Nos detuvimos para tomar\
muchas fotos y capturar esos momentos maravillosos. Luego, nos\
sentamos en una banca del parque, compartimos los bocadillos y\
bebidas que habíamos traído, y disfrutamos de la sensación del \
viento suave en nuestras caras. Ese tiempo nos hizo sentir\
increíblemente relajados y felices, permitiéndonos olvidar \
temporalmente las preocupaciones del trabajo y la vida, y \
llenándonos de energía y motivación para enfrentar nuevos desafíos y oportunidades."

arabic = "Fī ṣabāḥ nhār al-jumʿah al-shamsī, anā wa asdiqā’ī \
dhahabnā ilā al-ḥadīqah li-namtashi, mumtadīn bi-buṭ’ alā al-mamar\
al-mujāwir lil-buḥayrah, mustamtiʿīn bil-manāẓir al-jamīlah ḥawlanā \
wa nataḥadathu ʿan ḥayātinā wa aʿmālinā. Wa waqafnā li-akhdh kathīr \
min al-ṣuwar li-tuwathiq hādhihi al-lāḥẓāt al-jamīlah. Baʿd dhālik, \
jalasnī ʿalā maqāʿid al-ḥadīqah, wa taqāsimnā al-ṭaʿām wa al-mashrūbāt \
allatī ahdarnāhā, mustamtiʿīn biniṣīm al-rīḥ al-latī lamsat wujūhanā. \
Hādhā al-waqt jaʿalanā nasʿur bi-irtikhā’ wa saʿādah la tutṣaddaq, \
muʿṭīnānā qudrah ʿalā nisīān humūm al-ʿamal wa al-ḥayāh, wa mali’ānā \
bi-ṭāqah wa ḥāfiẓ li-muwājahat al-taḥaddiyāt al-jadīdah wa al-furṣ al-qādimah"

most_frequent(english)
most_frequent(mandarin)
most_frequent(japan)
most_frequent(spanish)
most_frequent(arabic)