n = 54749648884874001108038301329774150258791219273879249601123423751292261798269586163458351220727718910448330440812899799 
e = 65537
ct = [52052531108833646741308670070505961165002560985048445381912028939564989677616205955826911335832917245744890104862186090,24922951057478302364724559167904980705887738247412638765127966502743153757232333552037075100099370197070290632101808468,31333127727137796897042309238173536507191002247724391776525004646835609286736822503824661004274731843794662964916495223,37689731986801363765434552977964842847326744893755747412237221863834417045591676371189948428149435230583786704331100191,10128169466676555996026197991703355150176544836970137898778443834308512822737963589912865084777642915684970180060271437,31333127727137796897042309238173536507191002247724391776525004646835609286736822503824661004274731843794662964916495223,32812400903438770915197382692214538476619741855721568752778494391450400789199013823710431516615200277044713539798778715,48025916179002039543667066543229077043664743885236966440148037177519549014220494347050632249422811334833955153322952673,52052531108833646741308670070505961165002560985048445381912028939564989677616205955826911335832917245744890104862186090,32361547617137901317806379693272240413733790836009458796321421127203474492226452174262060699920809988522470389903614273,4363489969092225528080759459787310678757906094535883427177575648271159671231893743333971538008898236171319923600913595,47547012183185969621160796219188218632479553350320144243910899620916340486530260137942078177950196822162601265598970316,32361547617137901317806379693272240413733790836009458796321421127203474492226452174262060699920809988522470389903614273,33230176060697422282963041481787429356625466151312645509735017885677065049255922834285581184333929676004385794200287512,32315367490632724156951918599011490591675821430702993102310587414983799536144448443422803347161835581835150218650491476,6693321814134847191589970230119476337298868688019145564978701711983917711748098646193404262988591606678067236821423683,32710099976003111674253316918478650203401654878438242131530874012644296546811017566357720665458366371664393857312271236,49634925172985572829440801211650861229901370508351528081966542823154634901317953867012392769315424444802884795745057309,50837960186490992399835102776517955354761635070927126755411572132063618791417763562399134862015458682285563340315570436]

from string import printable
flag = ""

for j in ct:
	for i in printable:
		print(flag + i)
		if pow(ord(i), e, n) == j:
			flag = flag + i
			break
