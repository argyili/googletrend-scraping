// 地方情報
var region = [
    ["01","北海道地方"],
    ["02","東北地方"],
    ["03","関東地方"],
    ["04","甲信地方"],
    ["05","東海地方"],
    ["06","北陸地方"],
    ["07","近畿地方"],
    ["08","中国地方"],
    ["09","四国地方"],
    ["10","九州地方"],
    ["11","沖縄地方"]
];

// 都道府県情報
var prefecture = {
    "01":[
        ["11","宗谷"],
        ["12","上川"],
        ["13","留萌"],
        ["14","石狩"],
        ["15","空知"],
        ["16","後志"],
        ["17","ｵﾎｰﾂｸ"],
        ["18","根室"],
        ["19","釧路"],
        ["20","十勝"],
        ["21","胆振"],
        ["22","日高"],
        ["23","渡島"],
        ["24","檜山"]
    ],
    "02":[
        ["31","青森"],
        ["32","秋田"],
        ["33","岩手"],
        ["34","宮城"],
        ["35","山形"],
        ["36","福島"]
    ],
    "03":[
        ["40","茨城"],
        ["41","栃木"],
        ["42","群馬"],
        ["43","埼玉"],
        ["44","東京"],
        ["45","千葉"],
        ["46","神奈川"]
    ],
    "04":[
        ["48","長野"],
        ["49","山梨"]
    ],
    "05":[
        ["50","静岡"],
        ["51","愛知"],
        ["52","岐阜"],
        ["53","三重"]
    ],
    "06":[
        ["54","新潟"],
        ["55","富山"],
        ["56","石川"],
        ["57","福井"]
    ],
    "07":[
        ["60","滋賀"],
        ["61","京都"],
        ["62","大阪"],
        ["63","兵庫"],
        ["64","奈良"],
        ["65","和歌山"]
    ],
    "08":[
        ["66","岡山"],
        ["67","広島"],
        ["68","島根"],
        ["69","鳥取"],
        ["81","山口"]
    ],
    "09":[
        ["71","徳島"],
        ["72","香川"],
        ["73","愛媛"],
        ["74","高知"]
    ],
    "10":[
        ["82","福岡"],
        ["83","大分"],
        ["84","長崎"],
        ["85","佐賀"],
        ["86","熊本"],
        ["87","宮崎"],
        ["88","鹿児島"]
    ],
    "11":[
        ["9194","沖縄"]
    ]
};

// 地点情報
var point = {
    "11":[
        ["11001","宗谷岬"],
        ["11016","稚内"],
        ["11046","礼文"],
        ["11076","浜鬼志別"],
        ["11121","沼川"],
        ["11151","沓形"],
        ["11176","豊富"],
        ["11206","浜頓別"],
        ["11276","中頓別"],
        ["11291","北見枝幸"],
        ["11316","歌登"]
    ],
    "12":[
        ["12011","中川"],
        ["12041","音威子府"],
        ["12141","美深"],
        ["12181","名寄"],
        ["12231","下川"],
        ["12261","士別"],
        ["12266","朝日"],
        ["12301","和寒"],
        ["12386","江丹別"],
        ["12396","比布"],
        ["12411","上川"],
        ["12442","旭川"],
        ["12451","東川"],
        ["12512","志比内"],
        ["12551","美瑛"],
        ["12596","上富良野"],
        ["12626","富良野"],
        ["12632","麓郷"],
        ["12691","幾寅"],
        ["12746","占冠"],
        ["15041","朱鞠内"],
        ["15076","幌加内"]
    ],
    "13":[
        ["13061","天塩"],
        ["13086","遠別"],
        ["13121","初山別"],
        ["13146","焼尻"],
        ["13181","羽幌"],
        ["13261","達布"],
        ["13277","留萌"],
        ["13311","増毛"],
        ["13321","幌糠"]
    ],
    "14":[
        ["14026","浜益"],
        ["14071","厚田"],
        ["14101","新篠津"],
        ["14116","山口"],
        ["14121","石狩"],
        ["14136","江別"],
        ["14163","札幌"],
        ["14206","恵庭島松"],
        ["14286","支笏湖畔"]
    ],
    "15":[
        ["15116","石狩沼田"],
        ["15161","深川"],
        ["15231","空知吉野"],
        ["15241","滝川"],
        ["15251","芦別"],
        ["15311","月形"],
        ["15321","美唄"],
        ["15356","岩見沢"],
        ["15431","長沼"],
        ["15442","夕張"]
    ],
    "16":[
        ["16026","美国"],
        ["16061","神恵内"],
        ["16076","余市"],
        ["16091","小樽"],
        ["16156","共和"],
        ["16206","蘭越"],
        ["16217","倶知安"],
        ["16252","寿都"],
        ["16281","真狩"],
        ["16286","喜茂別"],
        ["16321","黒松内"]
    ],
    "17":[
        ["17036","雄武"],
        ["17076","興部"],
        ["17091","西興部"],
        ["17112","紋別"],
        ["17166","湧別"],
        ["17196","滝上"],
        ["17246","常呂"],
        ["17306","遠軽"],
        ["17316","佐呂間"],
        ["17341","網走"],
        ["17351","宇登呂"],
        ["17482","白滝"],
        ["17501","生田原"],
        ["17521","北見"],
        ["17546","小清水"],
        ["17561","斜里"],
        ["17596","留辺蘂"],
        ["17607","境野"],
        ["17631","美幌"],
        ["17717","津別"]
    ],
    "18":[
        ["18038","羅臼"],
        ["18136","標津"],
        ["18161","上標津"],
        ["18171","中標津"],
        ["18256","別海"],
        ["18273","根室"],
        ["18281","納沙布"],
        ["18311","厚床"]
    ],
    "19":[
        ["19021","川湯"],
        ["19051","弟子屈"],
        ["19076","阿寒湖畔"],
        ["19151","標茶"],
        ["19191","鶴居"],
        ["19261","中徹別"],
        ["19311","榊町"],
        ["19376","太田"],
        ["19416","白糠"],
        ["19432","釧路"],
        ["19451","知方学"]
    ],
    "20":[
        ["20146","陸別"],
        ["20186","ぬかびら源泉郷"],
        ["20266","上士幌"],
        ["20276","足寄"],
        ["20341","本別"],
        ["20356","新得"],
        ["20361","鹿追"],
        ["20371","駒場"],
        ["20421","芽室"],
        ["20432","帯広"],
        ["20441","池田"],
        ["20506","浦幌"],
        ["20556","糠内"],
        ["20601","上札内"],
        ["20606","更別"],
        ["20631","大津"],
        ["20696","大樹"],
        ["20751","広尾"]
    ],
    "21":[
        ["21111","厚真"],
        ["21126","穂別"],
        ["21161","大滝"],
        ["21171","森野"],
        ["21187","苫小牧"],
        ["21226","大岸"],
        ["21261","白老"],
        ["21276","鵡川"],
        ["21297","伊達"],
        ["21312","登別"],
        ["21323","室蘭"]
    ],
    "22":[
        ["22036","日高"],
        ["22141","日高門別"],
        ["22156","新和"],
        ["22241","静内"],
        ["22291","三石"],
        ["22306","中杵臼"],
        ["22327","浦河"],
        ["22391","えりも岬"]
    ],
    "23":[
        ["23031","長万部"],
        ["23086","八雲"],
        ["23166","森"],
        ["23206","川汲"],
        ["23226","北斗"],
        ["23232","函館"],
        ["23326","木古内"],
        ["23376","松前"],
        ["24141","熊石"]
    ],
    "24":[
        ["24041","せたな"],
        ["24051","今金"],
        ["24101","奥尻"],
        ["24201","鶉"],
        ["24217","江差"]
    ],
    "31":[
        ["31001","大間"],
        ["31111","むつ"],
        ["31121","小田野沢"],
        ["31136","今別"],
        ["31156","脇野沢"],
        ["31186","市浦"],
        ["31201","蟹田"],
        ["31296","五所川原"],
        ["31312","青森"],
        ["31332","野辺地"],
        ["31336","六ケ所"],
        ["31366","鰺ケ沢"],
        ["31436","深浦"],
        ["31461","弘前"],
        ["31466","黒石"],
        ["31482","酸ケ湯"],
        ["31506","三沢"],
        ["31586","十和田"],
        ["31602","八戸"],
        ["31646","碇ケ関"],
        ["31662","休屋"],
        ["31721","三戸"]
    ],
    "32":[
        ["32056","八森"],
        ["32111","能代"],
        ["32126","鷹巣"],
        ["32136","大館"],
        ["32146","鹿角"],
        ["32206","湯瀬"],
        ["32266","八幡平"],
        ["32286","男鹿"],
        ["32287","大潟"],
        ["32296","五城目"],
        ["32311","阿仁合"],
        ["32402","秋田"],
        ["32407","岩見三内"],
        ["32466","角館"],
        ["32476","田沢湖"],
        ["32496","大正寺"],
        ["32551","大曲"],
        ["32571","本荘"],
        ["32581","東由利"],
        ["32596","横手"],
        ["32616","にかほ"],
        ["32626","矢島"],
        ["32691","湯沢"],
        ["32771","湯の岱"]
    ],
    "33":[
        ["33006","種市"],
        ["33026","軽米"],
        ["33071","二戸"],
        ["33136","山形"],
        ["33146","久慈"],
        ["33166","荒屋"],
        ["33176","奥中山"],
        ["33186","葛巻"],
        ["33206","普代"],
        ["33226","岩手松尾"],
        ["33296","好摩"],
        ["33326","岩泉"],
        ["33336","小本"],
        ["33371","薮川"],
        ["33421","雫石"],
        ["33431","盛岡"],
        ["33441","区界"],
        ["33472","宮古"],
        ["33486","沢内"],
        ["33501","紫波"],
        ["33526","川井"],
        ["33581","大迫"],
        ["33616","山田"],
        ["33631","湯田"],
        ["33671","遠野"],
        ["33716","北上"],
        ["33751","釜石"],
        ["33776","若柳"],
        ["33781","江刺"],
        ["33801","住田"],
        ["33877","大船渡"],
        ["33911","一関"],
        ["33921","千厩"]
    ],
    "34":[
        ["34012","駒ノ湯"],
        ["34026","気仙沼"],
        ["34096","川渡"],
        ["34111","築館"],
        ["34171","米山"],
        ["34186","志津川"],
        ["34216","古川"],
        ["34266","大衡"],
        ["34276","鹿島台"],
        ["34292","石巻"],
        ["34296","女川"],
        ["34311","新川"],
        ["34331","塩釜"],
        ["34361","江ノ島"],
        ["34392","仙台"],
        ["34461","白石"],
        ["34462","蔵王"],
        ["34471","亘理"],
        ["34506","丸森"]
    ],
    "35":[
        ["35002","飛島"],
        ["35052","酒田"],
        ["35071","差首鍋"],
        ["35116","金山"],
        ["35141","鶴岡"],
        ["35146","狩川"],
        ["35162","新庄"],
        ["35176","向町"],
        ["35216","肘折"],
        ["35231","尾花沢"],
        ["35246","鼠ケ関"],
        ["35332","村山"],
        ["35361","大井沢"],
        ["35376","左沢"],
        ["35426","山形"],
        ["35456","長井"],
        ["35486","小国"],
        ["35511","高畠"],
        ["35541","高峰"],
        ["35552","米沢"]
    ],
    "36":[
        ["36056","茂庭"],
        ["36066","梁川"],
        ["36106","桧原"],
        ["36127","福島"],
        ["36151","相馬"],
        ["36176","喜多方"],
        ["36196","鷲倉"],
        ["36221","飯舘"],
        ["36251","西会津"],
        ["36276","猪苗代"],
        ["36291","二本松"],
        ["36342","金山"],
        ["36361","若松"],
        ["36391","船引"],
        ["36411","浪江"],
        ["36426","只見"],
        ["36476","郡山"],
        ["36501","川内"],
        ["36536","南郷"],
        ["36562","湯本"],
        ["36591","小野新町"],
        ["36611","広野"],
        ["36641","田島"],
        ["36667","白河"],
        ["36676","石川"],
        ["36716","桧枝岐"],
        ["36821","東白川"],
        ["36836","山田"],
        ["36846","小名浜"]
    ],
    "40":[
        ["40046","北茨城"],
        ["40061","大子"],
        ["40091","常陸大宮"],
        ["40136","日立"],
        ["40191","笠間"],
        ["40201","水戸"],
        ["40221","古河"],
        ["40231","下館"],
        ["40281","下妻"],
        ["40311","鉾田"],
        ["40336","つくば"],
        ["40341","土浦"],
        ["40406","鹿嶋"],
        ["40426","龍ケ崎"]
    ],
    "41":[
        ["41011","那須高原"],
        ["41076","五十里"],
        ["41091","黒磯"],
        ["41116","土呂部"],
        ["41141","大田原"],
        ["41166","奥日光"],
        ["41171","今市"],
        ["41181","塩谷"],
        ["41247","那須烏山"],
        ["41271","鹿沼"],
        ["41277","宇都宮"],
        ["41331","真岡"],
        ["41361","佐野"],
        ["41376","小山"]
    ],
    "42":[
        ["42046","藤原"],
        ["42091","みなかみ"],
        ["42121","草津"],
        ["42146","沼田"],
        ["42186","中之条"],
        ["42221","田代"],
        ["42251","前橋"],
        ["42266","桐生"],
        ["42286","上里見"],
        ["42302","伊勢崎"],
        ["42326","西野牧"],
        ["42366","館林"],
        ["42396","神流"]
    ],
    "43":[
        ["43051","寄居"],
        ["43056","熊谷"],
        ["43126","久喜"],
        ["43156","秩父"],
        ["43171","鳩山"],
        ["43241","さいたま"],
        ["43256","越谷"],
        ["43266","所沢"]
    ],
    "44":[
        ["44046","小河内"],
        ["44056","青梅"],
        ["44071","練馬"],
        ["44112","八王子"],
        ["44116","府中"],
        ["44132","東京"],
        ["44136","江戸川臨海"],
        ["44172","大島"],
        ["44226","三宅島"],
        ["44263","八丈島"],
        ["44301","父島"],
        ["44356","南鳥島"]
    ],
    "45":[
        ["45061","我孫子"],
        ["45081","香取"],
        ["45106","船橋"],
        ["45116","佐倉"],
        ["45147","銚子"],
        ["45181","横芝光"],
        ["45212","千葉"],
        ["45261","茂原"],
        ["45282","木更津"],
        ["45291","牛久"],
        ["45326","坂畑"],
        ["45361","鴨川"],
        ["45371","勝浦"],
        ["45401","館山"]
    ],
    "46":[
        ["46091","海老名"],
        ["46106","横浜"],
        ["46141","辻堂"],
        ["46166","小田原"],
        ["46211","三浦"]
    ],
    "48":[
        ["48031","野沢温泉"],
        ["48061","信濃町"],
        ["48066","飯山"],
        ["48141","白馬"],
        ["48156","長野"],
        ["48191","大町"],
        ["48196","信州新町"],
        ["48216","菅平"],
        ["48256","上田"],
        ["48296","穂高"],
        ["48321","東御"],
        ["48331","軽井沢"],
        ["48361","松本"],
        ["48381","立科"],
        ["48386","佐久"],
        ["48466","奈川"],
        ["48491","諏訪"],
        ["48531","開田高原"],
        ["48536","木祖薮原"],
        ["48546","辰野"],
        ["48561","原村"],
        ["48571","野辺山"],
        ["48606","木曽福島"],
        ["48621","伊那"],
        ["48717","南木曽"],
        ["48731","飯島"],
        ["48767","飯田"],
        ["48826","浪合"],
        ["48841","南信濃"]
    ],
    "49":[
        ["49036","大泉"],
        ["49086","韮崎"],
        ["49142","甲府"],
        ["49151","勝沼"],
        ["49161","大月"],
        ["49196","古関"],
        ["49236","切石"],
        ["49251","河口湖"],
        ["49256","山中"],
        ["49316","南部"]
    ],
    "50":[
        ["50106","井川"],
        ["50136","御殿場"],
        ["50196","富士"],
        ["50206","三島"],
        ["50226","佐久間"],
        ["50241","川根本町"],
        ["50261","清水"],
        ["50281","網代"],
        ["50331","静岡"],
        ["50386","天竜"],
        ["50456","浜松"],
        ["50476","菊川牧之原"],
        ["50491","松崎"],
        ["50506","稲取"],
        ["50536","磐田"],
        ["50551","御前崎"],
        ["50561","石廊崎"]
    ],
    "51":[
        ["51031","愛西"],
        ["51071","稲武"],
        ["51106","名古屋"],
        ["51116","豊田"],
        ["51216","大府"],
        ["51226","岡崎"],
        ["51247","新城"],
        ["51281","蒲郡"],
        ["51311","南知多"],
        ["51331","豊橋"],
        ["51346","伊良湖"]
    ],
    "52":[
        ["52041","河合"],
        ["52051","神岡"],
        ["52081","白川"],
        ["52111","栃尾"],
        ["52146","高山"],
        ["52181","六厩"],
        ["52196","宮之前"],
        ["52221","長滝"],
        ["52286","萩原"],
        ["52331","八幡"],
        ["52346","宮地"],
        ["52381","樽見"],
        ["52406","金山"],
        ["52461","美濃"],
        ["52482","黒川"],
        ["52511","揖斐川"],
        ["52536","美濃加茂"],
        ["52556","恵那"],
        ["52557","中津川"],
        ["52571","関ケ原"],
        ["52581","大垣"],
        ["52586","岐阜"],
        ["52606","多治見"]
    ],
    "53":[
        ["53041","桑名"],
        ["53061","四日市"],
        ["53091","亀山"],
        ["53112","上野"],
        ["53133","津"],
        ["53196","小俣"],
        ["53231","粥見"],
        ["53257","鳥羽"],
        ["53296","南伊勢"],
        ["53326","紀伊長島"],
        ["53378","尾鷲"],
        ["53401","熊野新鹿"]
    ],
    "54":[
        ["54012","粟島"],
        ["54041","弾崎"],
        ["54086","村上"],
        ["54157","相川"],
        ["54166","両津"],
        ["54181","中条"],
        ["54191","下関"],
        ["54232","新潟"],
        ["54271","羽茂"],
        ["54296","新津"],
        ["54341","巻"],
        ["54387","寺泊"],
        ["54396","三条"],
        ["54421","津川"],
        ["54501","長岡"],
        ["54541","柏崎"],
        ["54566","守門"],
        ["54586","大潟"],
        ["54616","小出"],
        ["54651","高田"],
        ["54661","安塚"],
        ["54676","十日町"],
        ["54711","糸魚川"],
        ["54721","能生"],
        ["54816","関山"],
        ["54836","津南"],
        ["54841","湯沢"]
    ],
    "55":[
        ["55022","朝日"],
        ["55041","氷見"],
        ["55056","魚津"],
        ["55091","伏木"],
        ["55102","富山"],
        ["55141","砺波"],
        ["55166","上市"],
        ["55191","南砺高宮"],
        ["55206","八尾"]
    ],
    "56":[
        ["56036","珠洲"],
        ["56052","輪島"],
        ["56116","志賀"],
        ["56146","七尾"],
        ["56176","羽咋"],
        ["56186","かほく"],
        ["56227","金沢"],
        ["56276","小松"],
        ["56286","白山河内"],
        ["56301","加賀菅谷"]
    ],
    "57":[
        ["57001","三国"],
        ["57051","越廼"],
        ["57066","福井"],
        ["57082","勝山"],
        ["57121","大野"],
        ["57206","今庄"],
        ["57248","敦賀"],
        ["57286","美浜"],
        ["57317","小浜"]
    ],
    "60":[
        ["60051","今津"],
        ["60061","長浜"],
        ["60102","米原"],
        ["60116","南小松"],
        ["60131","彦根"],
        ["60196","東近江"],
        ["60216","大津"],
        ["60226","信楽"],
        ["60236","土山"]
    ],
    "61":[
        ["61001","間人"],
        ["61076","宮津"],
        ["61111","舞鶴"],
        ["61187","福知山"],
        ["61206","美山"],
        ["61242","園部"],
        ["61286","京都"],
        ["61326","京田辺"]
    ],
    "62":[
        ["62016","能勢"],
        ["62046","枚方"],
        ["62078","大阪"],
        ["62081","生駒山"],
        ["62091","堺"],
        ["62131","熊取"]
    ],
    "63":[
        ["63016","香住"],
        ["63051","豊岡"],
        ["63071","兎和野高原"],
        ["63121","和田山"],
        ["63201","生野"],
        ["63216","柏原"],
        ["63251","一宮"],
        ["63321","福崎"],
        ["63331","西脇"],
        ["63366","上郡"],
        ["63383","姫路"],
        ["63411","三田"],
        ["63461","三木"],
        ["63491","家島"],
        ["63496","明石"],
        ["63518","神戸"],
        ["63551","郡家"],
        ["63571","洲本"],
        ["63588","南淡"]
    ],
    "64":[
        ["64036","奈良"],
        ["64041","針"],
        ["64101","大宇陀"],
        ["64127","五條"],
        ["64206","上北山"],
        ["64227","風屋"]
    ],
    "65":[
        ["65026","かつらぎ"],
        ["65036","友ケ島"],
        ["65042","和歌山"],
        ["65061","高野山"],
        ["65121","清水"],
        ["65162","龍神"],
        ["65201","川辺"],
        ["65256","栗栖川"],
        ["65276","新宮"],
        ["65306","西川"],
        ["65356","潮岬"]
    ],
    "66":[
        ["66046","上長田"],
        ["66091","千屋"],
        ["66127","奈義"],
        ["66136","今岡"],
        ["66171","久世"],
        ["66186","津山"],
        ["66221","新見"],
        ["66296","福渡"],
        ["66306","和気"],
        ["66336","高梁"],
        ["66408","岡山"],
        ["66421","虫明"],
        ["66446","倉敷"],
        ["66481","笠岡"],
        ["66501","玉野"]
    ],
    "67":[
        ["67016","高野"],
        ["67106","三次"],
        ["67116","庄原"],
        ["67151","大朝"],
        ["67191","油木"],
        ["67212","加計"],
        ["67292","三入"],
        ["67316","世羅"],
        ["67326","府中"],
        ["67376","東広島"],
        ["67401","福山"],
        ["67421","廿日市津田"],
        ["67437","広島"],
        ["67461","竹原"],
        ["67471","生口島"],
        ["67496","大竹"],
        ["67511","呉"],
        ["67576","呉市蒲刈"]
    ],
    "68":[
        ["68022","西郷"],
        ["68056","海士"],
        ["68091","鹿島"],
        ["68132","松江"],
        ["68156","出雲"],
        ["68246","大田"],
        ["68261","掛合"],
        ["68276","横田"],
        ["68306","赤名"],
        ["68351","川本"],
        ["68376","浜田"],
        ["68401","瑞穂"],
        ["68431","弥栄"],
        ["68462","益田"],
        ["68516","津和野"],
        ["68541","吉賀"]
    ],
    "69":[
        ["69006","境"],
        ["69021","塩津"],
        ["69041","青谷"],
        ["69061","岩井"],
        ["69076","米子"],
        ["69101","倉吉"],
        ["69122","鳥取"],
        ["69246","智頭"],
        ["69271","茶屋"]
    ],
    "81":[
        ["81011","須佐"],
        ["81071","萩"],
        ["81116","油谷"],
        ["81151","徳佐"],
        ["81196","秋吉台"],
        ["81231","広瀬"],
        ["81266","豊田"],
        ["81286","山口"],
        ["81321","岩国"],
        ["81371","防府"],
        ["81386","下松"],
        ["81397","玖珂"],
        ["81428","下関"],
        ["81481","柳井"],
        ["81486","安下庄"]
    ],
    "71":[
        ["71066","池田"],
        ["71087","穴吹"],
        ["71106","徳島"],
        ["71191","京上"],
        ["71231","蒲生田"],
        ["71251","木頭"],
        ["71266","日和佐"],
        ["71291","海陽"]
    ],
    "72":[
        ["72061","内海"],
        ["72086","高松"],
        ["72111","多度津"],
        ["72121","滝宮"],
        ["72146","引田"],
        ["72161","財田"]
    ],
    "73":[
        ["73001","大三島"],
        ["73076","今治"],
        ["73126","西条"],
        ["73141","新居浜"],
        ["73151","四国中央"],
        ["73166","松山"],
        ["73256","長浜"],
        ["73276","久万"],
        ["73306","大洲"],
        ["73341","瀬戸"],
        ["73406","宇和"],
        ["73442","宇和島"],
        ["73446","近永"],
        ["73516","御荘"]
    ],
    "74":[
        ["74056","本川"],
        ["74071","本山"],
        ["74136","大栃"],
        ["74181","高知"],
        ["74187","後免"],
        ["74271","安芸"],
        ["74296","梼原"],
        ["74311","須崎"],
        ["74361","窪川"],
        ["74372","室戸岬"],
        ["74381","江川崎"],
        ["74436","佐賀"],
        ["74447","宿毛"],
        ["74456","中村"],
        ["74516","清水"]
    ],
    "82":[
        ["82046","宗像"],
        ["82056","八幡"],
        ["82101","行橋"],
        ["82136","飯塚"],
        ["82171","前原"],
        ["82182","福岡"],
        ["82191","太宰府"],
        ["82206","添田"],
        ["82261","朝倉"],
        ["82306","久留米"],
        ["82317","黒木"],
        ["82361","大牟田"]
    ],
    "83":[
        ["83021","国見"],
        ["83051","中津"],
        ["83061","豊後高田"],
        ["83106","院内"],
        ["83121","杵築"],
        ["83137","日田"],
        ["83191","玖珠"],
        ["83201","湯布院"],
        ["83216","大分"],
        ["83341","犬飼"],
        ["83371","竹田"],
        ["83401","佐伯"],
        ["83431","宇目"],
        ["83476","蒲江"]
    ],
    "84":[
        ["84012","鰐浦"],
        ["84072","厳原"],
        ["84121","芦辺"],
        ["84171","平戸"],
        ["84183","松浦"],
        ["84266","佐世保"],
        ["84306","西海"],
        ["84341","有川"],
        ["84496","長崎"],
        ["84519","雲仙岳"],
        ["84523","島原"],
        ["84536","福江"],
        ["84561","口之津"],
        ["84597","脇岬"]
    ],
    "85":[
        ["85033","唐津"],
        ["85116","伊万里"],
        ["85142","佐賀"],
        ["85161","嬉野"],
        ["85166","白石"]
    ],
    "86":[
        ["86006","鹿北"],
        ["86066","南小国"],
        ["86086","岱明"],
        ["86101","菊池"],
        ["86111","阿蘇乙姫"],
        ["86141","熊本"],
        ["86156","阿蘇山"],
        ["86157","南阿蘇"],
        ["86161","高森"],
        ["86216","三角"],
        ["86236","甲佐"],
        ["86271","松島"],
        ["86316","本渡"],
        ["86336","八代"],
        ["86451","水俣"],
        ["86467","人吉"],
        ["86477","上"],
        ["86491","牛深"]
    ],
    "87":[
        ["87041","高千穂"],
        ["87066","古江"],
        ["87071","鞍岡"],
        ["87141","延岡"],
        ["87181","日向"],
        ["87206","神門"],
        ["87231","西米良"],
        ["87293","高鍋"],
        ["87301","加久藤"],
        ["87331","西都"],
        ["87352","小林"],
        ["87376","宮崎"],
        ["87406","田野"],
        ["87426","都城"],
        ["87492","油津"],
        ["87501","串間"]
    ],
    "88":[
        ["88061","阿久根"],
        ["88081","大口"],
        ["88107","さつま柏原"],
        ["88131","中甑"],
        ["88151","川内"],
        ["88261","東市来"],
        ["88286","牧之原"],
        ["88317","鹿児島"],
        ["88331","輝北"],
        ["88371","加世田"],
        ["88406","志布志"],
        ["88432","喜入"],
        ["88442","鹿屋"],
        ["88447","肝付前田"],
        ["88466","枕崎"],
        ["88486","指宿"],
        ["88506","内之浦"],
        ["88536","田代"],
        ["88612","種子島"],
        ["88666","上中"],
        ["88686","屋久島"],
        ["88706","尾之間"],
        ["88736","中之島"],
        ["88836","名瀬"],
        ["88901","古仁屋"],
        ["88956","伊仙"],
        ["88971","沖永良部"]
    ],
    "9194":[
        ["91011","伊是名"],
        ["91021","奥"],
        ["91107","名護"],
        ["91146","久米島"],
        ["91166","宮城島"],
        ["91181","渡嘉敷"],
        ["91197","那覇"],
        ["91241","糸数"],
        ["92011","南大東"],
        ["93041","宮古島"],
        ["94001","伊原間"],
        ["94017","与那国島"],
        ["94062","西表島"],
        ["94081","石垣島"],
        ["94101","大原"],
        ["94116","波照間"]
    ]
};

var data = {
    region: region,
    prefecture: prefecture,
    point, point
}
var jsonString = JSON.stringify(data)
// console.log(jsonString)

var fs = require('fs')
fs.writeFile("data.json", jsonString, function(err) {
    if (err) {
        console.log(err);
    }
});