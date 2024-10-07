import subprocess
import os
import re

def download_track_by_link(track_url):
    try:
        # Fetch the track ID or title from the URL
        track_id = track_url.rstrip('/').split('/')[-1]
        print(f"Track ID extracted: {track_id}")

        # Create a directory for the track if it doesn't exist
        if not os.path.exists("links"):
            print("Creating 'links' directory")
            os.makedirs("links")
        else:
            print("'links' directory already exists")

        # Build the scdl command to download the track
        command = [
            "scdl",
            "-l", track_url,
            "--path", "links",  # saving directory
        ]

        print(f"Constructed scdl command: {' '.join(command)}")

        # Run the scdl command
        print("Running scdl command...")
        result = subprocess.run(command, capture_output=True, text=True)
        print("scdl command finished running")

        # Check if the command was successful
        if result.returncode == 0:
            print(f"Successfully downloaded track from {track_url}")
        else:
            print(f"Failed to download track. Error: {result.stderr}")

    except Exception as e:
        print(f"An error occurred: {e}")

def parse_and_download_tracks(message):
    # Regular expression to find SoundCloud URLs in the message
    url_pattern = re.compile(r'https://soundcloud\.com/\S+')
    urls = url_pattern.findall(message)
    print(f"Found URLs: {urls}")

    # Download each track by URL
    for url in urls:
        download_track_by_link(url)


if __name__ == "__main__":
    message = '''
    jafart, [06.07.2024 2:20]
https://soundcloud.com/sonnydigital/ilove-makonnen-ft-wiz-khalifa-and-gucci-mane-i-dont-sell-molly-no-more-prod-by-sonny-digital?si=6563bf5e396949c3ae2735ad567fce8f&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 2:21]
https://soundcloud.com/thefuturebeatsshow/whispa-i-used-to-smoke?si=9480932f85d3405d99f9195b119d8b45&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 2:22]
https://soundcloud.com/misogi/clairvoyant?si=c2828b097c7b4b8489307746053af324&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 2:24]
https://soundcloud.com/magikmoar/moar-sarsha-simone-gonna-do-me-20syl-remix?si=78667fd181cf46e1928fa010fddaa811&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 2:24]
https://soundcloud.com/complexion/complexion-mix-for-first-ear?si=749a3978ead14a7cb97b41a15073842a&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 2:24]
https://soundcloud.com/yungwallstreet/young-dro-fdb-yung-wall-street-flip?si=1b64c8bdd03048258b4470ad693741b4&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 2:25]
https://soundcloud.com/danielfernandesofficial/daniel-fernandes-on-everyday-out-now?si=be8446d46ff94889ad00a56f959f7c8f&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 2:26]
https://soundcloud.com/eastghost/dvocean?si=2ed2d3a00d644f17ac47c58deeec6b6f&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 2:27]
https://soundcloud.com/ramriddlz/call-me-ft-nemesis-prod-chilla-jaegen?si=579152b974474df48c657360f2ba740d&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 2:27]
https://soundcloud.com/jeremiah-jackson-24/juicy-j-for-everybody-featwiz-khalifa-r-city-remix?si=b8943912916e4ba59dcc153ad5be61c4&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 2:28]
https://soundcloud.com/thajournalist/eat?si=988f490846434777827e36a9449e58d0&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 2:28]
https://soundcloud.com/mastercpromo/troyboi-og-jerseyclubremix-by-thatdude809-master_c97?si=49620e1625244024a44f8951f85307d8&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 2:29]
https://soundcloud.com/hydrate/uz-x-r-kelly-im-a-flirt-trap?si=7e0a521eef924c5cb1ff54f242dbea48&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 2:30]
https://soundcloud.com/sorrowgarage/grimes-skin-sorrow-remix?si=6ea239cecb29422e96dd05788acc9340&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 2:30]
https://soundcloud.com/truluxlynx/so-sick?si=e0f4488dff5d4e288014ba0e4c7f52f3&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 2:30]
https://soundcloud.com/platform/weddit-shlomo-d33j-nickmelons?si=742608edf97e48119c3b529a4591588d&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 2:32]
https://soundcloud.com/robyn/robyn-la-bagatelle-magique-feat-maluca-love-is-free-on-annie-mac-bbc-radio-1?si=0c2366e2983d4566b7e94c7f1c8a8965&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 2:32]
https://soundcloud.com/lilwestbb/blizteal-pressure-prod-nodachi?si=8030627c20bb4b58971cb4db7c5b79f0&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 2:32]
https://soundcloud.com/dj-t-marq-201/dj-t-marq?si=71a3aa4df2364f0786bda3df9894d9af&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 2:34]
https://soundcloud.com/kevinwallace12/clouds-above?si=6f2fe83e5ee0459ba53de3f88e008889&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 2:35]
https://soundcloud.com/black-c-o-a-l/black-coal-cellular-prod-morenight?si=ffc4ef52ac33487e85d504948c9996e0&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 2:38]
https://soundcloud.com/hamzasaucegod/anh-yeah-prod-hamza?si=23a19a9f89384af595df33df0a843829&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 2:38]
https://soundcloud.com/shlohmo/baby-bash-suga-suga-shlohmo-remix?si=255c1b9ad6bb404f90c3aea21548c520&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 2:39]
https://soundcloud.com/fafane-sparta/ghetto-thug-vi-dj-siiree-smocked-feat-dj-boss-bando-chientus-and-sparta-gang-enfwa-2k17?si=0db77c194a404fde92b7126550a09007&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 2:41]
https://soundcloud.com/21savage/x-feat-future?si=5582c0e1058e416fbf99e22be8589f03&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 2:41]
https://soundcloud.com/djzebo/me-and-u-zebos-clark-belmont?si=e22f8fc775be49978f57b3f7ebeb2cac&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 2:42]
https://soundcloud.com/koni_music/drake-one-dance-koni-remix-ft-casey-malone-1?si=85a6f312112c43d8a1bae7e28aba1b67&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 2:42]
https://soundcloud.com/user-655476614/mr-eazi-ft-tekno-short-skirt?si=73d82c0231ab40ff9e78b5ddef22ac1c&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 2:42]
https://soundcloud.com/user-947872832/les-malhonnetes-qlm-choun-choun-remix-by-dj-skunk?si=29fa39f7283d462e9894f6996af8c267&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 2:42]
https://soundcloud.com/djflex973-417441283/catch-me-outside-afrobeat?si=31bfe64441784df3b049f84eec582602&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 2:45]
https://soundcloud.com/smilehighclubcommunity/rzl-insincerity?si=1ad0518fc1b9417887d06b0c21dfca1e&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 2:46]
https://soundcloud.com/weaverbeats/player?si=e2cc5befe2c04dddae0dbf2bb91538f2&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 2:47]
https://soundcloud.com/iamrealblondie/love-for-you?si=51f231fe052443a4981f4bc7e44bd433&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 2:47]
https://soundcloud.com/jimmyprime/cant-stop-myself?si=7b9b29965d0a4f1eb93d251fabb85f69&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 2:47]
https://soundcloud.com/blamelobotome/the-ting-gok-itaewon?si=7873694ce9c3433493323c812e74d4a1&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 2:47]
https://soundcloud.com/atl_aztecs/02-dark-faders-prod?si=efdfdee722fe498aae8ab764a9b19a04&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 2:48]
https://soundcloud.com/youngthugworld/relationship-feat-future-1?si=d920b59ae0d9480aa2efcced2b203207&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 2:48]
https://soundcloud.com/okosa/dj-taj-disclosure-latch-jersey?si=92bdbbcf4e914fe4be67cf2ecdc48b7e&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 2:48]
https://soundcloud.com/throwbackjerseyclub/dj-tricks-impossible-ft-dj-get?si=87555a7ab9d842a7a5f2918626f40c3b&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 2:49]
https://soundcloud.com/brenno_meendes/mc-kevinho-tumbalatum-kondzilla?si=c2acc39ff3a34ea0a68116c6a8c188cc&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 2:49]
https://soundcloud.com/famous_dex1/japan?si=efb347d495614f40a730a3625e6a85d0&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 2:49]
https://soundcloud.com/rnbass/aisa-get-right-ft-makio-prod-las-venus?si=2baa0891044f4d57b098de45ca5fba57&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 2:49]
https://soundcloud.com/044klannn/044-rose-hoodrich-ua-rip-peep-rip-fredo-rip-xxxtentacion-rip-yams?si=28b7e57c583847e5a9f221b253818224&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 2:50]
https://soundcloud.com/ziggyfocused/ziggy-look-back-at-it-jersey-mix?si=27911c3ccb364366a38b83366ce8ca25&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 2:50]
https://soundcloud.com/liluzivert/erase-your-social-produced-by-don-cannon-lyle-leduff?si=5aaeaebe8ab3434084de77e89e75c0b5&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 2:51]
https://soundcloud.com/avix60/close?si=a8af0d289a30434cb31fa3e1edef1f4f&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 2:52]
https://soundcloud.com/deejayy-smallz/butterflies-jersey-club-mix?si=04f7ac23af724b1b9e34c3a8b723a39c&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 2:52]
https://soundcloud.com/bringtherukus/lil-dicky-ft-rich-homie-quan-fetty-wap-save-dat-money-dj-rukus-rnbass-remix?si=ef06dd761ac946538314730dc50fa08d&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 2:53]
https://soundcloud.com/rnbass/rayven-justice-hit-or-nah-dirty-prod-jmg?si=53fe7ce7a7324ae5b004045794d82b96&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 2:53]
https://soundcloud.com/prodbybrandong/danileigh-lil-bebe-jersey-club-remix-dj-fearess-remix?si=45345b7c7b7d482cace910192f4a8e30&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 2:53]
https://soundcloud.com/officialmanucrooks/throw-it-back-feat-b-wise?si=74c422bb7fc1491ea24de193a42807f5&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 2:53]
https://soundcloud.com/fatnick/ps-fuck-you-cunt-ft-lil-peep-prodmikey-the-magician?si=86125bd2da8f47a3a32e51e50ad96372&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 2:54]
https://soundcloud.com/proderis/coola?si=da0e3610c5eb48878431c58ebf1fb0fb&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 2:54]
https://soundcloud.com/acemula908/fiyah-acemula-ft-shotta-spence?si=c59c71f69900402494348cd4e262ab2a&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 2:55]
https://soundcloud.com/latin-club/sets/latin-club-3-take-over-hosted-by-official-karen?si=ddce837617de4d6cad3779a08e80d9a5&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 2:55]
https://soundcloud.com/latin-club/2-ayer-anuel-cueheat-x-merks?si=c96dba190c604e2ab2bd6198196815d2&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 2:55]
https://soundcloud.com/user-880532784/ty-ne-ver-slezam-ss18?si=c1e09869a2c340b0958824e75beb2253&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 2:56]
https://soundcloud.com/djirresistible/taste-x-zeze-dj-irresistible-mix?si=5d00565dc2a542979c1892566b4f6d13&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 2:56]
https://soundcloud.com/djtwinz/dj-twinz-ft-dj-lokey-dame-tu-cosita?si=e3ea81c16da14d7dbb6cd7fab4e283d2&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 2:57]
https://soundcloud.com/producerkeyflo/u-majid-jordanjerseyclubremix-k3yflo?si=aedfe7593e7944119f90b8653b24cc3c&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 2:57]
https://soundcloud.com/maxgaspard/koffee-toast-jersey-club-remix-prod-max-blu?si=214ee07b035f40c3a91847fee8b0f00b&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 2:57]
https://soundcloud.com/eliteteamdjs/ill-b-right-there-4-u-cueheat-x-djmerks973?si=1cfc13545b8f497e837cb34aadcd359a&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 2:58]
https://soundcloud.com/therealdjhook1/thotiana-hook-remix-ft-cardi-b?si=1cb8d76565024096ac970f5eee7ff5c0&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 2:59]
https://soundcloud.com/kingtimmy136/vamos-a-repetir-prod-cito-on-the-beat?si=a00fef30ce984356ae16afcc05de1a11&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 2:59]
https://soundcloud.com/sjayyofficial/afro-b-drogba-joanna-sjayy-jersey-club-mix-1?si=0337dcfc8c434438b3094d443089a4ff&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:00]
https://soundcloud.com/thunderstone-labs/wlf3?si=27f23628a17c4ec7a896142e19fff6f6&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:00]
https://soundcloud.com/user-12462261/jeremih-dont-tell-em-official-video-ft-yg?si=ecee6958db5443d1ba5e2c8ab0d38cae&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:00]
https://soundcloud.com/bipdrip/thomas-mraz-pol-eto-lava?si=3bfa9d1e645b4a59a3c366305e4447c4&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:01]
https://soundcloud.com/lilkrystalll/orbit-feat-og-buda-offmi?si=331c6a0428da49ff856eb8386efb7cc8&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:01]
https://soundcloud.com/djjayfrescosf/bad-bunny-callaita-jay-fresco-edit?si=eaf7a874bb9b4dc2845a88a5fe61745c&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:02]
https://soundcloud.com/lava_dome/bad-gyal-mercadona-lava-rebounce?si=305f85a91b51465fb0d0cb1c8e26992d&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:03]
https://soundcloud.com/fernandorufino/bad-gyal-mercadona?si=ae902a9151e24ded8dfe42af10f054ef&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:07]
https://soundcloud.com/dazvaaa/backr00ms?si=6b2d6d0e85d34d8089f23cf48c71d652&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:07]
https://soundcloud.com/goldxwave/never-lose-me-x-one-in-a?si=c972d54adc83439280b90d41f457ce58&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:07]
https://soundcloud.com/lovv66/og-buda-lovv66-toska?si=8be3992b25e3487ea31ba732b1d63454&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:08]
https://soundcloud.com/the_9ine/obsessed-with-me-with-rubi-rose?si=0ca43e24c8b0403385208b41386dbb6e&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:08]
https://soundcloud.com/mof-e/prince-of-egypt-act-ii-your-majesty?si=c6e0579911fe429092ecd4b51d8b9a4c&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:09]
https://soundcloud.com/teamtaj/dj-taj-angel-numbers-jersey-club-ft-tricks?si=2307d860e3a44985b85f0bb31b759409&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:09]
https://soundcloud.com/guilbes-jules-635679714/crew-love-g_unkown-x-loog-jerseyclub-tiktok?si=cf991cf6d4464fc9914efb6216ed1e0a&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:09]
https://soundcloud.com/cactusjackutopia/jhonni-blaze-fumble?si=aff984b918f0464793ea42845e1f9195&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:10]
https://soundcloud.com/djryanflossy/ice-spice-princess-diana-remix-breezy-bad-btches?si=122e13963512437e8f4c151b8b043750&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:10]
https://soundcloud.com/user-348377214/no-more-excuses-sdot-go-x-kyle?si=da0903f8821b449a933a529bbdf24f0a&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:10]
https://soundcloud.com/user-554403881/buni-demon-rejects-uncensored?si=ead4beb4811d4348b19ab73342bb56a0&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:10]
https://soundcloud.com/unclewaffles/peacock-feat-ice-beats-slide-sbuda-maleather?si=afda9bb2234a4c8594bcddba423023f0&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:11]
https://soundcloud.com/fendi-da-rappa/in-the-trunk-feat-glorilla?si=e38fe4ed467640a09450bae5369b83c3&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:11]
https://soundcloud.com/funk-hits-oficial/mc-fioti-luz-do-luar-2-ciclo-lunar?si=3c09a501f76b4d0496d4bebac660b750&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:11]
https://soundcloud.com/frenchycal/lose-my-breath-2k15-jerseyclub-remix-x-frenchcalhoun-empiremusic?si=918cb0841bcf47a1b112f52fa43871c9&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:12]
https://soundcloud.com/iamsbf/tims-intro-jersey-club-feat-notorious-urb?si=66d204d8784149fd895c112dbb800e20&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:12]
https://soundcloud.com/davinciiproductions/officially-something-ft?si=44e73e068b6f403eb35cf86e789453c4&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:12]
https://soundcloud.com/treohfie/tre-oh-fie-stand-by-me?si=3b979e39d62c42a4a6b2c1f4a9a3bb27&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:12]
https://soundcloud.com/gangwalkk/jersey-breeze-legendary_tah?si=603b1f4cbc2d4df4a86c9cf851ba8511&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:12]
https://soundcloud.com/thrill_pill/ushira-thrill-pill-tvorit-volshebstvo?si=99119acb9c024ecda25a4d8c62f7afe2&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:13]
https://soundcloud.com/fxb-779282176/shabjdeed-mtaktak?si=81038ad2d83b4e058ab7456fbe3cbdeb&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:13]
https://soundcloud.com/raymonddeejay/tyla-x-raymond-x-walshy-gypsy-water-clean?si=44b125c6d0b6423cb59fb56b6a51fcaf&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:13]
https://soundcloud.com/lastfragment/vechno-molodoy-phonk-remix?si=be47cc7053d6425894f095cbe7f50f6f&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:14]
https://soundcloud.com/retr00j/pennywise-story-it-retroj?si=6d559039388e4282908efe3881162fc6&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:14]
https://soundcloud.com/vory7/bad-guy-freestyle?si=4dab901064e546ef8ea840d99d5909de&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:14]
https://soundcloud.com/user-54294422/point-me-to-the-sluts-fendi?si=c773b6df70b04c7a9e3b6d9166db6bf4&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:14]
https://soundcloud.com/fxb-779282176/dnob8vqxjacp?si=f77fbf443f55462b85c0a3c2164bfe76&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:15]
https://soundcloud.com/kevindaveprod/rihanna-x-burna-boy-x-spice-x-daddy-yankee-jump-x-last-last-x-like-it-xgasolina-kevin-dave-mashup?si=828d282962c24446b487bbd005e7c57d&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:15]
https://soundcloud.com/riddla/riddla-x-oxlade-ku-lo-sa-amapiano-remix?si=ef7a1a1183dd4be29cb7af6d52841dca&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:15]
https://soundcloud.com/riddla/riddla-x-byron-messia-talibans-amapiano-remix?si=7748b209cb6248f19ed4a0cb20df3eb8&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:15]
https://soundcloud.com/seyoum-kelly/shaunmusiq-ftears-bheba-bheba?si=0d241ede0f9a4d0eb2f61932f0b2fae6&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:16]
https://soundcloud.com/eee-ddd-108588586/playboi-carti-ft-smooky?si=6db31c82c860494caf6e446d96fd5eb1&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:16]
https://soundcloud.com/chromebrokenhearts/estakada-feat-mayot-yungway-lovv66-scally-milano-uglystephan?si=5ffde8270a0f4deaa0bc73e576a01b7f&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:16]
https://soundcloud.com/rainbowcrvsh/scally-milano-yupi-yo-instrumental?si=667e6be489484597a176f5fdf5d76655&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:16]
https://soundcloud.com/nigelcoronamusic/yebbas-heartbreak-jerseyclub-remix-slowed-reverb?si=f11601d9424c422bb9264e36a6940617&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:16]
https://soundcloud.com/rrodney-330740734/rrodney_x-kaoticcc_x-chillznyc_come-on-jerseyclub?si=b3f7182a0f75481d9356c0f485348515&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:17]
https://soundcloud.com/the-cookiee-jar/no-lies-feat-yu-nova?si=e22d5fb6eabd4d418d29bd31d7770755&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:17]
https://soundcloud.com/phantherrr/playboi-cart-molly-destxmido-edit-best-instrumental?si=6855c67073b146b4a320998ae35858e5&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:17]
https://soundcloud.com/nynekk/solo-future-speed-up?si=af333399f1284b5d91a12ec4a2df4c3c&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:17]
https://soundcloud.com/deejay_j3/mnike-vs-drift-by-deejay-j3-remix?si=71d8ee0bd5014628b716f90945f942ea&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:18]
https://soundcloud.com/kevindaveprod/nicki-minaj-x-teejay-x-spice-x-vybz-kartel-red-ruby-x-drift-x-whine-kotch-kevin-dave-mashup?si=3ed0015556c94ab7ad39ee1cab136809&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:18]
https://soundcloud.com/user-975702863/so-sick-jersey-club-feat-mvntana?si=ef0c1415ad2e4dceadd1ce24e4e82b64&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:18]
https://soundcloud.com/nassietheproducer/workin-dat-back-twerk-anthem-nassietheproducer-4dabuttz-fmoignxssiegang?si=b74584fdffc54ec59de37622e9b59853&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:18]
https://soundcloud.com/gangwalkk/my-man-gangwalkk-loog-prodbyabnormal-thank-you-to-my-man?si=f0cccd9380fb455fba21b4a7846106b0&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:18]
https://soundcloud.com/msundqviist/ofb-akz-x-dsavv-far-from-over-exclusive?si=036fa88896a14ef99ab24a29b3e63c05&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:19]
https://soundcloud.com/user-690903937/ice-spice-x-pop-smoke-deli?si=79df41cbb8ab450b8d904cc062df30a5&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:19]
https://soundcloud.com/user-788537184/loco-og-rocka-thewolfofwallstreet-prod-by-polo-boy-shawty?si=2b96bdabd40a4fe9b33babe72718a66e&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:20]
https://soundcloud.com/chekksean/spin-with-max?si=d88fb7fb558040578e9151ddf3c3c679&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:20]
https://soundcloud.com/xizhon/xizhon-the-weeknd-run-up-trust-issuesremix?si=1576ba98e4614249b15757f2c4710ca3&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:20]
https://soundcloud.com/jaythemixer201/bender-99jaythemixer?si=3b9e90cd2f8b49b0852c7b584f09a88a&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:20]
https://soundcloud.com/c-him/be-my-lover-3-dj-c-him-remix?si=400b3d9c1da54464923b32d82f9e86e2&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:21]
https://soundcloud.com/user-823195875/f-e-x-burt-ultrakill?si=980ae42a0c8a42f1a6a8b1fa9c9375a2&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:21]
https://soundcloud.com/countygoatloog/janemba-200bpm-loog-x-samu?si=21937f00912b4fa7b3bbafc565159f9d&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:21]
https://soundcloud.com/jaytoonz/jaytoonz-big-up-ya?si=5228b7bf9be345dab18bee8628aea740&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:21]
https://soundcloud.com/dj-clubhead/kehlani-can-you-blame-me-remix-clubby?si=b844d1d6890e4deb91e1f834fa64def2&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:22]
https://soundcloud.com/onestopjubee/bend-ova-gurl-onestopjubee-x-abe-jerseyclub?si=5e24da43816941599ec0cd6494057713&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:22]
https://soundcloud.com/teamtaj/donk?si=397b6932f311489099fda81794330cbb&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:22]
https://soundcloud.com/jaylacag/hoxton-lsav-one-more?si=6dec43039f4740288e932ad71f7acdd3&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:22]
https://soundcloud.com/vsremixes/ilham-finesse-vinyl-shotz-dancehall-remix?si=39b44067785d490aba86033db03a6311&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:23]
https://soundcloud.com/aloffxcial/bills-bills-bills-trillzal?si=95c09c77abeb4a8f99b4f1baa4a978f4&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:23]
https://soundcloud.com/djassassin13/just-a-lil-bit-remix?si=4886f6965eef457cb79eb75bfc90570e&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:23]
https://soundcloud.com/lada_babi/beyonce-party-dj-k-millz-remix?si=422ca40dfa6e40e3a595535efdbe7083&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:24]
https://soundcloud.com/whoisluci/before-i-die?si=56411217493f4d62a289681d8f0daa6d&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:24]
https://soundcloud.com/ivy-shields-329064628/running-through-my-mind-dej-loaf-sped-up?si=a8076656f7aa49848ae03eedfd0656ec&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:24]
https://soundcloud.com/10234567/turn-me-on-jersey-club-remix?si=82e2119b468c43ce95e0a2fbed9bacb6&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:24]
https://soundcloud.com/milliamusic/neededme-rihanna-edit?si=7251803fb3434fd8a2c87696b6710b63&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:25]
https://soundcloud.com/kylan-157398552/everybody-sweep-tg-flockaa-x?si=08ce7c1c25e3453dbceb3a92741f6885&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:25]
https://soundcloud.com/imaabs/meryl-coucou-imaabs-edit?si=66e6f262ea1e4b2bb10e1fd762c0284a&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:25]
https://soundcloud.com/crucast/bru-c-bou-streetside?si=8c01ae23326e4cb2bb58da52e6f3f0ad&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:25]
https://soundcloud.com/localactionrec/uniiqu3-unavailable-feat-r3ll?si=34f9547c8a4a49db91476fd6b9ba33e8&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:26]
https://soundcloud.com/hypnotone/chris-brown-x-nadus-x-destinys?si=2d7e5ca1972d4783a6c7af94c11639f7&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:26]
https://soundcloud.com/nadus/drake-ft-the-weekend-crew-love?si=1e2918f9ea2144f2985a5da9b2552d6e&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:26]
https://soundcloud.com/abigail-mena-580813828/fuck-up-some-commas-jersey-club-double-tap-dj-lilo-vmg-ig-djlilony?si=efbe0ddc7e4c4aeead40b4afd039da2e&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:26]
https://soundcloud.com/tamecheetahbeats/good-mood-5-jerseyclub?si=c153bbb6ff604baea7ff3d1a09830569&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:27]
https://soundcloud.com/abcash495/360_heembeezy?si=4ae8a573350344b1b25e395e8955a370&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:27]
https://soundcloud.com/iamhofmannita/saucebaby-hofmannita-nikogda?si=4036b7c3d67241a180c882154557ef80&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:27]
https://soundcloud.com/djk-shiz/drop-down-to-the-floor-2?si=e409f9f6af4b4a28b38a7269b1329057&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:28]
https://soundcloud.com/onestopjubee/bend-it-over-feat-brikisses2?si=0565a5de907243b49e2da8445bc3fde1&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:28]
https://soundcloud.com/nassietheproducer/pump-up-da-jam-tik-tok-anthem?si=55f9113d48b248cba9a3a016deef05d4&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:28]
https://soundcloud.com/gettinkunt/like-ice-spice-unreleased?si=b494ee599a6641fe954aeded7ce19f2b&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:28]
https://soundcloud.com/jalen-justhangin-carter/ukusa-ft-swae?si=5a8ecbd0fb6e43278ac10ec55392898a&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:28]
https://soundcloud.com/spedupmusic/jeremih-dont-tell-em-ft-yg-speed-up?si=8ce3d6c9debc4f05bdcd6c126ecd8e02&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:28]
https://soundcloud.com/gravityboys/ecco2k-thaiboy-digital-1-1-ft?si=da5bdedb714c44218c3941d7d2d75178&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:29]
https://soundcloud.com/deejaytricks/big-nuni-tricks-turn-me-up-jersey-dirty?si=7101462c41e54a84bc5d08af8595af69&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:29]
https://soundcloud.com/lilsnatched/bad-bitches-lilsnatched-x?si=8a500e73bc894a9485be7c07d19cd0a0&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:29]
https://soundcloud.com/arnettjtm/ice-spice-nicki-minaj-princess-diana-x-jay-z-tom-ford-mashup-by-arnett?si=fedc0c049d084e3cb377fcf7ee7da09e&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:29]
https://soundcloud.com/nassietheproducer/lil-uzi-i-just-wanna-rock-nxssie-remix-nxssiegang20-tiktok-moviee?si=ca72721f2c5246dca0081c843d5c2346&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:30]
https://soundcloud.com/djneptune973/djneptune973-going-dummy-ft-lola-brooke?si=d7324046a09d420380acb69c9db7a63b&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:30]
https://soundcloud.com/imbald/airplane-mode-sped-up?si=0725ac52c9eb45aa9bd3c72e629526ec&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:30]
https://soundcloud.com/pesdalisik/sh1n-molly?si=a65222dcf9ef4777a8507fc55dacfa69&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:31]
https://soundcloud.com/iamzxnny/jayo-22-z-mix?si=194dedefd8ea44c19b26a49d01befac1&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:31]
https://soundcloud.com/zlatanibile/only-fan-feat-lojay-dj-neptune?si=513761ab53074d97bf397e9e30eaa7b7&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:31]
https://soundcloud.com/shashu/chanel-rihanna-shashu-remix?si=e179e6b2bad34a54ab67d9eab9aa42b6&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:32]
https://soundcloud.com/0ojak0/call-me-sturdy?si=ea7696eba92e4263a1742532422891c2&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:32]
https://soundcloud.com/aidenschlecht/still-into-you-drill-remix-1?si=caca0a58a0af430db4ecb5c059e77346&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:32]
https://soundcloud.com/djmisee/amapiano-pure-vibess-by-djmisee-ft-woza-la-hamba-wena-zotata?si=35daec2af03f4d4393378e5f71607395&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:32]
https://soundcloud.com/heimanux/tek-it?si=5cc0c206a6e24fb89ed0ae3e9bcbe98f&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:33]
https://soundcloud.com/so-vis/kitty-phonk?si=8cbb8af7bc044eb1907c9f167b130d6f&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:34]
https://soundcloud.com/ogbuda/tourlife-rip-x?si=8249d45bfbcb427cad2d9bdbb00fd311&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:34]
https://soundcloud.com/eugyofficial/eugy-enough-for-me-1?si=81c5f9de3e0447f6b3b89ae9c27fd017&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:34]
https://soundcloud.com/africanmusictrend/asake-ft-burna-boy-sungba?si=70901d99bcb54b45b75251a618d20706&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:34]
https://soundcloud.com/sliinkofficial/dj-sliink-break-from-jersey-booty-bounce?si=71b99ee3547c452aa6fc7d27902c866a&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:35]
https://soundcloud.com/heslosinghismind/sahbabii-squidrific-slowed-reverb?si=22d7ec2d2cfb476e885f823239d61b20&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:35]
https://soundcloud.com/lxnerswxrld/keh-ani-can-i-ft-tory-anez-s?si=ca0c157cddb045e8a8c188f9d9589be3&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:36]
https://soundcloud.com/kehlanimusic/can-i-feat-tory-lanez?si=1669c75e436a498992cc1cbc9f1f9871&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:37]
https://soundcloud.com/itsdjproblembitch/rxady-2-go-dj-problem-bandit?si=0362add476ba4302a553ab7d3c913265&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:37]
https://soundcloud.com/piffylongstockn/show-me-love-jersey-club-remix?si=6688ee46b6794ae4bb2d9a262db55c26&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:37]
https://soundcloud.com/sliinkofficial/dj-sliink-ft-ice-spice-in-ha-mood-2-jersey-club?si=63f9378e5b2b42b89711b942440d51de&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:37]
https://soundcloud.com/richibeatzz/playboi-carti-thraxx-new-songleak-prod-richi?si=02b60f3446ec42309e0244c3b5a60c91&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:38]
https://soundcloud.com/looffyswagga/govorish?si=7cf6e5c77c514b728d83414f9f4f20df&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:38]
https://soundcloud.com/babyxsosa/girlfriend-prod-isobeats?si=7eaf6862fa634c968c762ee81b15742a&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:38]
https://soundcloud.com/goodiearchive/numberone?si=494c6b5c9d6a4eada4c00c71109da6e2&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:38]
https://soundcloud.com/guttamusic/do-it-tonight?si=61714500f9a540c8ac2285f9d040f4fc&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:39]
https://soundcloud.com/roddtheproducer_908/roddonnabeat-x?si=7dbe3d3c15da4661bdf55ab21ecc92bd&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:39]
https://soundcloud.com/sliinkofficial/dj-sliink-presents-gangsta-grillz-volume-2-cannon-official-intro-2023?si=3fe742c782a7405db0f210be11197dfd&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:39]
https://soundcloud.com/ay-beats-productions/frenzo-harami-x-caps-type-beat-paranda-bollywood-sample-produced-by-ay-beats?si=ef9744a8bf18430db127b779942cf2d5&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:39]
https://soundcloud.com/lovv666/govoryat-cho-feat-blago-white?si=23de4fb505ea49ccb1b19121da7dd857&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:40]
https://soundcloud.com/tolik-da/aap-rocky-shittin-me-1?si=9f9b7e77bded493eb8a0b8fec8ac315c&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:40]
https://soundcloud.com/iamhofmannita/pechen-i-serdtse-feat-drippin-so-pretty?si=599a9f1c6165468298059653fc34435e&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:40]
https://soundcloud.com/lilwannasleep/kodein?si=aeb5b57fa3c04670a9dde66ddd98cd96&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:41]
https://soundcloud.com/destinyy_duhhh/touchin-on-your-body-merks-cueheat?si=ccbd2ec944084273b2def4b99199758c&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:41]
https://soundcloud.com/iamsbf/my-neck-my-back-20-forever-ft-tricks-dj-smallz?si=5aa43dd6887c472897d85a4315f7c222&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:42]
https://soundcloud.com/cheyxoi25/amaria-bb-its-on-fast?si=242e41b854d14128a286c86337c56d28&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:42]
https://soundcloud.com/finesse4real/og-buda-mayot-17-seventeen-vina?si=4216525f7ed44d93858e0f6b2411d38f&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:43]
https://soundcloud.com/etyunjfb80zz/yfyfyf-ingushi-kabardinczy-mp3?si=0b71755c898342e98b89478c937050d8&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:43]
https://soundcloud.com/orbly/streli-jersey-remix?si=5dfc8b583f974b8ca7cd86dcf5393ca9&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:43]
https://soundcloud.com/user-413997109/the-garden-state-blue-n-green?si=844b9eb5e25348459c1a2f6bca48101c&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:43]
https://soundcloud.com/finesse4real/plohoyparen-853891146?si=5d27529de2474005b0633aab9521bc84&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:43]
https://soundcloud.com/mrsginger/pen-push-up-rap-goals?si=5403911609674fcb9b9c6f2f5bc85625&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:44]
https://soundcloud.com/tamjidd/yeat-playboi-carti-on-me-prod-tamjid?si=228c03e789954dc7ac3e52015e4099cc&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:44]
https://soundcloud.com/770rd/poland-lil-yachtyprod-f1lthy?si=037403f531974f3e9b2644e117f82583&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:44]
https://soundcloud.com/iamhofmannita/poshlaya-molli-hofmannita-habibati?si=dc71b9e43214465aadb6f1a9bf42f037&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:44]
https://soundcloud.com/officaldjtwinkletoes/that-gwirl-ha?si=7699530234304fd58d59655ce072cd3b&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:44]
https://soundcloud.com/xrig00/still-countin-x-prod-xrig0-dayday-jerseyclub-yeat-labgodz?si=42babaaeec8845c39e37e35d0554096b&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:45]
https://soundcloud.com/itscarvell/futsal-shuttle-2020?si=90c20807938b4c21a4167883dd0788ca&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:45]
https://soundcloud.com/prodijee1/collide-prodijee?si=6a9cb8623a8e47ecaa045161cd9d7283&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:46]
https://soundcloud.com/galactikbassmusik/wrk-back-n-it-remix?si=18413fb90d684cd9a57e9e047debc5c7&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:46]
https://soundcloud.com/djdirtykkkk/ljc-by-your-side-dirty-k-remix?si=ba4b28ec8cbf47f69965b68e29aa7ab8&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:46]
https://soundcloud.com/bannan-chevis/big-bannan-x-don-dzy-lonely?si=d146103ae3024329a6b2e7d6851e7f2c&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:46]
https://soundcloud.com/free-rap-trap-beats/no-diet-uk-drill-type-beat?si=f2ba88ae4f4948378e5bb9b2819a919c&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:47]
https://soundcloud.com/talha-asif/like-a-g6-official-1?si=a1ddf8c5c31e455ebc3bfda448423975&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:47]
https://soundcloud.com/samiyah-amina/yoin-digits?si=b6fea82b7ff14fa5a5f56e307f5c3ca3&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:47]
https://soundcloud.com/arnettjtm/burna-toni-bounce-arnett?si=fc305af202cd454099dc05bbbc19664e&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:48]
https://soundcloud.com/iamsbf/massive-iamsbf-remix?si=f6675fdf7e0f46f4ad0ae19b31d3f384&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:48]
https://soundcloud.com/thrill_pill/uzel-ft-plohoyparen?si=d599a7284f86483c9101ea7f4c09634a&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:48]
https://soundcloud.com/layaly-gamal/the-synaptik-haykal-shabmouri?si=c489cadcec614ec5bfbb8acb2e6e7850&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:48]
https://soundcloud.com/rahswish/tell-em?si=54af772e442c4566a6e5e1d5c6759a4c&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:48]
https://soundcloud.com/bymacca/miss-the-rage-reversed-x-escape-plan-macca-mashupedit?si=db7a576df1a742b29b8e9ef65c480e4c&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:49]
https://soundcloud.com/da-golden-kingsley/xclusive-dj-golden-mixgyptian-brick-and-lace-hold-yuh-vs-love-is-wicked?si=9f74f2200fa24ed383e4e4d5b8b24276&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:49]
https://soundcloud.com/rudebone/bandana-rudebone-dj-kunsept?si=dcbec893d78d41eda4e6440ea60c2940&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:50]
https://soundcloud.com/tobago-tracks/bambinodj-lost-riddim-1?si=3ed75f7623704f40821f6f30374f97ee&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:50]
https://soundcloud.com/ayeshachanel/chanel-manita-de-fatima-prodtriggertracks?si=b716b6f8938c497a8e0aa00a9045ca8d&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

jafart, [06.07.2024 3:52]
https://soundcloud.com/luc1dsc/get-up-on-the-floor-jersey-club?si=ca7044971c364b08ae2452512e0ca28c&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing
    '''

    parse_and_download_tracks(message)