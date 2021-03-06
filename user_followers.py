# -*- coding: utf-8 -*-
import sys
import json
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

from zhihu_oauth import ZhihuClient
from neo4j import Database

client = ZhihuClient()
client.load_token('token.pkl')
database = Database()

# me = client.me()

def user_bestanswers():

    # userIDs = database.graph.data("match(u:User{topicID:'19554298'}) where u.name<>'匿名用户' and u.grab is null return u.userId as userId order by id(u) asc skip 150 limit 50")
    # userIDs = ['13ba78a859eaf6b9a5b27c5c56ee8419', 'a7c7015c4ca7c3104daab2e9abfedb57', '64fa851552b5600b7c8be72165edfdaa', 'aedee3338cf0437b9f28f20c8d6dc2d1', 'cc238666dd4406d7abda8090a04503b5', '2307d4205a82926f3617da53423a049f', '0a60bd319fac005341466c38de50afc8', '4cb6d3b7b099b64c1b506c667e7306a8', '6b630094ec4c56d07eba3224e370fecc', 'ba4db02667f457a477aec36121933b97', '317fffe6dcd8df5e5b9c2d9087a4382d', '22d1cc2d518948d2f689c847258a7881', 'fd7c571a0ada1a72e42e8d7992c4a780', '3049d74682543a3f8f73b57964bf5db3', '6bfad8199c976be84f00a7bdc078d4f5', '8a6a82ca0532b6af42131f49706fc0f7', 'da4acc1b0a6197e72ca6055a67fa9d7d', '0e512d1ab8402ae4a2517b241bccec8f', 'd5ef4d4aaa08aaa331dabd8d4f79d0e9', '044eb2b3d3f9af5d1a79830d351c1dc5', '2889bfb08d752d394089da3d8b8d2b59', 'd59999d973a2e7b49a246d5754c8270a', '13d36f4d156f77e009c117b6021703e7', 'ebbe6e14adde32eba8d014b0fcc47dbd', 'c6adcb1f69bff45a74f57f4e2150dc3c', '4952252c6cee7ec5fb6e145456487621', '3212f9044005e9306aab1b61e74e7ae6', '0c6e41c0da1b18aba0b97975c1e4b09f', '2c5ce9612b1f25a3f3bf251a09c904b5', 'ced30ef2e460b4febfd77ef3038167ce', 'c477767e63254f832747e1e99329470c', 'a79cce38125d71baaf2188da72822b11', 'a6fecae6ca1389079dbb63d0b4368eba', '9959e364fc3b62367c587c4697d8a8fd', '9558cac1a967147f0318fe6b7b1a0f7b', '012fa0165014b9e7546ca9526461a7a9', '6fe49daa35fc3eb8f10d00d59cb1c45b', '40b164683dbaf1ae328756ad8bff0e82', '8bed628a9d3e752070294349bd5f0b12', '225cbdbbfac26810c6b71ce96f55de2f', 'b5a0612700ff2573650494c01895d20c', '6e1a145fbea96fe6c16eacba4cbb3d85', 'd471405572fd829578df0319618132ad', '73dea43918ac6edf7b152eea6eb87cd4', 'a482f5dabff2e9aa22e857e5bd951d17', 'fd5d50994743daf583cac4d510b20558', '33b61032ede4c22848160527ff9a9de9', 'a88640fa29ac407fd45cd45967b42a4e', '0970f947b898ecc0ec035f9126dd4e08', 'e62f00265931ac106064ccb77e876b1b']
    # userIDs = ['d2aa63540e4481bbab493175a262a042', '9e9ee1c749f6be0966ea5cea3a38884e', '47d3a73288d62256902ce9209acb3b35', '8aad4f38cf19a691ef2135d3a85bb612', 'e3a9ce94cda3a3f8acaf6da62f0b75b3', '557cc99bfe762006cbe8be655320af2b', '5a89e9dce88916bd01000d7f9985af94', '4c9dd7ce259e3e6ae2f0fa6ca42801ee', '07cb6860e9028ac1d987a5ab1c50c71e', '6dd067bf5573f2a38d487ab6f67b0431', 'a61ff943505b062db7cfceb36ab03014', '6ef2e77274cb0719253a577665cf690e', '7f3e9504e4fad3ff0205e33e9c1b008d', '508b28aa428e24fdabe3a89773ed3b22', 'af62ea77af08fa35799f843b60badd96', '446e9b4a22efcb71fec70800df455995', '7962727afd727f3fb7c27f7c70482881', 'c379ed1787150ed1a16124d279d1aeed', 'c3e462c36fdfa22e4eaebcb0323e39c9', 'f878db365246325edc35055891fb50f1', 'b830f90d42560328acfd2a85ffcfc35d', '4c0b95ee7a64010cd92cb88809349def', 'c8d22cca942a39ba1e554947a7361834', 'b53d00a3f1ed7e2766ba6bd5d8b8b77b', '7b6393283b8c861346793e7e61dacfd0', '86858a7a4aa77d290364625efcaacb70', '0630bd0fc3a60f77bc9b4f0edb0b5f98', 'af5220816d1bbb32f315611ef05659d6', '2fbe89f73d184baafe25c3e1bd9453ad', '126c270e54b9c78b800c0ee716dc1533', 'ff3ffafc788874278bac775977dd8bf1', '81e52da0a8189e95f7106160d7e8633e', '71f60bff956386a418c70db7fd65c0de', '0b6d6678b208a32e620775464bfdc0ec', 'c1c892f179f95da8b37a1dc604839d2c', 'f034af842cad3109523a21937a5a2fbf', '4920fca107ec266a26bf578ff112a6d3', 'fd51f37ac298387052e18e73158e3187', '7e014672f2f2cca26ac57b0e4f9fa359', 'a7e9266e7a6793e5843bd35d375a1cc5', '33b6fa3aae4eeb70fb0ce62e9bd358f7', 'b13dd95b2351a49867d3ac60c7670fe3', 'fd3dbdff0811166a87250acb815e03dd', 'eaf435b228ce0b038a4afe8203f59b49', '5ae91eb539f2dda88707cd2ebce3a4c2', '71637fe077b9a2d7be320e2800ccd818', '3d5b47d91b2d8283e9189c96e75b554e', '64611505e2b3fa65234b91b0136d4dd7', 'd2fe6ae843a10d589b8a0bebf136dda8', '68bb20e3a37968e48b34a4a8d07fef8e', 'ea31ec803eef405b08c99a1e38ba7439']
    # userIDs = ['913443092e5f0e270c794067a63c6590', 'a1e6c1666f677a126b8023a19feb6c76', 'e06f30956c83a8f9745abe4d21b55c58', 'b86a6e1f5acec6616f4b96f32bfd74ea', '184d63c15edb58b42e0a02628945fa76', '9298714d81042fe201badf5ae36cb9c5', '6cf564f2ba06cdea67bc3db83e364e42', '2811e176fee847ccda32e8cef2d64b1e', 'b7a864fdc5cb9a7aa25b2521a518b670', 'da007c93c894ec199fa111b65ad50e6a', 'b94ddafa293d006d853b3270b436e24f', '59fcae62596fb6ba08f2860a5fe6f171', '2e3ed6f53aaf5cc6cd7c714d510befe5', '5e1b090bfccfd65fcbb8874610613c17', 'f3a4eaf32075bc78047833788a64699e', 'd2e4767a8475e98c2b7ed00e04bd396b', '7240b2ae38836f4837c2d7355b2ee72d', '710eba6a35a79b11101c571177962ffd', '11c60d07820333e540e2dbc9c45c299b', 'e8d88045c67c8d3d4622ddba084f837f', '3b625deb18f23bdedc3a984b8837ee33', '07691f2649ffa9b9d0f5bf4960615a37', '5874b9fc2c79879886cc9caaa2aa1492', 'b6434d4c9bc43e9b26fa3757d16682f6', '8f3d51f2019c445f6759de75e791712c', 'ce40c704800079110fac389de1d6f57f', 'a67d8786ea160ae9f351f919bdf50a42', '6b67515a2a52aa37e09fafb9151c3d0b', '5a03599103a14853ca1fa633f10ff90a', '56d815fee99b300503f145502bcdd06e', '9c320789933cd00d55f43f690796066f', '11c4242fd92613a7f85ad9fff60c29c9', 'd2ffc0b141affc7d146b81ef0e51f793', '8635a46c137bb5f6c4b729025a07e3d5', 'fddac274446bd2cc9f57f765b2237511', '5280cd1d7f0aa8701e0db0ff1719cdd3', 'd5b1ef5682e3799087404a8f9f9911a2', '8ddb56915cba77bb5216250e5ea66158', 'c306d62d8f9b8b2428f608ef2085225b', '8a5061a695d8825220515490ef0579cd', 'b6d28ac2b88b7f230552bab4a0aceaca', 'ef35bd4a24d7c3d32efa489256bfa035', '1c07593b7f654d83178d910798b83c4e', 'd24f457cbb7237dedb044e36859e6151', '31be21fc552f6ba19a99df3957eaa2c4', '5e17a77873f7697eba699623870439ac', '461de99bf9c5ee3c71b375c803919376', '4fb1ae49d3855f27dce6a68982db3245', '94ce7e96ee47ebe4abaaa5334c5ef672', 'b9dc73bfdd3b51af128b800d2d1a8bd3', 'aedddd3c2544112b9d83b06d7c5cbdb6', 'be1a629f6fd8c81dee1d8c55365d440b']
    # userIDs = ['3bc44825e051990996115e575b3e04cb', '2abace86c9dcd0709de72b4100ed78b0', '2608276c748748cb2b7443adc51cf890', '745f68a74a02e49711cc097e1855b1e1', 'a209c6e6fce1e6b38c3381822e93b736', '5afe981cf9daa29842e836695bdc7fca', 'd9986e0277865c6e072e70bf322fd982', '61dcd85a914cd5ae545c8dccf380dd66', '6bd2fdf394e6b537279bc68c7f7903fd', 'df7258f9a4c6d7572a706c08c26963cf', '20e911524247b63b55decfbe6080aceb', '1c3369bbd58b14ed815011effaf0895c', 'e000a9cfe2bde20026589244fe339cde', 'cfdec6226ece879d2571fbc274372e9f', 'a21f8e9dc63e1c10f7619032156fd869', '96ead89e2fdda4f36be32ac625b2ae1e', 'b07903863cc25ca0c66968ec13a0d075', '129fd2d679c7c5529b4f4ee59cf45fce', 'd38388a2efff44b4454096180eaa7e45', 'a18dcc6f00961a04f4cd525392a6f678', '3ce01c8716a208c76b1cd2c9c15ca9ad', '5f20bc6faab23bf2f44b50ce282b37ac', '44f8bdf68421131645b6f262728f8970', '64d972cc5bae62489442e35b32dc0fce', '495c9da6e6e559dc30a9b8edb366c620', '6a054e26b6337424edc883596882a8c9', '50c983ae7dc963b6b4431d262acb3c63', 'a1d971f2154a83f8b975093bc22698b6', 'e7015c71d121b982319a6e247050f536', 'bfc066b72b540aff07ac780dec116124', '1e2c9261b85996ccc3c5436850127e33', 'ec303d7e6a3f10c9cee3aaecded6671b', 'ab5522d09083da90577fec1eeba69001', '4f7c9e13702f5fc6754d93208162eb4b', '2c261f1c1ea50cdec6c8488f21c5327f', '8f61ccf91855babb2ed54ea0afe0ae29', '7fa5026e74e6ba8d14f7b8b1d5eb873a', '39c850a21201193173517ef32b7379c1', '5182e7ba5562d67c7578bfa03d4ec388', '2b288852f51067e3a6b7404b7b496989', '9952afb07027dcb513f66d9e1cd8f3df', 'a37a4b9a815e1c88c445a17bd658aaad', '676634384fa772b6bcae8cec83eb3b29', '842e4fe986283e7132d8e0d5f9202973', '1c7f429366f5db6b3cf05e2b6eaac0a9', '78dedffbc01a611126ac203cb146d406', '580b81d81d27e62a1660972891cfe2fd', '6615469b87a411227fe0102b2d9f8d99', 'dd86fd536b5d1709dcc5f8828eaf28b2', 'ae64cbc1c9d1159dbdb497b2410babfb', 'aabde7cc5616a826c22db37e22bd9c8e', '29a386cc4b62dd3a95af790ba2fcf1cb', 'b228918246a65d9e16d5c0f6a8329205', 'a06cfb38e37dac1658e6457df4d7f032', '78e3b98074a915b222ae1be4ab038a6e']
    # userIDs = ['033aaa7b41577bdf4f5344943a28dbb0', 'a9767cdbcc0404778bbb0e6ddeab0eba', 'c67d30567c1ebd6c36ca4352d2c716df', '97afafbef6a1a9e016e4d82a009ddfd1', 'bd82ddabd837505f49d031ed61191f86', 'b643d703e77a5775e1a2cd0e23bb84be', 'e90f6efea7193e51f49f55ac1394a9cd', '5205731f359c1ddcf75489b92269541e', 'c265de1dfd836bf0f644c8e0123e53a4', 'db6c847e3cebe429cd77f92002fa4723', 'ce818bf23f05445cfdf62f79075a6077', '6d11f4d0ce00d647330b9d917e91e56e', '8366575cfc9846f14d3fb919baedbd19', 'ce0e506d9bf9409430da37e7d6e4270d', '32552cc48792c561eeadf5559cc7d620', '9ffc73a3ef7d14df1a9ad1bf9effca1d', 'ba4bdc344991e21bd1e34560c20a9ea8', '960e5e06bd066473de06f7a00b6c80cc', '87a3b6e08f65f7edaa1ad76f5611bc1c', 'cdd2e158b4ce08b7343959c85802b5a2', '4b6d9d23690d4c526341b26fb93ff568', '69c1e58d312948d357fabe529e719876', '98c3d502b9dc1c32f5e4a19de2173f7a', '7c1a9c880510c38533e76303adc2fc59', '28c21455a93d30c205fdf268a92b867f', '3fc0e5ac8e0e61552b1b0529ba49b3e7', '5ca33aadc924dd61277b96b0cf1f7814', 'af8dddebc2e4ee235774f2b8ffe6bbe2', '5857470f6197017bc6071db75a99d493', 'f8a351d7e9dffd38c89f9244a7ab3e7f', 'f44dbffad299aee0f2e31e1bfc9d9071', '2a87fad28e43b886a4ca144b784986e5', '8b868bb9f1be69bc35316d9f9ab3accc', 'eef16ca7df4d4cb380f5f6ae41eefe84', '772ce49683f339d80f6e0b10e60aaad6', '0864c2e91232dd3802f7c7c79a38016b', '16b06a29ab688e636680780f9a7a0d49', 'aa470e33dc1db2877185401e45c50c42', 'f30335ec306e04b89da9aeeb3fdd8218', '6b84dd88098fbd97748a703740e52877', '98061517b5aa6dc34eefd133e0b58076', '4f03664cbcd7f28be57c03b845fddf68', '7c57858c89be08c6b14ce0d1ed3fa79f', '1cf49425436c8dd996ac5ba1f1ed46d9', '6a98a308b2a0d34fa2449555b92bea94', '26bb884219b1de428f3bbbb697f03f1c', '55ef9099b50de6ac0c3acc5692f8967f', '872194797a5c6642be2eb61a8474a5ba', 'a5c0ae00a41898390ae63f77f015da00', '18e2fb6b157c0bf1e426f12a14c3c8dc', '25193db88c3ce879aa864e1802b5fada', '9717dc1e245c951531143db76f61f65f']
    userIDs = ['7414dbc04055e1dd78950f3dfaebb932', 'bbb58b3cf74a5fa7e835c0358e430acf', 'e14d03bd80efa2edc3ffc87478632587', '6e0f3effcddf2f7094599db2a2414c36', 'cc8ca47dc982c7d7ed88612630afc29f', '1967b75baca614c950a8473510c47f28', '96479e64f5cbbec5139bdc2d60e30351', 'ab29231e5fb98f57e287f054af33366f', '25cee48f69116a7ace04749dd06d3d99', '5317b3729e3dab6ea788ca843dbedab5', 'f0c0d7151845da590ce491ec1ea3571d', '85b8e42bd9c8472f4d7c7c5ef492bbd8', 'ba286d02fd9701a446d68ba85d0755c0', 'dac70c6601dd2c31a9ec996c2d220498', '69ed13f3ddc662d6ecd8261512117e85', '99674d69f913c30f56d215a3134cec0c', '3d64d66dd23d43365c280aba98a1dd3f', 'ac1d5194207dd02313890ee0f258a1b3', '8bbcca0c1b68fd01daec861eadaa7db5', '99953853cc4219fabe8327301058357c', 'd747c816e27f21abc7b64826b5739c3e', '1a4e3c5326a396f5aca2a9f712c60aca', '7420ab5069fb013b519ce473beef0e9e', '9465a25dee438f71fac2470d9d78b65a', '7765950fd44e7680e7dddef177b3851d', '252e58ed350b5b430a231ed3a2bbf00b', 'c5198d4e9c0145aee04dd53cc6590edd', '642e40fd8c4dcac56f20b3863e50d746', '5c12691e3216ec43a8633587cc42f774', '10fc569007188534060b52a7ac114ca4', '9d8ccaea6c94d8decb7ddbcf9402ec55', '64937e970cbba82d75b970c6947955b2', 'cffe6c89d479be933b51bafa2f774f63', 'c675a876b8c1898930c0e192aa38e976', 'fea2f801ab1dc87a87f8bdeb6fdb3394', 'ebd95bca61f4aaed185d5f5366630719', '53387d10456ae3aaba5da76813878f72', '5494e6adb603d145d4f93ee8afdfccc3', '8517c9e0e90e40fb5d51800668477228', 'e4b7fdc4aa351157b2903a7a7d0c6f34', '506627df3b12a4cb06382d9b59e58107', '153e5d85f7400a9bc4dfee1cc51401c8', '605f797c99ae00d2fd3784bd02901924', '386a18ccea2ea671eb1560bc6e11ae56', '2f12a2c52d1af80e091341c00f67227d', '35227f7b21a5023ed363b8237cbf4bef', '70f832881a0428b1e748f25ad1a47f39', '7bf7ca5658d8d6f979efc6de351a7e1f', '371d91da56a79f27f70a749cd4c0a3bd', '6d1a164af570b03f27b5f58534f7557e', 'f0cac173b0956fa63e312a1c0f3eae1f', '73395f1f6462f879f344d175ca87f7ba', 'cd9e1e62491cbcc8d9faf9713686f21c', 'b52e46d241e60aea20fe0d2f057f919b', 'e3b51103535d6392779f4e7b8fef3d83', '0d81a29a497b91e0f374ae0508de779d', 'de3fe1f01b52035350b18854c5decb9b', '64458d15a75902cd0425732b7b757705', '4beba9e1713f168fb77e234bc041be8c', 'ea307a9111d56ef7a8e1ff0f8ddec09c', 'fb4b27e8881a6eae5742eb8a5bda09a8', 'f2b0b7a4d0c9f55a405913668b7d45df', '8dfff70c92c374d5dbd02eff75345058', 'd9e78b550f018b9dd758fdc3a590fcc3', '3ad57dc22c27e016dd0e10d49ac1ff63', 'b1e6d044cbe657bb954c31c1033b8678', '5f80afc51a69c1cffa0c2ee7895b751c', 'c7de1694c846fe3b95895bc4ccb8df50', '83a3b10a446f936a77f07f78870b5eec', '6d3784eaed0929d9690604d541620d27', 'ee295405146c9238f7b4798d9e41905c', 'ef7be83f9f1fcab3adfa7a6a1f510427', '94128a0fd742bcea671993557d9f25bc', 'e868f40d517b8b6fded2b2022754d5de', '63e1f5157b082401652a1935d0ecb3e7', 'b262e9a8532b90fce8ecab5b32a0191f', '7e52885ebbc059130b0c01cce0bcf954', 'a15d500d1fd0497890707ab24eaec0f2', '90aa8604caa16d9d439a284312287727', 'b9cdfd5033c3a79a6a917257cfece72f', '0db5348a65ea7b11671a9b8e74c30ee1', 'b7822d554cfe3ed3118815a0339fe4c3', '5643ef38ab8462e2442ae244517e40ea', '92dd1033361ad94f941a4543e64791ff', '496b1b264b8f3cb922953cb6627702ab', '7407795460968de9aa7f60d890b29c39', '7566c264e4b41ad4e6758ab174590a20', 'eb5c0b6e4c2dad803b32fbe58e19f644']
    for userId in userIDs:
        people = client.people(userId)
        try:
            for follower in people.followings:
                try:
                    # t1 = threading.Thread(target=insertNeo4j, args=(follower, people.id))
                    # print("启动新线程t1")
                    # t1.start()
                    flag = grab_or_not(follower)
                    if flag is 1:
                        print("此用户已经抓过,跳过"+str(follower.id))
                        continue
                    insertNeo4j(follower, people.id)
                    print("first关系成功####"+str(follower.id))
                except Exception, e:
                    print(e)
                    failure = database.graph.begin()
                    failure.run("create(f:UserFailure{id:'"+str(follower.id)+"'})")
                    failure.commit()
                    continue
                for thirdFollow in follower.followings:
                    try:
                        second_flag = second_grab_or_not(thirdFollow)
                        if second_flag is 1:
                            print("此二度用户已抓过"+str(thirdFollow.id))
                            continue
                        insertNeo4j(thirdFollow, follower.id)
                        database.graph.data("match(u:User{userId:'" + thirdFollow.id + "'}) set u.answer_end=true")
                        print("second关系成功********************"+str(thirdFollow.id))
                    except Exception, e:
                        print(e)
                        failure = database.graph.begin()
                        failure.run("create(f:UserFailure{id:'"+str(thirdFollow.id)+"'})")
                        failure.commit()
                        continue
                database.graph.data("match(u:User{userId:'" + follower.id + "'}) set u.allgrab=true")
            database.graph.data("match(u:User{userId:'"+people.id+"'}) set u.grab=true")
        except Exception, e:
            print(e.message)
            continue
    print("it is over")


# 二度
def second_grab_or_not(thirdFollow):
    flag = database.graph.data("match(u:User{userId:'" + thirdFollow.id + "'}) where u.answer_end=true return count(u) as num ")
    if flag[0]["num"] >= 1:
        return 1
    else:
        return 2

# 一度
def grab_or_not(follower):
    flag = database.graph.data("match(u:User{userId:'" + follower.id + "'}) where u.allgrab=true return count(u) as num")
    if flag[0]["num"] >= 1:
        return 1
    else:
        return 2

def insertNeo4j(follower, userId):
    tx = database.graph.begin()
    author = userinfo(follower)
    cypher = "merge(u:User{userId: '"+author["author_id"]+"'}) on create set u.name='"+author["author_name"]+"',u.email='"+author["author_email"]+"',u.gender='"+author["author_gender"]+"'," \
                    "u.weibo='"+author["author_weibo"]+"', u.loation='"+author["author_location"]+"'," \
                    "u.business='"+author["author_business"]+"',u.education="+author["author_education"]+"," \
                    "u.employment="+author["author_employment"]+" with u match(au:User{userId :'"+str(userId)+"'}) merge(au)-[:FOLLOWING]->(u)"
    tx.run(cypher)
    print("用户关系对应成功"+str(userId)+"->"+str(author["author_id"]))
    tx.commit()

    # 回答相关
    follower_answers = follower.answers
    i = 0
    # 抓取10个回答
    for answer in follower_answers:
        # if answer.voteup_count == 0 and answer.comment_count == 0:
        #     print("此答案效率不高啊")
        #     continue
        # tx1 = database.graph.begin()
        myanswer = user_answer(answer)
        relationShip = "match(u:User{userId: '"+author["author_id"]+"'}) MERGE (u)-[:AUTHOR]->(a:Answer{answerId:'"+myanswer["answer_id"]+"'}) on create set a.excerpt="+myanswer["excerpt"]+"," \
                            "a.thanks_count="+myanswer["thanks_count"]+",a.voteup_count="+myanswer["voteup_count"]+"," \
                            "a.comment_count="+myanswer["comment_count"]+",a.question="+myanswer["title"]+""
        database.graph.data(relationShip)
        # tx1.run(relationShip)
        # tx1.commit()
        i += 1
        print("本次已经抓取了"+str(i)+"条回答")
    print("用户回答对应完毕"+str(author["author_id"])+"->"+"回答")


def userinfo(author):
    peopleInfo = {}
    peopleInfo["author_name"] = author.name
    peopleInfo["author_weibo"] = author.sina_weibo_url if author.sina_weibo_url else ''
    peopleInfo["author_email"] = author.email if author.email else ''
    temp_location = ''
    if author.locations:
        for location in author.locations:
            temp_location += location.name
    peopleInfo["author_location"] = temp_location
    # peopleInfo["author_gender"] = "male" if author.gender == 1 else "female" if author.gender == 2 else "未填"
    if author.gender == 1:
        peopleInfo["author_gender"] = "male"
    elif author.gender == 0:
        peopleInfo["author_gender"] = "female"
    else:
        peopleInfo["author_gender"] = "未填"

    peopleInfo["author_business"] = author.business.name if author.business else ""

    temp_education = ''
    if author.educations:
        for education in author.educations:
            if 'school' in education:
                temp_education += education.school.name
            if 'major' in education:
                temp_education += education.major.name
    peopleInfo["author_education"] = json.dumps(temp_education)

    temp_employment = ''
    if author.employments:
        for employment in author.employments:
            if 'company' in employment:
                temp_employment += employment.company.name
            if 'job' in employment:
                temp_employment += employment.job.name
    peopleInfo["author_employment"] = json.dumps(temp_employment)
    peopleInfo["author_id"] = str(author.id)
    return peopleInfo

def user_answer(answer):
    answerInfo = {}
    answerInfo["thanks_count"] = str(answer.thanks_count)
    answerInfo["voteup_count"] = str(answer.voteup_count)
    answerInfo["comment_count"] = str(answer.comment_count)
    answerInfo["excerpt"] = json.dumps(answer.excerpt)
    answerInfo["answer_id"] = str(answer.id)
    answerInfo["title"] = json.dumps(answer.question.title)
    return answerInfo


# def answr_topic(topics):
#     topicList = []
#     for  mytopic in topics:
#         topicInfo = {}
#         topicInfo["id"] = mytopic.id
#         topicInfo["name"] = mytopic.name
#         topicList.append(topicInfo)
#     return topicList


def main():
    user_bestanswers()


if __name__ == '__main__':
    main()
