'''
Created on Oct 3, 2011

@author: jcg
'''
import os

# project_dir = os.path.dirname(os.path.abspath(__file__))
project_dir_old = os.path.dirname(os.path.abspath(__file__))

bases = ['a', 't', 'g', 'c']

codons_list  = ['tct', 'atc', 'tgc', 'tgg', 'ttc', 'tcg', 'gca', 'tcc', 'aga', 'tca', 'tac', 'caa', 'tgt', 'ata', 'ctc', 'ctt', 'atg', 'cgt', 'gta', 'ctg', 'ttt', 'gct', 'cta', 'att', 'gat', 'ggt', 'acc', 'gtt', 'cga', 'tat', 'cgc', 'aag', 'cgg', 'gcc', 'aaa', 'ggg', 'gga', 'ggc', 'gag', 'acg', 'ttg', 'gac', 'ccg', 'gaa', 'gtc', 'aca', 'gtg', 'gcg', 'aac', 'cct', 'cag', 'agc', 'cat', 'aat', 'agg', 'tta', 'act', 'cac', 'agt', 'cca', 'ccc']
scod = ['taa', 'tag', 'tga']
rcod = ['agg', 'aga', 'cga', 'cta','ata','ccc']

aa2codon_table =  { 'phe' : ['ttt','ttc'] ,
                    'leu' : ['tta','ttg','ctt','ctc','cta','ctg'],
                    'ile' : ['att','atc','ata'],
                    'met' : ['atg'],
                    'val' : ['gtt','gtc','gta','gtg'],
                    'ser' : ['tct','tcc','tca','tcg','agt','agc'],
                    'pro' : ['cct','ccc','cca','ccg'],
                    'thr' : ['act','acc','aca','acg'],
                    'ala' : ['gct','gcc','gca','gcg'],
                    'tyr' : ['tat','tac'],
                    'stop': ['taa','tag','tga'],
                    'his' : ['cat','cac'],
                    'gln' : ['caa','cag'],
                    'asn' : ['aat','aac'],
                    'lys' : ['aaa','aag'],
                    'asp' : ['gat','gac'],
                    'glu' : ['gaa','gag'],
                    'cys' : ['tgt','tgc'],
                    'trp' : ['tgg'],
                    'arg' : ['cgt','cgc','cga','cgg','aga','agg'],
                    'gly' : ['ggt','ggc','gga','ggg'] }

codon2aa_table =  { 'aaa' : 'lys',
                    'aag' : 'lys',
                    'tta' : 'leu',
                    'ttg' : 'leu',
                    'ctt' : 'leu',
                    'ctc' : 'leu',
                    'cta' : 'leu',
                    'ctg' : 'leu',
                    'gaa' : 'glu',
                    'gag' : 'glu',
                    'caa' : 'gln',
                    'cag' : 'gln',
                    'cat' : 'his',
                    'cac' : 'his',
                    'aat' : 'asn',
                    'aac' : 'asn',
                    'tct' : 'ser',
                    'tcc' : 'ser',
                    'tca' : 'ser',
                    'tcg' : 'ser',
                    'agt' : 'ser',
                    'agc' : 'ser',
                    'cgt' : 'arg',
                    'cgc' : 'arg',
                    'cga' : 'arg',
                    'cgg' : 'arg',
                    'aga' : 'arg',
                    'agg' : 'arg',
                    'tgg' : 'trp',
                    'gct' : 'ala',
                    'gcc' : 'ala',
                    'gca' : 'ala',
                    'gcg' : 'ala',
                    'tgt' : 'cys',
                    'tgc' : 'cys',
                    'ggt' : 'gly',
                    'ggc' : 'gly',
                    'gga' : 'gly',
                    'ggg' : 'gly',
                    'gat' : 'asp',
                    'gac' : 'asp',
                    'ttt' : 'phe',
                    'ttc' : 'phe',
                    'atg' : 'met',
                    'tat' : 'tyr',
                    'tac' : 'tyr',
                    'gtt' : 'val',
                    'gtc' : 'val',
                    'gta' : 'val',
                    'gtg' : 'val',
                    'act' : 'thr',
                    'acc' : 'thr',
                    'aca' : 'thr',
                    'acg' : 'thr',
                    'cct' : 'pro',
                    'ccc' : 'pro',
                    'cca' : 'pro',
                    'ccg' : 'pro',
                    'att' : 'ile',
                    'atc' : 'ile',
                    'ata' : 'ile',
                    'taa' : 'stop',
                    'tag' : 'stop',
                    'tga' : 'stop' }


cai_table_ec = {   'ttt' : 0.296,
                'ttg' : 0.02,
                'ttc' : 1,
                'tta' : 0.2,
                'tgt' : 0.5,
                'tgg' : 1,
                'tgc' : 1,
                'tga' : 1,
                'tct' : 1,
                'tcg' : 0.017,
                'tcc' : 0.744,
                'tca' : 0.077,
                'tat' : 0.239,
                'tag' : 1,
                'tac' : 1,
                'taa' : 1,
                'gtt' : 1,
                'gtg' : 0.221,
                'gtc' : 0.066,
                'gta' : 0.495,
                'ggt' : 1,
                'ggg' : 0.019,
                'ggc' : 0.724,
                'gga' : 0.01,
                'gct' : 1,
                'gcg' : 0.424,
                'gcc' : 0.122,
                'gca' : 0.586,
                'gat' : 0.434,
                'gag' : 0.259,
                'gac' : 1,
                'gaa' : 1,
                'ctt' : 0.042,
                'ctg' : 1,
                'ctc' : 0.037,
                'cta' : 0.007,
                'cgt' : 1,
                'cgg' : 0.004,
                'cgc' : 0.356,
                'cga' : 0.004,
                'cct' : 0.07,
                'ccg' : 1,
                'ccc' : 0.012,
                'cca' : 0.135,
                'cat' : 0.291,
                'cag' : 1,
                'cac' : 1,
                'caa' : 0.124,
                'att' : 0.185,
                'atg' : 1,
                'atc' : 1,
                'ata' : 0.003,
                'agt' : 0.085,
                'agg' : 0.002,
                'agc' : 0.41,
                'aga' : 0.004,
                'act' : 0.965,
                'acg' : 0.099,
                'acc' : 1,
                'aca' : 0.076,
                'aat' : 0.051,
                'aag' : 0.253,
                'aac' : 1,
                'aaa' : 1 }

tai_tuller = {  'gtc' : 0.25,
                'acc' : 0.25,
                'aca' : 0.125,
                'gtg' : 0.2,
                'act' : 0.10975,
                'aac' : 0.5,
                'cct' : 0.054875,
                'tgg' : 0.165,
                'agc' : 0.125,
                'aag' : 0.24,
                'cat' : 0.054875,
                'aat' : 0.2195,
                'gtt' : 0.10975,
                'cac' : 0.125,
                'acg' : 0.29,
                'agt' : 0.054875,
                'cca' : 0.125,
                'ccg' : 0.165,
                'ccc' : 0.125,
                'ggt' : 0.2195,
                'tct' : 0.10975,
                'atg' : 1.0,
                'cga' : 0.054875, #5e-05,
                'cag' : 0.33,
                'tga' : 0.125,
                'tat' : 0.164625,
                'cgg' : 0.125,
                'tcg' : 0.165,
                'agg' : 0.165,
                'ggg' : 0.165,
                'gga' : 0.125,
                'tca' : 0.125,
                'gaa' : 0.5,
                'gag' : 0.16,
                'tcc' : 0.25,
                'tac' : 0.375,
                'gac' : 0.375,
                'tgt' : 0.054875,
                'ata' : 0.163204,
                'gca' : 0.375,
                'ctt' : 0.054875,
                'gta' : 0.625,
                'ggc' : 0.5,
                'gcg' : 0.12,
                'atc' : 0.375,
                'ctg' : 0.54,
                'taa' : 0.163204,
                'gct' : 0.10975,
                'aga' : 0.125,
                'cta' : 0.125,
                'gcc' : 0.25,
                'aaa' : 0.75,
                'att' : 0.164625,
                'caa' : 0.25,
                'ttt' : 0.10975,
                'cgt' : 0.5,
                'cgc' : 0.36,
                'tgc' : 0.125,
                'tag' : 0.163204,
                'ctc' : 0.125,
                'ttg' : 0.165,
                'tta' : 0.125,
                'gat' : 0.164625,
                'ttc' : 0.25 }


hydropathy_index_table = {"aaa":-3.90, "aac":-3.50, "aag":-3.90, "aat":-3.50,
                            "aca":-0.70, "acc":-0.70, "acg":-0.70, "act":-0.70,
                            "aga":-4.50, "agc":-0.80, "agg":-4.50, "agt":-0.80,
                            "ata":4.50, "atc":4.50, "atg":1.90, "att":4.50,
                            "caa":-3.50, "cac":-3.20, "cag":-3.50, "cat":-3.20,
                            "cca":-1.60, "ccc":-1.60, "ccg":-1.60, "cct":-1.60,
                            "cga":-4.50, "cgc":-4.50, "cgg":-4.50, "cgt":-4.50,
                            "cta":3.80, "ctc":3.80, "ctg":3.80, "ctt":3.80,
                            "gaa":-3.50, "gac":-3.50, "gag":-3.50, "gat":-3.50,
                            "gca":1.80, "gcc":1.80, "gcg":1.80, "gct":1.80,
                            "gga":-0.40, "ggc":-0.40, "ggg":-0.40, "ggt":-0.40,
                            "gta":4.20, "gtc":4.20, "gtg":4.20, "gtt":4.20,
                            "tac":-1.30, "tat":-1.30, "tca":-0.80, "tcc":-0.80,
                            "tcg":-0.80, "tct":-0.80, "tgc":2.50, "tgg":-0.90,
                            "tgt":2.50, "tta":3.80, "ttc":2.80, "ttg":3.80,
                            "ttt":2.80}

pwm_rbs = {'a': [0.7199057370433655, 1.2030286117821993, -1.9264145631929932, -5.987547803839298, 1.552449588275917, 0.18559865387680505, 0.6501622933766987], 
           'c': [0.10664341040961967, -1.3462808725344189, -3.790037581422891, -5.987547803839298, -1.6274901666975587, -1.687206712669005, -0.8683985487558977], 
           't': [-2.090392223787765, -0.8657422013844742, -2.6247366853812046, -5.987547803839298, -0.4590971509196684, -0.4772289756946564, 0.16755848922854324], 
           'g': [0.058508428919707124, -0.40410169010468266, 1.8083818203552808, 1.9828452735169795, -5.987547803839298, 0.8748579849208438, -0.39641357691890833]}


pwm_pro15 = {'a': [-1.8077860069559815, -1.8077860069559815, -0.9048024872362479, 1.0178985352964702, -1.8077860069559815, 1.1038035301521685, -0.14111003251455548, -0.14111003251455548, -0.3536848465762256, -0.603085883409828, 0.3556213105624206, 0.04412774624102864, 0.04412774624102864, 0.04412774624102864, 0.20826510595244638, 0.9265526589609655, -0.14111003251455548, 0.3556213105624206, -1.2867709434202912, -0.14111003251455548, -0.14111003251455548, -1.8077860069559815, 1.4700931887583837, -0.14111003251455548, 1.3345230747502872, 0.9265526589609655, -1.8077860069559815], 
             'c': [-0.603085883409828, -2.631372634246629, -1.2867709434202912, -1.2867709434202912, 1.1848795243720076, -0.9048024872362479, 0.04412774624102864, 0.3556213105624206, 0.3556213105624206, 0.7244336116497855, -0.9048024872362479, -0.14111003251455548, 0.04412774624102864, -0.14111003251455548, -0.14111003251455548, -1.2867709434202912, 0.04412774624102864, -0.3536848465762256, 0.04412774624102864, -0.9048024872362479, -0.3536848465762256, -2.631372634246629, -1.8077860069559815, -0.9048024872362479, -1.2867709434202912, -0.14111003251455548, -1.2867709434202912], 
             't': [1.2616406526610262, 1.761961827567924, 0.04412774624102864, 0.20826510595244638, 0.04412774624102864, -0.3536848465762256, 0.04412774624102864, 0.20826510595244638, 0.20826510595244638, 0.04412774624102864, 0.4893116698775844, 0.4893116698775844, 0.20826510595244638, -0.3536848465762256, 0.04412774624102864, 0.20826510595244638, 0.4893116698775844, -0.14111003251455548, 0.04412774624102864, 0.04412774624102864, 0.04412774624102864, 1.6521942428362504, -1.8077860069559815, 1.0178985352964702, -0.603085883409828, -0.603085883409828, 1.4700931887583837], 
             'g': [-0.603085883409828, -2.631372634246629, 1.0178985352964702, -1.2867709434202912, -1.2867709434202912, -0.9048024872362479, 0.04412774624102864, -0.603085883409828, -0.3536848465762256, -0.603085883409828, -0.3536848465762256, -0.603085883409828, -0.3536848465762256, 0.3556213105624206, -0.14111003251455548, -0.9048024872362479, -0.603085883409828, 0.04412774624102864, 0.6116571979336957, 0.6116571979336957, 0.3556213105624206, -1.2867709434202912, -0.603085883409828, -0.9048024872362479, -1.2867709434202912, -0.9048024872362479, -0.9048024872362479]}

pwm_pro16 = {'a': [-0.8286240775911423, -1.8795065682166356, -1.0284291302737418, 0.7892896762743752, 0.19615965038587807, 1.3387204991091335, -0.1090822810734714, -0.22709187623390137, 0.10141117761114446, -0.6531546704737212, 0.10141117761114446, -0.1090822810734714, 0.28506718362252687, -0.1090822810734714, -1.0284291302737418, -0.8286240775911423, 0.19615965038587807, 0.10141117761114446, 0.28506718362252687, -0.22709187623390137, -0.3556213105624205, 0.19615965038587807, -1.5370096313325536, 1.4582434151719543, -0.6531546704737212, 1.3796716181469966, 1.3387204991091335, -2.3294908816931317], 
             'c': [-2.3294908816931317, -2.3294908816931317, -2.3294908816931317, -0.4967313430769761, 0.7271807447377281, -1.8795065682166356, 0.0, 0.19615965038587807, -0.4967313430769761, -0.3556213105624205, -0.3556213105624205, -0.4967313430769761, 0.10141117761114446, -0.4967313430769761, 0.19615965038587807, 0.19615965038587807, -0.4967313430769761, -1.0284291302737418, -0.8286240775911423, 0.5229938069272871, 0.19615965038587807, -0.22709187623390137, -1.8795065682166356, -0.8286240775911423, -1.2604237977986685, -0.8286240775911423, -1.0284291302737418, -1.2604237977986685], 
             't': [1.6377714565895838, 1.6377714565895838, -0.6531546704737212, 0.3688123010873653, -0.8286240775911423, -0.6531546704737212, 0.5229938069272871, 0.19615965038587807, 0.5943157341374843, 0.7271807447377281, 0.5943157341374843, 0.5229938069272871, -0.3556213105624205, 0.5229938069272871, 0.5229938069272871, 0.5943157341374843, 0.28506718362252687, 0.5943157341374843, 0.5943157341374843, 0.10141117761114446, 0.44796175594274307, -0.22709187623390137, 1.5327561611414895, -0.8286240775911423, 1.1621969436153452, -1.8795065682166356, -1.8795065682166356, 1.6377714565895838], 
             'g': [-2.9869939448090497, -1.2604237977986685, 1.4194923459455895, -1.8795065682166356, -0.6531546704737212, -0.8286240775911423, -0.6531546704737212, -0.22709187623390137, -0.4967313430769761, -0.1090822810734714, -0.6531546704737212, -0.1090822810734714, -0.1090822810734714, -0.1090822810734714, -0.1090822810734714, -0.3556213105624205, -0.1090822810734714, -0.1090822810734714, -0.4967313430769761, -0.6531546704737212, -0.4967313430769761, 0.19615965038587807, -1.0284291302737418, -2.9869939448090497, -0.4967313430769761, -0.8286240775911423, -0.4967313430769761, -1.8795065682166356]}

pwm_pro17 = {'a': [-1.7091922189651259, -1.210750656786959, -1.5675348939417788, 1.0294550840274896, -0.14346739940614797, 1.0069801474571496, 0.2879118002341518, 0.4632431577690334, 0.13048201468403112, 0.13048201468403112, 0.13048201468403112, -0.09404264759091994, -0.19464562453665757, -0.09404264759091994, 0.4298402119698648, 0.13048201468403112, -0.2477063321195173, 0.0, 0.04481812132739147, 0.0, -0.6150315168544132, -0.36006749495514423, -0.6150315168544132, -1.7091922189651259, 1.6961148533941588, -0.14346739940614797, 1.0515852601357145, 1.3303002283467689, -2.4769900439800905], 
             'c': [-1.7091922189651259, -2.0426053214669015, -0.8410005807914696, 0.0, 0.9609518181383797, -0.8410005807914696, -0.09404264759091994, -0.2477063321195173, -0.41970976393289827, -0.14346739940614797, 0.04481812132739147, -0.14346739940614797, 0.08828579009529143, 0.0, -0.14346739940614797, -0.36006749495514423, -0.19464562453665757, -0.14346739940614797, 0.08828579009529143, 0.04481812132739147, 0.13048201468403112, -0.19464562453665757, -0.19464562453665757, -0.8410005807914696, -2.0426053214669015, -1.109057229761569, -0.48192442322188334, -0.8410005807914696, -1.210750656786959], 
             't': [1.6533409458411101, 1.6241038060035249, -0.30279331431772327, -0.5469434099512077, -0.30279331431772327, -0.36006749495514423, 0.1714790664900391, 0.3606206191103988, 0.589619682765654, 0.21134322474768583, 0.0, 0.1714790664900391, 0.13048201468403112, 0.21134322474768583, 0.08828579009529143, -0.14346739940614797, 0.6195567962565799, 0.4632431577690334, 0.3606206191103988, 0.04481812132739147, 0.2501354211817969, 0.04481812132739147, 0.49589018870884216, 1.5326598102714313, -1.5675348939417788, 1.0515852601357145, -0.7616793265169038, -1.109057229761569, 1.681997326277986], 
             'g': [-2.0426053214669015, -2.0426053214669015, 1.1976629386661948, -1.8662884759590337, -1.5675348939417788, -0.6150315168544132, -0.48192442322188334, -1.0140624347879468, -0.6150315168544132, -0.2477063321195173, -0.19464562453665757, 0.04481812132739147, -0.04625518352077599, -0.14346739940614797, -0.5469434099512077, 0.2879118002341518, -0.41970976393289827, -0.48192442322188334, -0.6864929067992099, -0.09404264759091994, 0.08828579009529143, 0.39564551474647375, 0.08828579009529143, -2.0426053214669015, -2.4769900439800905, -0.8410005807914696, -0.6864929067992099, -1.109057229761569, -2.4769900439800905]}

pwm_pro18 = {'a': [-2.7720866324368725, -1.1595062357324748, -2.0184869388883406, 1.1733226633102696, -0.4170799438920379, 1.0387566759348883, 0.7248761006487723, 0.5379518908370993, -0.07432288052660976, 0.20243229218321937, 0.07068086979405949, 0.32315217516557004, -0.4170799438920379, -0.23554618764483193, 0.32315217516557004, -0.4170799438920379, 0.4345459786415287, -0.4170799438920379, 0.32315217516557004, 0.32315217516557004, -0.6247891490715012, 0.4345459786415287, -0.07432288052660976, -0.4170799438920379, -2.7720866324368725, 1.6595249766781857, -0.6247891490715012, 1.2964010211192258, 1.1733226633102696, -0.6247891490715012], 
             'c': [-0.4170799438920379, -2.0184869388883406, -2.0184869388883406, -0.867514920652551, 0.8099766806596423, -2.0184869388883406, -0.6247891490715012, -0.07432288052660976, 0.07068086979405949, -0.6247891490715012, -0.6247891490715012, -0.4170799438920379, 0.07068086979405949, -0.07432288052660976, -0.23554618764483193, 0.32315217516557004, -0.6247891490715012, -0.23554618764483193, -0.6247891490715012, -0.23554618764483193, 0.6344392580560524, -0.23554618764483193, -0.23554618764483193, -0.4170799438920379, -1.1595062357324748, -2.7720866324368725, 0.20243229218321937, -1.1595062357324748, -0.4170799438920379, -2.7720866324368725], 
             't': [1.4633228199494888, 1.6129188419798375, -1.1595062357324748, -1.1595062357324748, 0.20243229218321937, -0.4170799438920379, -0.4170799438920379, -0.07432288052660976, -1.1595062357324748, 0.32315217516557004, 0.4345459786415287, 0.32315217516557004, 0.20243229218321937, 0.5379518908370993, 0.07068086979405949, 0.6344392580560524, 0.5379518908370993, 0.5379518908370993, 0.20243229218321937, -0.23554618764483193, -0.6247891490715012, 0.07068086979405949, -0.07432288052660976, 0.32315217516557004, 1.6129188419798375, -1.1595062357324748, 0.5379518908370993, -0.4170799438920379, -2.0184869388883406, 1.6129188419798375], 
             'g': [-1.5259895069130105, -2.0184869388883406, 1.6129188419798375, -0.4170799438920379, -1.5259895069130105, -0.07432288052660976, -0.07432288052660976, -0.6247891490715012, 0.6344392580560524, -0.07432288052660976, -0.07432288052660976, -0.4170799438920379, 0.07068086979405949, -0.4170799438920379, -0.23554618764483193, -1.1595062357324748, -0.867514920652551, -0.07432288052660976, -0.07432288052660976, 0.07068086979405949, 0.20243229218321937, -0.4170799438920379, 0.32315217516557004, 0.32315217516557004, -1.5259895069130105, -2.0184869388883406, -0.4170799438920379, -1.5259895069130105, -0.4170799438920379, -2.7720866324368725]} 

pwm_pro19 = {'a': [-1.2064508774674263, -1.7369655941662063, -0.5145731728297583, 1.2829339632714987, 0.3025627700204313, 1.0238467419543678, -0.5145731728297583, -0.0489096004809464, -0.8194277543581792, 0.13750352374993502, 0.13750352374993502, -0.0489096004809464, 0.3025627700204313, -0.5145731728297583, -0.8194277543581792, -0.2630344058337938, -0.2630344058337938, 0.13750352374993502, 0.3025627700204313, 0.13750352374993502, -0.8194277543581792, 0.13750352374993502, 0.3025627700204313, -1.7369655941662063, -0.5145731728297583, -1.7369655941662063, 1.6930222465786091, -1.2064508774674263, 1.5025003405291835, 0.925999418556223, -1.7369655941662063], 
             'c': [-1.7369655941662063, -0.8194277543581792, -0.2630344058337938, -0.8194277543581792, 0.925999418556223, -0.8194277543581792, 0.4506614090095652, -0.2630344058337938, 0.13750352374993502, -0.5145731728297583, -0.2630344058337938, -0.2630344058337938, 0.13750352374993502, -0.2630344058337938, 0.3025627700204313, 0.13750352374993502, -0.5145731728297583, -1.7369655941662063, -1.2064508774674263, -0.5145731728297583, -0.5145731728297583, -0.2630344058337938, -0.0489096004809464, -0.0489096004809464, -0.0489096004809464, -1.2064508774674263, -2.584962500721156, -0.8194277543581792, -1.2064508774674263, -0.2630344058337938, -0.5145731728297583], 
             't': [1.5025003405291835, 1.4329594072761063, -0.5145731728297583, -1.7369655941662063, -0.8194277543581792, -1.2064508774674263, 0.4506614090095652, 0.3025627700204313, 0.3025627700204313, 0.5849625007211562, 0.3025627700204313, 0.3025627700204313, 0.3025627700204313, 0.7078192485066896, -0.0489096004809464, 0.13750352374993502, 0.3025627700204313, 0.5849625007211562, 0.4506614090095652, 0.5849625007211562, 0.8210298589546806, -0.2630344058337938, 0.3025627700204313, 0.3025627700204313, 0.13750352374993502, 1.4329594072761063, -1.7369655941662063, 1.2016338611696504, -1.7369655941662063, -0.2630344058337938, 1.4329594072761063], 
             'g': [-1.2064508774674263, -1.2064508774674263, 0.8210298589546806, -0.5145731728297583, -1.7369655941662063, -0.0489096004809464, -0.8194277543581792, -0.0489096004809464, 0.13750352374993502, -0.5145731728297583, -0.2630344058337938, -0.0489096004809464, -1.2064508774674263, -0.2630344058337938, 0.3025627700204313, -0.0489096004809464, 0.3025627700204313, 0.13750352374993502, -0.0489096004809464, -0.5145731728297583, -0.0489096004809464, 0.3025627700204313, -0.8194277543581792, 0.5849625007211562, 0.3025627700204313, -0.8194277543581792, -1.7369655941662063, -0.5145731728297583, -1.2064508774674263, -1.2064508774674263, -1.7369655941662063]} 

pwm_lacI  = {'a': [0.2765858335338852, -1.4499843134764958, -1.4499843134764958, -1.4499843134764958, 1.5370096313325539, -1.4499843134764958, -1.4499843134764958, -1.4499843134764958, 0.2765858335338852], 
             'c': [-1.4499843134764958, -1.4499843134764958, -1.4499843134764958, -1.4499843134764958, -1.4499843134764958, -1.4499843134764958, 1.5370096313325539, -1.4499843134764958, 0.2765858335338852], 
             't': [1.0402782882555777, -1.4499843134764958, 1.5370096313325539, -1.4499843134764958, -1.4499843134764958, -1.4499843134764958, -1.4499843134764958, -1.4499843134764958, -1.4499843134764958], 
             'g': [-1.4499843134764958, 1.5370096313325539, -1.4499843134764958, 1.5370096313325539, -1.4499843134764958, 1.5370096313325539, -1.4499843134764958, 1.5370096313325539, 0.2765858335338852]}


pwm_lacI_o= {'a': [1.0402782882555777, 1.0402782882555777, 0.2765858335338852, 0.2765858335338852, -1.4499843134764958, -1.4499843134764958, -1.4499843134764958, 1.5370096313325539, -1.4499843134764958, -1.4499843134764958, -1.4499843134764958, 0.2765858335338852, 1.0402782882555777, 0.2765858335338852, 1.0402782882555777, 1.0402782882555777, -1.4499843134764958, 1.5370096313325539, 1.5370096313325539, -1.4499843134764958, -1.4499843134764958], 
             'c': [-1.4499843134764958, -1.4499843134764958, 0.2765858335338852, -1.4499843134764958, -1.4499843134764958, -1.4499843134764958, -1.4499843134764958, -1.4499843134764958, -1.4499843134764958, 1.5370096313325539, -1.4499843134764958, 0.2765858335338852, -1.4499843134764958, -1.4499843134764958, 0.2765858335338852, -1.4499843134764958, 1.5370096313325539, -1.4499843134764958, -1.4499843134764958, 0.2765858335338852, 0.2765858335338852], 
             't': [-1.4499843134764958, -1.4499843134764958, 0.2765858335338852, 1.0402782882555777, -1.4499843134764958, 1.5370096313325539, -1.4499843134764958, -1.4499843134764958, -1.4499843134764958, -1.4499843134764958, -1.4499843134764958, -1.4499843134764958, -1.4499843134764958, 1.0402782882555777, -1.4499843134764958, -1.4499843134764958, -1.4499843134764958, -1.4499843134764958, -1.4499843134764958, 1.0402782882555777, 1.0402782882555777], 
             'g': [0.2765858335338852, 0.2765858335338852, -1.4499843134764958, -1.4499843134764958, 1.5370096313325539, -1.4499843134764958, 1.5370096313325539, -1.4499843134764958, 1.5370096313325539, -1.4499843134764958, 1.5370096313325539, 0.2765858335338852, 0.2765858335338852, -1.4499843134764958, -1.4499843134764958, 0.2765858335338852, -1.4499843134764958, -1.4499843134764958, -1.4499843134764958, -1.4499843134764958, -1.4499843134764958]}

pwm_35    = {'a': [-1.7357363914465747, -1.5979229552856256, -1.413126577111018, 1.0848097027780488, -0.17276952242946456, 1.1449503940384098], 
             'c': [-1.5336578941015893, -2.2517714773068596, -1.249335777934012, -0.41176410385678575, 0.96758532537598, -1.249335777934012], 
             't': [1.6319111539406774, 1.6868899609626944, -0.47071453694712506, -0.3831682493561359, -0.32762275640492217, -0.5321767624436156], 
             'g': [-1.9708034298766062, -2.058517088895277, 1.3116507628376781, -1.4721338637045378, -1.4721338637045378, -0.5639185196931832]}

pwm_10    = {'a': [-2.058517088895277, 1.6868899609626944, -0.41176410385678575, 1.2940516426365727, 1.2851709143365382, -2.1519108061484826], 
             'c': [-1.3564381974154478, -2.058517088895277, -0.8862249900135163, -0.8466454882121791, -0.6983672583037123, -1.413126577111018], 
             't': [1.6107416625771427, -1.5336578941015893, 1.0745379200025795, -1.0119278937414655, -1.249335777934012, 1.6801311020420377], 
             'g': [-1.665184720179913, -2.359061769459582, -0.7340326964474218, -1.0119278937414655, -0.9269210362459909, -2.359061769459582]}



pwm_cdsNT = {'a': [1.2931246638130196, -3.9053723674528062, -4.2418446040740188, 0.68926636648294337, 0.39997889956210764, 0.29147147814608854, 0.53783895626021516, 0.54063459688448257, 0.23624949934609618, 0.35730750958850926, 0.22865067858747062, 0.26901490244283083, 0.36598869933355582, 0.21172719776295823, 0.10196081777966468, 0.27485860059174194, 0.11742504347724628, 0.018014396625654964, 0.1435098206925372, 0.087132809510047121, -0.044141528864765245, 0.1418473099189238, 0.091516858618581387, -0.053200473553517133, 0.073864149562213932, 0.018955573165718716, -0.14085549913324985, 0.037595441824761384, -0.0058075969467018861, -0.20465845569186703, -0.020378034412579404, -0.015497595247670977, -0.20819411052417477, -0.045144035214390851, -0.051180270846241216, -0.22007073468675384, -0.0029188130408108583, -0.029223300927545909, -0.24793443917368888, -0.018422999576776122, -0.052189862047593558, -0.25039446501455115, -0.025282409127669249, -0.025282409127669249, -0.23330003165525104, -0.026266177037801965, -0.031199586155757804, -0.2931682809978377, 0.019895864725360448, -0.038147504924554695, -0.25905252775766585, -0.014524359161118713, -0.00099758286291693615, -0.27281134392909356, -0.021356987011563671, -0.0038808140770018912, -0.31526144731454331, -0.064385135141411864, -0.0058075969467018861, -0.24059046491793035, -0.041140025861008622, 0.0076025657007218776, -0.25657113690628036, -0.072598733678800639, 0.057705808775624097, -0.30220643161289962, -0.0087047501078547848, 0.099360036079607403, -0.26029553599726279, -0.068483501533694077, 0.095010311953141496, -0.26528307750830182, 0.010452923925078506, 0.10541803816352255, -0.24303246857348199, 0.0095037069577461868, 0.10628047892418115, -0.26528307750830182, 0.073864149562213932, 0.14848083341455764, -0.23572427526675746, 0.0056978032200679946, 0.16080131780259818, -0.27029561933184609, -0.0087047501078547848, 0.095881771703282506, -0.33516920497246833, -0.038147504924554695, 0.15671133255107303, -0.27281134392909356],
             'c': [-4.3428402066471445, -4.4169481788008662, -3.8464033203332533, -0.46422626335012801, 0.11233730966235246, -0.25926774140695485, -0.17506817587022644, -0.26772700635293128, -0.29728580859447562, -0.057285140213843101, -0.16625754618807156, -0.17506817587022644, -0.12754303400738112, -0.11913962321100166, -0.12018619578167272, 0.008358964231477797, -0.13177137011690221, -0.1618811715882727, -0.004616194631655678, -0.11288308559669653, -0.0027522611935929266, -0.014930397648419788, -0.14349233541505915, 0.032916815013141795, -0.0036837936317044777, -0.081166872217230401, 0.008358964231477797, -0.013988334460518753, -0.06716664354384079, 0.046303895795601221, 0.013868620042447334, -0.074142257280265869, 0.020258418141218412, -0.0018215957006398366, -0.077146766300564676, 0.035608606678853183, -0.074142257280265869, -0.093325076697040016, -0.0064836088064510571, -0.022499024128427515, -0.048474510531688088, 0.051608948025294539, -0.059253644786515285, -0.056302339151934971, 0.060388635677340194, -0.049449644689894517, -0.03300031394909074, 0.060388635677340194, -0.10460146476497441, -0.004616194631655678, 0.012035438960786536, -0.068160185602718484, -0.090271639210149579, 0.050726724765603345, -0.017761923844158308, -0.066174087631089021, 0.073415307077348738, -0.03300031394909074, -0.042643590220894957, 0.048959939853717438, -0.10460146476497441, -0.004616194631655678, 0.021167922524058878, -0.0622136864149921, -0.028213325391866207, 0.021167922524058878, -0.058268908123975761, -0.013988334460518753, 0.011117586670557487, -0.048474510531688088, -0.046527090247292575, 3.7140893985717424e-05, -0.05140277031077653, -0.054339629984086209, -0.0092912849606496262, -0.058268908123975761, -0.090271639210149579, 0.047190027887259164, -0.069154715769226896, -0.079154799103810292, 0.069091910805641879, -0.057285140213843101, -0.10563292437163684, 0.041861418476040177, -0.071146748300467549, -0.082174428977530231, 0.032017938548124736, -0.055320503039678184, -0.10254173180196391, 0.018436924012827247],
             't': [-2.4390352986593791, 1.3917538137250773, -3.9053723674528062, -0.50735463870803044, -0.30480383567058522, 0.24228725353701616, -0.54632060724141429, 0.032039871980159534, 0.15424928781129804, -0.1486117707046089, 0.34651846359769112, 0.16812139928910405, -0.24548045021212209, 0.34312287459655288, 0.26754862652030359, -0.24181072132315981, 0.40126342125446435, 0.26608019747523692, -0.27786185971516209, 0.3559652275077797, 0.20628183230438621, -0.29445445480858168, 0.3308023902085121, 0.16487464319023404, -0.37064359316612816, 0.32180890171113868, 0.1418473099189238, -0.33919876045847003, 0.32596979537030341, 0.11571855842148802, -0.35685027103379235, 0.3613235792433992, 0.076532003523406555, -0.37621463821558371, 0.32735292145525469, 0.12844677438144159, -0.32450243716827315, 0.36265869292636849, 0.10972282311515402, -0.3486646864473531, 0.32319779082329286, 0.064020669634298574, -0.29188375930548094, 0.29860926719438108, 0.082729455851777156, -0.31789302778059925, 0.30992480518695698, 0.12591405880215747, -0.33919876045847003, 0.29718577940952717, 0.1493069383768629, -0.34324461897801378, 0.29789777659161704, 0.13684312933434775, -0.38886413927965641, 0.29932025193815986, 0.093265110812110891, -0.3418941798801422, 0.27121029300626659, 0.084493124739273825, -0.37761226248222146, 0.26239966332411169, 0.10022771509282985, -0.36925566789128017, 0.27631420492444247, 0.14848083341455764, -0.38886413927965641, 0.23624949934609618, 0.10886334734243515, -0.41901717745034406, 0.23927293324409335, 0.099360036079607403, -0.3790118428366448, 0.21637116895740882, 0.097622416181066665, -0.4175605129538798, 0.22099367333627615, 0.092391366763513907, -0.45311981499036658, 0.19845093872383823, 0.072973280906412613, -0.42633249902671683, 0.20159065872850604, 0.15424928781129804, -0.33785377034313735, 0.26901490244283083, 0.13097309151455275, -0.38603927864410165, 0.22712396073367078, 0.13097309151455275],
             'g': [-1.1707565432857026, -4.5840022634640327, 1.356408195094162, -0.22845961766462325, -0.41663256622704192, -0.4539396186398526, -0.12965496721052469, -0.67562224931438741, -0.17728301619977935, -0.25686389409556032, -0.68663153482275674, -0.37930964407306639, -0.10254173180196391, -0.71849927367077926, -0.33941073489514684, -0.11288308559669653, -0.64507180511596196, -0.17839227865406512, 0.086274464125638828, -0.50338789405383377, -0.19518058565732202, 0.10817929951368875, -0.41381962485042723, -0.17065315766110967, 0.20651520023455047, -0.36851331788284353, -0.029168891637534763, 0.22744272034050639, -0.36049188449826824, 0.012952449570667665, 0.25946874705991479, -0.40821736930175734, 0.081150627125769301, 0.2987996591223383, -0.2910552588438397, 0.022076600460277061, 0.29465886645630696, -0.36583235112958568, 0.10149031136289195, 0.28143208121443342, -0.31876484027159979, 0.09306566170364057, 0.28283264166746447, -0.2985365904961283, 0.054250957488133168, 0.29050085630764333, -0.3420217024358671, 0.052490393653099918, 0.30634686475772133, -0.34857910298202638, 0.051608948025294539, 0.30839534618419379, -0.28609861920391139, 0.03650426280679777, 0.30017612183106179, -0.31494074383319659, 0.087125890315856339, 0.31722392644839681, -0.29354282231564127, 0.069091910805641879, 0.36668999466518976, -0.34726417840071711, 0.091372181197307459, 0.35569020727619283, -0.412416115848107, 0.073415307077348738, 0.31992480587552918, -0.42369973345013423, 0.094756279181547901, 0.36668999466518976, -0.37524735006418763, 0.11730420729068929, 0.2967314060582793, -0.34071536652181178, 0.11233730966235246, 0.32059888746492277, -0.30355542160807103, 0.080294096024152994, 0.2967314060582793, -0.34463950497794599, 0.056886005126138242, 0.32664526127678734, -0.33550702141467353, 0.024797690574637685, 0.30360901226038278, -0.38202703704956625, 0.10232888583551313, 0.33664201230549834, -0.37659961531420116, 0.07427774783800728]}



if __name__ == '__main__':
    pass