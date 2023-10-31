class MagneticReadoutProcessing < Formula
  include Language::Python::Virtualenv

  desc "Shiny new formula"
  homepage "https://github.com/LFB-MRI/MagnetCharacterization/"
  url "https://files.pythonhosted.org/packages/01/0d/469d92fe02a796a43c6c1678358b169a2212932c462b8129a80d565a0740/MagneticReadoutProcessing-0.0.3.tar.gz"
  sha256 "aed4a494903458d6271e822354c39e71fe6baa34ca3ee8f5bec1e2c1c8f06d7a"

  depends_on "python3"

  resource "asttokens" do
    url "https://files.pythonhosted.org/packages/45/1d/f03bcb60c4a3212e15f99a56085d93093a497718adf828d050b9d675da81/asttokens-2.4.1.tar.gz"
    sha256 "b03869718ba9a6eb027e134bfdf69f38a236d681c83c160d510768af11254ba0"
  end

  resource "bleach" do
    url "https://files.pythonhosted.org/packages/6d/10/77f32b088738f40d4f5be801daa5f327879eadd4562f36a2b5ab975ae571/bleach-6.1.0.tar.gz"
    sha256 "0a31f1837963c41d46bbf1331b8778e1308ea0791db03cc4e7357b97cf42a8fe"
  end

  resource "blinker" do
    url "https://files.pythonhosted.org/packages/ea/96/ed1420a974540da7419094f2553bc198c454cee5f72576e7c7629dd12d6e/blinker-1.6.3.tar.gz"
    sha256 "152090d27c1c5c722ee7e48504b02d76502811ce02e1523553b4cf8c8b3d3a8d"
  end

  resource "click" do
    url "https://files.pythonhosted.org/packages/96/d3/f04c7bfcf5c1862a2a5b845c6b2b360488cf47af55dfa79c98f6a6bf98b5/click-8.1.7.tar.gz"
    sha256 "ca9853ad459e787e2192211578cc907e7594e294c7ccc834310722b41b9ca6de"
  end

  resource "cobs" do
    url "https://files.pythonhosted.org/packages/87/dd/cb6aa7465da843cc1633e2ee05ef86a8df63fd95e741dfcb98ed8f477cb8/cobs-1.2.1.tar.gz"
    sha256 "2af7f8791cde1ae7c6b936f5d0c35fe29feb10de25f79c15b0af0d6729783cc0"
  end

  resource "configparser" do
    url "https://files.pythonhosted.org/packages/0b/65/bad3eb64f30657ee9fa2e00e80b3ad42037db5eb534fadd15a94a11fe979/configparser-6.0.0.tar.gz"
    sha256 "ec914ab1e56c672de1f5c3483964e68f71b34e457904b7b76e06b922aec067a8"
  end

  resource "contourpy" do
    url "https://files.pythonhosted.org/packages/b1/7d/087ee4295e7580d3f7eb8a8a4e0ec8c7847e60f34135248ccf831cf5bbfc/contourpy-1.1.1.tar.gz"
    sha256 "96ba37c2e24b7212a77da85004c38e7c4d155d3e72a45eeaf22c1f03f607e8ab"
  end

  resource "cycler" do
    url "https://files.pythonhosted.org/packages/a9/95/a3dbbb5028f35eafb79008e7522a75244477d2838f38cbb722248dabc2a8/cycler-0.12.1.tar.gz"
    sha256 "88bb128f02ba341da8ef447245a9e138fae777f6a23943da4540077d3601eb1c"
  end

  resource "decorator" do
    url "https://files.pythonhosted.org/packages/66/0c/8d907af351aa16b42caae42f9d6aa37b900c67308052d10fdce809f8d952/decorator-5.1.1.tar.gz"
    sha256 "637996211036b6385ef91435e4fae22989472f9d571faba8927ba8253acbc330"
  end

  resource "executing" do
    url "https://files.pythonhosted.org/packages/08/41/85d2d28466fca93737592b7f3cc456d1cfd6bcd401beceeba17e8e792b50/executing-2.0.1.tar.gz"
    sha256 "35afe2ce3affba8ee97f2d69927fa823b08b472b7b994e36a52a964b93d16147"
  end

  resource "Flask" do
    url "https://files.pythonhosted.org/packages/d8/09/c1a7354d3925a3c6c8cfdebf4245bae67d633ffda1ba415add06ffc839c5/flask-3.0.0.tar.gz"
    sha256 "cfadcdb638b609361d29ec22360d6070a77d7463dcb3ab08d2c2f2f168845f58"
  end

  resource "Flask-Cors" do
    url "https://files.pythonhosted.org/packages/c8/b0/bd7130837a921497520f62023c7ba754e441dcedf959a43e6d1fd86e5451/Flask-Cors-4.0.0.tar.gz"
    sha256 "f268522fcb2f73e2ecdde1ef45e2fd5c71cc48fe03cffb4b441c6d1b40684eb0"
  end

  resource "fonttools" do
    url "https://files.pythonhosted.org/packages/43/bc/6051ee22b88c5d9d39ea68e8e2422d3036d9b52ac2afc559f7397d59bc64/fonttools-4.43.1.tar.gz"
    sha256 "17dbc2eeafb38d5d0e865dcce16e313c58265a6d2d20081c435f84dc5a9d8212"
  end

  resource "iniconfig" do
    url "https://files.pythonhosted.org/packages/d7/4b/cbd8e699e64a6f16ca3a8220661b5f83792b3017d0f79807cb8708d33913/iniconfig-2.0.0.tar.gz"
    sha256 "2d91e135bf72d31a410b17c16da610a82cb55f6b0477d1a902134b24a455b8b3"
  end

  resource "ipython" do
    url "https://files.pythonhosted.org/packages/23/e5/5cc4f78c0a4e050859e69ead6e33ebdb3509166f50c2a2f3ea49b28195ac/ipython-8.17.1.tar.gz"
    sha256 "9e12020f4bf74f08631c0f033bb580e074fbe36c64903195f3e63b9c0a986cbe"
  end

  resource "itsdangerous" do
    url "https://files.pythonhosted.org/packages/7f/a1/d3fb83e7a61fa0c0d3d08ad0a94ddbeff3731c05212617dff3a94e097f08/itsdangerous-2.1.2.tar.gz"
    sha256 "5dbbc68b317e5e42f327f9021763545dc3fc3bfe22e6deb96aaf1fc38874156a"
  end

  resource "jedi" do
    url "https://files.pythonhosted.org/packages/d6/99/99b493cec4bf43176b678de30f81ed003fd6a647a301b9c927280c600f0a/jedi-0.19.1.tar.gz"
    sha256 "cf0496f3651bc65d7174ac1b7d043eff454892c708a87d1b683e57b569927ffd"
  end

  resource "Jinja2" do
    url "https://files.pythonhosted.org/packages/7a/ff/75c28576a1d900e87eb6335b063fab47a8ef3c8b4d88524c4bf78f670cce/Jinja2-3.1.2.tar.gz"
    sha256 "31351a702a408a9e7595a8fc6150fc3f43bb6bf7e319770cbc0db9df9437e852"
  end

  resource "jsonpickle" do
    url "https://files.pythonhosted.org/packages/6e/92/62fdc2f6b468b870dd171ad21748ef0ec2bff1b258c25ce6db3545cccc90/jsonpickle-3.0.2.tar.gz"
    sha256 "e37abba4bfb3ca4a4647d28bb9f4706436f7b46c8a8333b4a718abafa8e46b37"
  end

  resource "kiwisolver" do
    url "https://files.pythonhosted.org/packages/b9/2d/226779e405724344fc678fcc025b812587617ea1a48b9442628b688e85ea/kiwisolver-1.4.5.tar.gz"
    sha256 "e57e563a57fb22a142da34f38acc2fc1a5c864bc29ca1517a88abc963e60d6ec"
  end

  resource "lz4" do
    url "https://files.pythonhosted.org/packages/9f/54/32b2d68d25b80ae4037cd1c68b8a6a28c6753cba3632cbf6d64bebd2b200/lz4-4.3.2.tar.gz"
    sha256 "e1431d84a9cfb23e6773e72078ce8e65cad6745816d4cbf9ae67da5ea419acda"
  end

  resource "magpy" do
    url "https://files.pythonhosted.org/packages/02/b4/a7633d52b519684c0deb2eeec51b790c3ef8536db3d27aada17536b1a01e/magpy-1.0.0.tar.gz"
    sha256 "940a507655dd0d9729a76b5ec933ffd69171b83d6e87e6b519851f45552e5ee7"
  end

  resource "magpylib" do
    url "https://files.pythonhosted.org/packages/d3/72/6e3605da706bf12e7f79d76e37351bce119bf278de13e36208b05a0999d0/magpylib-4.4.0.tar.gz"
    sha256 "1b0834f74ba381042dd4cf459e070cf466305bd14c5fa8bf01986d0e7a45ad48"
  end

  resource "MarkupSafe" do
    url "https://files.pythonhosted.org/packages/6d/7c/59a3248f411813f8ccba92a55feaac4bf360d29e2ff05ee7d8e1ef2d7dbf/MarkupSafe-2.1.3.tar.gz"
    sha256 "af598ed32d6ae86f1b747b82783958b1a4ab8f617b06fe68795c7f026abbdcad"
  end

  resource "matplotlib" do
    url "https://files.pythonhosted.org/packages/23/e1/77016194621fb1356aafeb2186f07b5dede62ea2043bf03f82325c4fccc5/matplotlib-3.8.0.tar.gz"
    sha256 "df8505e1c19d5c2c26aff3497a7cbd3ccfc2e97043d1e4db3e76afa399164b69"
  end

  resource "matplotlib-inline" do
    url "https://files.pythonhosted.org/packages/d9/50/3af8c0362f26108e54d58c7f38784a3bdae6b9a450bab48ee8482d737f44/matplotlib-inline-0.1.6.tar.gz"
    sha256 "f887e5f10ba98e8d2b150ddcf4702c1e5f8b3a20005eb0f74bfdbd360ee6f304"
  end

  resource "networkx" do
    url "https://files.pythonhosted.org/packages/c4/80/a84676339aaae2f1cfdf9f418701dd634aef9cc76f708ef55c36ff39c3ca/networkx-3.2.1.tar.gz"
    sha256 "9f1bb5cf3409bf324e0a722c20bdb4c20ee39bf1c30ce8ae499c8502b0b5e0c6"
  end

  resource "numpy" do
    url "https://files.pythonhosted.org/packages/78/23/f78fd8311e0f710fe1d065d50b92ce0057fe877b8ed7fd41b28ad6865bfc/numpy-1.26.1.tar.gz"
    sha256 "c8c6c72d4a9f831f328efb1312642a1cafafaa88981d9ab76368d50d07d93cbe"
  end

  resource "openpyscad" do
    url "https://files.pythonhosted.org/packages/96/4c/536b7bacb6df08943d2da6fe4fcb6ccb1e7c7a196eb15d3c40b8cd4624c3/openpyscad-0.5.0.tar.gz"
    sha256 "2e1ea8eb10fe9e9c31c8bc5941c1ef6294e3400e4ae4b23133ce2275124d1c9b"
  end

  resource "packaging" do
    url "https://files.pythonhosted.org/packages/fb/2b/9b9c33ffed44ee921d0967086d653047286054117d584f1b1a7c22ceaf7b/packaging-23.2.tar.gz"
    sha256 "048fb0e9405036518eaaf48a55953c750c11e1a1b68e0dd1a9d62ed0c092cfc5"
  end

  resource "parso" do
    url "https://files.pythonhosted.org/packages/a2/0e/41f0cca4b85a6ea74d66d2226a7cda8e41206a624f5b330b958ef48e2e52/parso-0.8.3.tar.gz"
    sha256 "8c07be290bb59f03588915921e29e8a50002acaf2cdc5fa0e0114f91709fafa0"
  end

  resource "pexpect" do
    url "https://files.pythonhosted.org/packages/e5/9b/ff402e0e930e70467a7178abb7c128709a30dfb22d8777c043e501bc1b10/pexpect-4.8.0.tar.gz"
    sha256 "fc65a43959d153d0114afe13997d439c22823a27cefceb5ff35c2178c6784c0c"
  end

  resource "Pillow" do
    url "https://files.pythonhosted.org/packages/80/d7/c4b258c9098b469c4a4e77b0a99b5f4fd21e359c2e486c977d231f52fc71/Pillow-10.1.0.tar.gz"
    sha256 "e6bf8de6c36ed96c86ea3b6e1d5273c53f46ef518a062464cd7ef5dd2cf92e38"
  end

  resource "plotly" do
    url "https://files.pythonhosted.org/packages/0d/17/ba496e60f95020227a15f73965a64ea3f176cae7faed2d9302a14524b681/plotly-5.18.0.tar.gz"
    sha256 "360a31e6fbb49d12b007036eb6929521343d6bee2236f8459915821baefa2cbb"
  end

  resource "pluggy" do
    url "https://files.pythonhosted.org/packages/36/51/04defc761583568cae5fd533abda3d40164cbdcf22dee5b7126ffef68a40/pluggy-1.3.0.tar.gz"
    sha256 "cf61ae8f126ac6f7c451172cf30e3e43d3ca77615509771b3a984a0730651e12"
  end

  resource "prompt-toolkit" do
    url "https://files.pythonhosted.org/packages/9a/02/76cadde6135986dc1e82e2928f35ebeb5a1af805e2527fe466285593a2ba/prompt_toolkit-3.0.39.tar.gz"
    sha256 "04505ade687dc26dc4284b1ad19a83be2f2afe83e7a828ace0c72f3a1df72aac"
  end

  resource "ptyprocess" do
    url "https://files.pythonhosted.org/packages/20/e5/16ff212c1e452235a90aeb09066144d0c5a6a8c0834397e03f5224495c4e/ptyprocess-0.7.0.tar.gz"
    sha256 "5c5d0a3b48ceee0b48485e0c26037c0acd7d29765ca3fbb5cb3831d347423220"
  end

  resource "pure-eval" do
    url "https://files.pythonhosted.org/packages/97/5a/0bc937c25d3ce4e0a74335222aee05455d6afa2888032185f8ab50cdf6fd/pure_eval-0.2.2.tar.gz"
    sha256 "2b45320af6dfaa1750f543d714b6d1c520a1688dec6fd24d339063ce0aaa9ac3"
  end

  resource "Pygments" do
    url "https://files.pythonhosted.org/packages/d6/f7/4d461ddf9c2bcd6a4d7b2b139267ca32a69439387cc1f02a924ff8883825/Pygments-2.16.1.tar.gz"
    sha256 "1daff0494820c69bc8941e407aa20f577374ee88364ee10a98fdbe0aece96e29"
  end

  resource "pyparsing" do
    url "https://files.pythonhosted.org/packages/37/fe/65c989f70bd630b589adfbbcd6ed238af22319e90f059946c26b4835e44b/pyparsing-3.1.1.tar.gz"
    sha256 "ede28a1a32462f5a9705e07aea48001a08f7cf81a021585011deba701581a0db"
  end

  resource "pyserial" do
    url "https://files.pythonhosted.org/packages/1e/7d/ae3f0a63f41e4d2f6cb66a5b57197850f919f59e558159a4dd3a818f5082/pyserial-3.5.tar.gz"
    sha256 "3c77e014170dfffbd816e6ffc205e9842efb10be9f58ec16d3e8675b4925cddb"
  end

  resource "pytest" do
    url "https://files.pythonhosted.org/packages/38/d4/174f020da50c5afe9f5963ad0fc5b56a4287e3586e3de5b3c8bce9c547b4/pytest-7.4.3.tar.gz"
    sha256 "d989d136982de4e3b29dabcc838ad581c64e8ed52c11fbe86ddebd9da0818cd5"
  end

  resource "python-dateutil" do
    url "https://files.pythonhosted.org/packages/4c/c4/13b4776ea2d76c115c1d1b84579f3764ee6d57204f6be27119f13a61d0a9/python-dateutil-2.8.2.tar.gz"
    sha256 "0123cacc1627ae19ddf3c27a5de5bd67ee4586fbdd6440d9748f8abb483d3e86"
  end

  resource "python-dotenv" do
    url "https://files.pythonhosted.org/packages/31/06/1ef763af20d0572c032fa22882cfbfb005fba6e7300715a37840858c919e/python-dotenv-1.0.0.tar.gz"
    sha256 "a8df96034aae6d2d50a4ebe8216326c61c3eb64836776504fcca410e5937a3ba"
  end

  resource "pyvis" do
    url ""
    sha256 ""
  end

  resource "PyYAML" do
    url "https://files.pythonhosted.org/packages/cd/e5/af35f7ea75cf72f2cd079c95ee16797de7cd71f29ea7c68ae5ce7be1eda0/PyYAML-6.0.1.tar.gz"
    sha256 "bfdf460b1736c775f2ba9f6a92bca30bc2095067b8a9d77876d1fad6cc3b4a43"
  end

  resource "scipy" do
    url "https://files.pythonhosted.org/packages/39/7b/9f265b7f074195392e893a5cdc66116c2f7a31fd5f3d9cceff661ec6df82/scipy-1.11.3.tar.gz"
    sha256 "bba4d955f54edd61899776bad459bf7326e14b9fa1c552181f0479cc60a568cd"
  end

  resource "six" do
    url "https://files.pythonhosted.org/packages/71/39/171f1c67cd00715f190ba0b100d606d440a28c93c7714febeca8b79af85e/six-1.16.0.tar.gz"
    sha256 "1e61c37477a1626458e36f7b1d82aa5c9b094fa4802892072e49de9c60c4c926"
  end

  resource "solid" do
    url "https://files.pythonhosted.org/packages/34/af/b9645f5120d93452ad356f23f9d209063c7fcfe780e3cc4c3ac36e707d35/solid-0.2.0.tar.gz"
    sha256 "93eaf438c38175f429bdadaf0122fc06fd71e39f76fb96261215c2b824db560e"
  end

  resource "stack-data" do
    url "https://files.pythonhosted.org/packages/28/e3/55dcc2cfbc3ca9c29519eb6884dd1415ecb53b0e934862d3559ddcb7e20b/stack_data-0.6.3.tar.gz"
    sha256 "836a778de4fec4dcd1dcd89ed8abff8a221f58308462e1c4aa2a3cf30148f0b9"
  end

  resource "tenacity" do
    url "https://files.pythonhosted.org/packages/89/3c/253e1627262373784bf9355db9d6f20d2d8831d79f91e9cca48050cddcc2/tenacity-8.2.3.tar.gz"
    sha256 "5398ef0d78e63f40007c1fb4c0bff96e1911394d2fa8d194f77619c05ff6cc8a"
  end

  resource "tinydb" do
    url "https://files.pythonhosted.org/packages/30/0b/9e75a8d3333a6a3d9b36de04bf87a37a8d7f100035ea23c9c37bf0a112ab/tinydb-4.8.0.tar.gz"
    sha256 "6dd686a9c5a75dfa9280088fd79a419aefe19cd7f4bd85eba203540ef856d564"
  end

  resource "tqdm" do
    url "https://files.pythonhosted.org/packages/62/06/d5604a70d160f6a6ca5fd2ba25597c24abd5c5ca5f437263d177ac242308/tqdm-4.66.1.tar.gz"
    sha256 "d88e651f9db8d8551a62556d3cff9e3034274ca5d66e93197cf2490e2dcb69c7"
  end

  resource "traitlets" do
    url "https://files.pythonhosted.org/packages/5a/0b/b825ac58e20a6fef55c94ba9c7c96f1777f9a3b7e34b3b43b6d54185ec2a/traitlets-5.13.0.tar.gz"
    sha256 "9b232b9430c8f57288c1024b34a8f0251ddcc47268927367a0dd3eeaca40deb5"
  end

  resource "typer" do
    url "https://files.pythonhosted.org/packages/5b/49/39f10d0f75886439ab3dac889f14f8ad511982a754e382c9b6ca895b29e9/typer-0.9.0.tar.gz"
    sha256 "50922fd79aea2f4751a8e0408ff10d2662bd0c8bbfa84755a699f3bada2978b2"
  end

  resource "typing-extensions" do
    url "https://files.pythonhosted.org/packages/1f/7a/8b94bb016069caa12fc9f587b28080ac33b4fbb8ca369b98bc0a4828543e/typing_extensions-4.8.0.tar.gz"
    sha256 "df8e4339e9cb77357558cbdbceca33c303714cf861d1eef15e1070055ae8b7ef"
  end

  resource "vector" do
    url "https://files.pythonhosted.org/packages/4d/98/4ed3626e6dff3f498dbf93dc9a92e8a6af93f86328913d24db1822d25412/vector-1.1.1.post1.tar.gz"
    sha256 "7a55ae549816e5fca0e52fab8cc66d4b0e4bb3b7753933e85b4167657940372b"
  end

  resource "vg" do
    url "https://files.pythonhosted.org/packages/c2/67/4dc05dee8167cff85fac313db7673dcfaa8acadfca815e90041e94928c6f/vg-2.0.0.tar.gz"
    sha256 "2a3f14951c81852c76727460abb8f977bf6e15bb07480e3f3bb01da1cd362570"
  end

  resource "waitress" do
    url "https://files.pythonhosted.org/packages/72/83/c3de9799e2305898b02ea67bcd125ad06f271e2a82cc86fe66b7bf4e6f63/waitress-2.1.2.tar.gz"
    sha256 "780a4082c5fbc0fde6a2fcfe5e26e6efc1e8f425730863c04085769781f51eba"
  end

  resource "wcwidth" do
    url "https://files.pythonhosted.org/packages/a6/ad/428bc4ff924e66365c96994873e09a17bb5e8a1228be6e8d185bc2a11de9/wcwidth-0.2.9.tar.gz"
    sha256 "a675d1a4a2d24ef67096a04b85b02deeecd8e226f57b5e3a72dbb9ed99d27da8"
  end

  resource "webencodings" do
    url "https://files.pythonhosted.org/packages/0b/02/ae6ceac1baeda530866a85075641cec12989bd8d31af6d5ab4a3e8c92f47/webencodings-0.5.1.tar.gz"
    sha256 "b36a1c245f2d304965eb4e0a82848379241dc04b865afcc4aab16748587e1923"
  end

  resource "Werkzeug" do
    url "https://files.pythonhosted.org/packages/0d/cc/ff1904eb5eb4b455e442834dabf9427331ac0fa02853bf83db817a7dd53d/werkzeug-3.0.1.tar.gz"
    sha256 "507e811ecea72b18a404947aded4b3390e1db8f826b494d76550ef45bb3b1dcc"
  end

  def install
    virtualenv_create(libexec, "python3")
    virtualenv_install_with_resources
  end

  test do
    false
  end
end
