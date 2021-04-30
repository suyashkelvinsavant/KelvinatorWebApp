import json
import time
from datetime import datetime

arr=[1617080400, 1617080700, 1617081000, 1617081300, 1617081600, 1617081900, 1617082500, 1617082800, 1617083100, 1617083400, 1617083700, 1617084000, 1617084300, 1617084600, 1617084900, 1617085200, 1617085500, 1617085800, 1617086100, 1617086400, 1617087000, 1617087300, 1617087600, 1617087900, 1617088200, 1617088500, 1617088800, 1617089100, 1617089400, 1617089700, 1617090000, 1617090300, 1617090600, 1617090900, 1617091200, 1617091500, 1617091800, 1617092100, 1617092400, 1617092700, 1617093000, 1617093300, 1617093600, 1617093900, 1617094200, 1617094500, 1617094800, 1617095100, 1617095400, 1617095700, 1617096000, 1617096300, 1617096600, 1617096900, 1617097200, 1617097500, 1617097800, 1617098100, 1617162300, 1617162600, 1617162900, 1617163200, 1617163500, 1617163800, 1617164100, 1617164700, 1617165000, 1617165300, 1617165600, 1617165900, 1617166200, 1617166500, 1617166800, 1617167100, 1617167400, 1617167700, 1617168000, 1617168300, 1617168600, 1617168900, 1617169200, 1617169500, 1617169800, 1617170400, 1617170700, 1617171000, 1617171300, 1617171600, 1617171900, 1617172200, 1617172500, 1617172800, 1617173100, 1617173400, 1617173700, 1617174000, 1617174300, 1617174600, 1617174900, 1617175200, 1617175500, 1617175800, 1617176100, 1617176400, 1617177000, 1617177300, 1617177600, 1617177900, 1617178200, 1617178500, 1617178800, 1617179100, 1617179400, 1617179700, 1617180000, 1617180600, 1617180900, 1617181200, 1617181500, 1617182100, 1617182700, 1617183000, 1617183300, 1617183600, 1617183900, 1617184200, 1617184500, 1617248700, 1617249000, 1617249300, 1617249600, 1617249900, 1617250200, 1617250500, 1617250800, 1617251100, 1617251400, 1617251700, 1617252000, 1617252300, 1617252600, 1617253200, 1617253500, 1617253800, 1617254100, 1617254400, 1617254700, 1617255000, 1617255300, 1617255600, 1617255900, 1617256200, 1617256500, 1617256800, 1617257100, 1617257400, 1617257700, 1617258000, 1617258300, 1617258600, 1617258900, 1617259200, 1617259500, 1617260100, 1617260400, 1617260700, 1617261000, 1617261300, 1617261600, 1617261900, 1617262200, 1617262500, 1617262800, 1617263100, 1617263400, 1617263700, 1617264000, 1617264300, 1617264600, 1617264900, 1617265200, 1617265500, 1617265800, 1617266100, 1617266400, 1617266700, 1617267000, 1617267300, 1617267600, 1617267900, 1617268200, 1617268500, 1617268800, 1617269100, 1617269400, 1617269700, 1617270000, 1617270300, 1617270600, 1617270900, 1617594300, 1617594600, 1617594900, 1617595200, 1617595500, 1617595800, 1617596100, 1617596400, 1617596700, 1617597000, 1617597300, 1617597600, 1617597900, 1617598200, 1617598500, 1617598800, 1617599100, 1617599400, 1617599700, 1617600000, 1617600300, 1617600600, 1617600900, 1617601200, 1617601500, 1617601800, 1617602100, 1617602400, 1617602700, 1617603000, 1617603300, 1617603600, 1617603900, 1617604200, 1617604500, 1617604800, 1617605100, 1617605400, 1617605700, 1617606000, 1617606600, 1617606900, 1617607200, 1617607500, 1617607800, 1617608100, 1617608400, 1617608700, 1617609000, 1617609300, 1617609600, 1617609900, 1617610200, 1617610500, 1617610800, 1617611100, 1617611400, 1617611700, 1617612000, 1617612300, 1617612600, 1617612900, 1617613200, 1617613500, 1617613800, 1617614100, 1617614400, 1617614700, 1617615000, 1617615300, 1617615600, 1617615900, 1617616200, 1617616500, 1617680700, 1617681000, 1617681300, 1617681600, 1617681900, 1617682200, 1617682500, 1617682800, 1617683100, 1617683400, 1617684000, 1617684300, 1617684600, 1617684900, 1617685200, 1617685500, 1617686100, 1617686400, 1617686700, 1617687000, 1617687300, 1617687600, 1617687900, 1617688200, 1617688500, 1617688800, 1617689100, 1617689400, 1617689700, 1617690300, 1617690900, 1617691200, 1617691500, 1617691800, 1617692100, 1617692400, 1617693000, 1617693300, 1617693600, 1617693900, 1617694200, 1617694500, 1617694800, 1617695400, 1617695700, 1617696000, 1617696300, 1617696600, 1617696900, 1617697500, 1617697800, 1617698100, 1617698400, 1617698700, 1617699000, 1617699300, 1617699600, 1617699900, 1617700200, 1617700500, 1617700800, 1617701100, 1617701400, 1617701700, 1617702000, 1617702300, 1617702600, 1617702900, 1617767100, 1617767400, 1617767700, 1617768000, 1617768300, 1617768600, 1617768900, 1617769200, 1617769500, 1617769800, 1617770100, 1617770400, 1617770700, 1617771000, 1617771300, 1617771600, 1617771900, 1617772200, 1617772500, 1617772800, 1617773100, 1617773400, 1617773700, 1617774000, 1617774300, 1617774600, 1617774900, 1617775200, 1617775500, 1617775800, 1617776100, 1617776400, 1617776700, 1617777000, 1617777300, 1617777600, 1617777900, 1617778200, 1617778500, 1617778800, 1617779100, 1617779400, 1617779700, 1617780000, 1617780300, 1617780600, 1617780900, 1617781200, 1617781500, 1617781800, 1617782100, 1617782400, 1617782700, 1617783000, 1617783300, 1617783600, 1617783900, 1617784200, 1617784500, 1617784800, 1617785100, 1617785400, 1617785700, 1617786000, 1617786300, 1617786600, 1617786900, 1617787200, 1617787500, 1617787800, 1617788100, 1617788400, 1617788700, 1617789000, 1617789300, 1617853500, 1617853800, 1617854100, 1617854400, 1617854700, 1617855000, 1617855300, 1617855600, 1617855900, 1617856200, 1617856500, 1617856800, 1617857100, 1617857400, 1617858000, 1617858300, 1617858600, 1617858900, 1617859200, 1617859500, 1617859800, 1617860100, 1617860400, 1617860700, 1617861000, 1617861300, 1617861600, 1617861900, 1617862200, 1617862500, 1617862800, 1617863100, 1617863400, 1617863700, 1617864000, 1617864300, 1617864600, 1617864900, 1617865200, 1617865500, 1617865800, 1617866100, 1617866400, 1617866700, 1617867000, 1617867300, 1617867600, 1617867900, 1617868200, 1617868500, 1617868800, 1617869100, 1617869400, 1617869700, 1617870000, 1617870300, 1617870600, 1617870900, 1617871200, 1617871500, 1617871800, 1617872100, 1617872400, 1617872700, 1617873000, 1617873300, 1617873600, 1617873900, 1617874200, 1617874500, 1617874800, 1617875100, 1617875400, 1617875700, 1617939900, 1617940200, 1617940500, 1617940800, 1617941100, 1617941400, 1617941700, 1617942000, 1617942300, 1617942600, 1617942900, 1617943200, 1617943500, 1617943800, 1617944100, 1617944400, 1617944700, 1617945000, 1617945300, 1617945600, 1617945900, 1617946200, 1617946500, 1617946800, 1617947100, 1617947400, 1617947700, 1617948000, 1617948300, 1617948600, 1617948900, 1617949200, 1617949500, 1617949800, 1617950100, 1617950400, 1617950700, 1617951000, 1617951300, 1617951600, 1617951900, 1617952200, 1617952500, 1617952800, 1617953100, 1617953400, 1617953700, 1617954000, 1617954300, 1617954600, 1617954900, 1617955200, 1617955500, 1617955800, 1617956400, 1617956700, 1617957000, 1617957300, 1617957600, 1617957900, 1617958200, 1617958500, 1617958800, 1617959100, 1617959400, 1617959700, 1617960000, 1617960300, 1617960600, 1617960900, 1617961200, 1617961500, 1617961800, 1617962100, 1618199100, 1618199400, 1618199700, 1618200000, 1618200300, 1618200600, 1618200900, 1618201200, 1618201500, 1618201800, 1618202100, 1618202400, 1618202700, 1618203000, 1618203300, 1618203600, 1618203900, 1618204200, 1618204500, 1618204800, 1618205100, 1618205400, 1618205700, 1618206000, 1618206300, 1618206600, 1618206900, 1618207200, 1618207500, 1618207800, 1618208100, 1618208400, 1618208700, 1618209000, 1618209300, 1618209600, 1618209900, 1618210200, 1618210500, 1618210800, 1618211100, 1618211400, 1618211700, 1618212000, 1618212300, 1618212600, 1618212900, 1618213200, 1618213500, 1618213800, 1618214100, 1618214400, 1618214700, 1618215000, 1618215300, 1618215900, 1618216200, 1618216500, 1618216800, 1618217100, 1618217400, 1618217700, 1618218000, 1618218300, 1618218600, 1618218900, 1618219200, 1618219500, 1618219800, 1618220100, 1618220400, 1618220700, 1618221000, 1618221300, 1618285500, 1618285800, 1618286100, 1618286400, 1618286700, 1618287000, 1618287300, 1618287600, 1618287900, 1618288200, 1618288500, 1618288800, 1618289100, 1618289400, 1618289700, 1618290000, 1618290300, 1618290600, 1618290900, 1618291200, 1618291500, 1618291800, 1618292100, 1618292400, 1618292700, 1618293000, 1618293300, 1618293600, 1618293900, 1618294200, 1618294500, 1618294800, 1618295100, 1618295400, 1618295700, 1618296000, 1618296300, 1618296600, 1618296900, 1618297200, 1618297500, 1618297800, 1618298100, 1618298400, 1618298700, 1618299000, 1618299300, 1618299600, 1618299900, 1618300200, 1618300500, 1618300800, 1618301100, 1618301400, 1618301700, 1618302000, 1618302300, 1618302600, 1618302900, 1618303200, 1618303500, 1618303800, 1618304100, 1618304400, 1618304700, 1618305000, 1618305300, 1618305600, 1618305900, 1618306200, 1618306500, 1618306800, 1618307100, 1618307400, 1618307700, 1618458300, 1618458600, 1618458900, 1618459200, 1618459500, 1618459800, 1618460100, 1618460400, 1618460700, 1618461000, 1618461300, 1618461600, 1618461900, 1618462200, 1618462500, 1618462800, 1618463100, 1618463400, 1618463700, 1618464000, 1618464300, 1618464600, 1618464900, 1618465200, 1618465500, 1618465800, 1618466100, 1618466400, 1618466700, 1618467000, 1618467300, 1618467600, 1618467900, 1618468200, 1618468500, 1618468800, 1618469100, 1618469400, 1618469700, 1618470000, 1618470300, 1618470600, 1618470900, 1618471200, 1618471500, 1618471800, 1618472100, 1618472700, 1618473000, 1618473300, 1618473600, 1618473900, 1618474200, 1618474500, 1618474800, 1618475100, 1618475400, 1618475700, 1618476000, 1618476300, 1618476600, 1618476900, 1618477200, 1618477500, 1618477800, 1618478100, 1618478400, 1618478700, 1618479000, 1618479300, 1618479600, 1618479900, 1618480200, 1618480500, 1618544700, 1618545000, 1618545300, 1618545600, 1618545900, 1618546200, 1618546500, 1618546800, 1618547100, 1618547400, 1618547700, 1618548000, 1618548300, 1618548600, 1618548900, 1618549200, 1618549500, 1618549800, 1618550100, 1618550400, 1618550700, 1618551000, 1618551300, 1618551600, 1618551900, 1618552200, 1618552500, 1618552800, 1618553100, 1618553400, 1618553700, 1618554000, 1618554300, 1618554600, 1618554900, 1618555200, 1618555500, 1618555800, 1618556100, 1618556400, 1618556700, 1618557000, 1618557300, 1618557600, 1618557900, 1618558200, 1618558500, 1618558800, 1618559100, 1618559400, 1618559700, 1618560000, 1618560300, 1618560600, 1618560900, 1618561200, 1618561500, 1618562100, 1618562700, 1618563000, 1618563300, 1618563900, 1618564200, 1618564500, 1618564800, 1618565100, 1618565400, 1618565700, 1618566000, 1618566300, 1618566600, 1618566900, 1618803900, 1618804200, 1618804500, 1618804800, 1618805100, 1618805400, 1618805700, 1618806000, 1618806300, 1618806600, 1618806900, 1618807200, 1618807500, 1618807800, 1618808100, 1618808400, 1618808700, 1618809000, 1618809300, 1618809600, 1618809900, 1618810200, 1618810500, 1618810800, 1618811100, 1618811400, 1618811700, 1618812000, 1618812300, 1618812600, 1618812900, 1618813200, 1618813500, 1618813800, 1618814100, 1618814400, 1618814700, 1618815000, 1618815300, 1618815600, 1618815900, 1618816200, 1618816500, 1618816800, 1618817100, 1618817400, 1618817700, 1618818000, 1618818300, 1618818600, 1618818900, 1618819200, 1618819500, 1618819800, 1618820100, 1618820400, 1618820700, 1618821000, 1618821300, 1618821600, 1618821900, 1618822200, 1618822500, 1618822800, 1618823100, 1618823400, 1618823700, 1618824000, 1618824300, 1618824600, 1618824900, 1618825200, 1618825500, 1618825800, 1618826100, 1618890300, 1618890600, 1618890900, 1618891200, 1618891500, 1618891800, 1618892400, 1618892700, 1618893000, 1618893300, 1618893600, 1618893900, 1618894200, 1618894500, 1618894800, 1618895100, 1618895400, 1618895700, 1618896000, 1618896300, 1618896600, 1618896900, 1618897200, 1618897500, 1618897800, 1618898100, 1618898400, 1618898700, 1618899000, 1618899300, 1618899600, 1618899900, 1618900200, 1618900500, 1618900800, 1618901100, 1618901400, 1618901700, 1618902000, 1618902300, 1618902600, 1618902900, 1618903200, 1618903500, 1618903800, 1618904100, 1618904400, 1618904700, 1618905000, 1618905300, 1618905600, 1618905900, 1618906200, 1618906500, 1618906800, 1618907100, 1618907400, 1618907700, 1618908000, 1618908300, 1618908600, 1618908900, 1618909200, 1618909500, 1618909800, 1618910100, 1618910400, 1618910700, 1618911000, 1618911300, 1618911600, 1618911900, 1618912200, 1618912500, 1619063100, 1619063400, 1619063700, 1619064000, 1619064300, 1619064600, 1619064900, 1619065200, 1619065500, 1619065800, 1619066100, 1619066400, 1619066700, 1619067000, 1619067300, 1619067600, 1619067900, 1619068200, 1619068500, 1619068800, 1619069100, 1619069400, 1619069700, 1619070000, 1619070300, 1619070600, 1619070900, 1619071200, 1619071500, 1619071800, 1619072100, 1619072400, 1619073000, 1619073300, 1619073600, 1619073900, 1619074200, 1619074500, 1619074800, 1619075100, 1619075400, 1619075700, 1619076000, 1619076300, 1619076600, 1619076900, 1619077200, 1619077500, 1619077800, 1619078100, 1619078400, 1619078700, 1619079000, 1619079300, 1619079600, 1619079900, 1619080200, 1619080500, 1619080800, 1619081100, 1619081400, 1619081700, 1619082000, 1619082300, 1619082600, 1619082900, 1619083200, 1619083500, 1619083800, 1619084100, 1619084400, 1619084700, 1619085000, 1619085300, 1619149500, 1619149800, 1619150100, 1619150400, 1619150700, 1619151000, 1619151300, 1619151600, 1619151900, 1619152200, 1619152500, 1619152800, 1619153400, 1619153700, 1619154000, 1619154300, 1619154900, 1619155200, 1619155500, 1619155800, 1619156100, 1619156400, 1619156700, 1619157000, 1619157300, 1619157600, 1619157900, 1619158200, 1619158500, 1619158800, 1619159100, 1619159700, 1619160000, 1619160300, 1619160600, 1619160900, 1619161200, 1619161500, 1619161800, 1619162100, 1619162400, 1619162700, 1619163000, 1619163300, 1619163600, 1619163900, 1619164200, 1619164500, 1619164800, 1619165100, 1619165400, 1619165700, 1619166000, 1619166300, 1619166600, 1619166900, 1619167200, 1619167500, 1619167800, 1619168100, 1619168400, 1619168700, 1619169000, 1619169300, 1619169600, 1619169900, 1619170200, 1619170500, 1619170800, 1619171100, 1619171400, 1619171700, 1619408700, 1619409000, 1619409300, 1619409600, 1619409900, 1619410200, 1619410500, 1619410800, 1619411100, 1619411400, 1619411700, 1619412000, 1619412300, 1619412600, 1619412900, 1619413200, 1619413500, 1619413800, 1619414100, 1619414400, 1619414700, 1619415000, 1619415300, 1619415600, 1619415900, 1619416200, 1619416500, 1619416800, 1619417100, 1619417400, 1619417700, 1619418000, 1619418300, 1619418600, 1619418900, 1619419200, 1619419500, 1619419800, 1619420100, 1619420400, 1619420700, 1619421000, 1619421300, 1619421600, 1619421900, 1619422200, 1619422500, 1619422800, 1619423100, 1619423400, 1619423700, 1619424000, 1619424300, 1619424600, 1619424900, 1619425200, 1619425500, 1619425800, 1619426100, 1619426400, 1619426700, 1619427000, 1619427300, 1619427600, 1619427900, 1619428200, 1619428500, 1619428800, 1619429100, 1619429400, 1619429700, 1619430000, 1619430300, 1619430600, 1619430900, 1619495100, 1619495400, 1619495700, 1619496000, 1619496300, 1619496600, 1619496900, 1619497200, 1619497500, 1619497800, 1619498100, 1619498400, 1619498700, 1619499000, 1619499300, 1619499600, 1619499900, 1619500200, 1619500500, 1619500800, 1619501100, 1619501400, 1619501700, 1619502000, 1619502300, 1619502600, 1619503500, 1619503800, 1619504100, 1619504400, 1619504700, 1619505000, 1619505300, 1619505600, 1619505900, 1619506200, 1619506500, 1619506800, 1619507100, 1619507400, 1619507700, 1619508000, 1619508300, 1619508600, 1619508900, 1619509200, 1619509500, 1619509800, 1619510100, 1619510400, 1619510700, 1619511000, 1619511300, 1619511600, 1619511900, 1619512200, 1619512500, 1619512800, 1619513100, 1619513400, 1619513700, 1619514000, 1619514300, 1619514600, 1619514900, 1619515200, 1619515500, 1619515800, 1619516100, 1619516700, 1619517000, 1619517300, 1619581500, 1619581800, 1619582100, 1619582400, 1619582700, 1619583000, 1619583300, 1619583600, 1619583900, 1619584200, 1619584500, 1619584800, 1619585100, 1619585400, 1619585700, 1619586000, 1619586300, 1619586600, 1619586900, 1619587200, 1619587500, 1619587800, 1619588100, 1619588400, 1619588700, 1619589000, 1619589300, 1619589600, 1619589900, 1619590200, 1619590500, 1619590800, 1619591100, 1619591400, 1619591700, 1619592000, 1619592300, 1619592600, 1619592900, 1619593200, 1619593500, 1619593800, 1619594100, 1619594400, 1619594700, 1619595000, 1619595300, 1619595600, 1619595900, 1619596200, 1619596500, 1619596800, 1619597100, 1619597400, 1619597700, 1619598000, 1619598300, 1619598600, 1619598900, 1619599200, 1619599500, 1619599800, 1619600100, 1619600400, 1619600700, 1619601000, 1619601300, 1619601600, 1619601900, 1619602200, 1619602500, 1619602800, 1619603400, 1619603700, 1619667900, 1619668200, 1619668500, 1619668800, 1619669400, 1619669700, 1619670000, 1619670300, 1619670600, 1619670900, 1619671200, 1619671500, 1619671800, 1619672100, 1619672400, 1619672700, 1619673000, 1619673300, 1619673600, 1619673900, 1619674200, 1619674500, 1619674800, 1619675100, 1619675400, 1619675700, 1619676000, 1619676300, 1619676600, 1619676900, 1619677200, 1619677500, 1619677800, 1619678100, 1619678400, 1619678700, 1619679000, 1619679300, 1619679600, 1619679900, 1619680200, 1619680500, 1619680800, 1619681100, 1619681400, 1619681700, 1619682000, 1619682300, 1619682600, 1619682900, 1619683200, 1619683500, 1619683800, 1619684100, 1619684400, 1619684700, 1619685000, 1619685300, 1619685600, 1619685900, 1619686200, 1619686500, 1619686800, 1619687400, 1619687700, 1619688000, 1619688300, 1619688600, 1619688900, 1619689200, 1619689500, 1619689800, 1619690100, 1619754300, 1619754600, 1619754900, 1619755200, 1619755500, 1619755800, 1619756100, 1619756400, 1619756700, 1619757000, 1619757300, 1619757600, 1619757900, 1619758200, 1619758500, 1619758800, 1619759010]



#print(datetime.now().day,datetime.fromtimestamp(1619757065).day,datetime.fromtimestamp(1619757065).month)
print(len(arr))
for i in range(len(arr)):
    a=datetime.now()
    if(a.day==datetime.fromtimestamp(arr[i]).day and a.month==datetime.fromtimestamp(arr[i]).month and a.year==datetime.fromtimestamp(arr[i]).year):
        arr=arr[:-(len(arr)-i)]
        break
print(arr)
print(len(arr))















# indexArr=[]
# for i in range(len(arr)):
#     a=datetime.now()
#     if(a.day==datetime.fromtimestamp(arr[i]).day and a.month==datetime.fromtimestamp(arr[i]).month):
#         indexArr.append(i)
# #print(indexArr)
# j=0
# for i in indexArr:
#     del arr[i-j]
#     j=j+1
# print(arr)