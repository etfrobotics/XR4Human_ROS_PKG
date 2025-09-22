import panda_api_ETF 
import rospy


P1_approach = [0.3144449073430269, -0.4264672808019738, -0.5114057854016621, -1.5156120447861519, 1.4723156284233134, 1.3169313412374921, 1.2237294479790772]
P1_1J = [-0.021016863280227133, -0.9443380888052337, 0.09212402341953296, -1.6996689351567051, 1.3524237293799637, 1.399391212211715, 1.6049285095847312]
P1_1C = [0.057283390499552285, 0.16544925039025868, 0.9425663516477191, -0.7529046961166552, 0.32233536474108787, 0.22197944124720867, 0.5291120475535348]
P1_1J = [0.05319557378197141, -0.6948883837315074, 0.07830056247817342, -1.6256076213280664, 1.3085981365467874, 1.485448397972129, 1.4246732332226304]
P1_2C = [0.18412423987739673, 0.1627028108956406, 0.940669932385807, -0.7508152550849544, 0.29883472845974196, 0.2306150665909908, 0.5420248600012181]
P1_3J = [0.04624657932760422, -0.4121132577920363, 0.07421909308762056, -1.442704312959085, 1.294996208994535, 1.5214539493587282, 1.3482792156851953]
P1_3C = [0.30659162713970595, 0.16099793398491258, 0.9365824708175836, -0.7409153726380816, 0.3076032578557206, 0.23578540248708846 ,0.5484796170498238]
P1_4J = [0.04781025308901172, -0.050432667163363906, 0.07049716959866571, -1.0762542180178625, 1.2623749376449969, 1.535777007487085, 1.3100119322455592]
P1_4C = [0.4257616502346532, 0.15829285495677636, 0.9370305968164072, -0.742305210618753, 0.29910931450019945, 0.21584058702375955, 0.5594009592954846]

P2_approach = [-0.19326919144302493, -0.3034370598948813, -0.382058112377959, -1.7024528335604752, 1.0036262299273127, 1.0710453125884543, 0.6819882715720331]
P2_1J = [-0.37818241163837696, -1.4413555650711058, 0.2838976311053383, -2.754026668648971, 1.58854045508988, 1.2472807865805096, 0.9558830108976464]
P2_1C = [0.1615669198491864, 0.16737747217325505, 0.5993893469119888, -0.7483490289491765, 0.3193641615870873, 0.22581046303824634, 0.5357143809410513]
P2_2J = [-0.0026134987551915093, -0.9042626239249579, 0.1893694844643275, -2.5432579126718093, 1.3700495365063312, 1.7190456499126223, 0.7247741693175748]
P2_2C = [0.2780343569148858, 0.16570663535067176, 0.6046678095763548, -0.7600457338932972, 0.31124274231732363, 0.20232641785052718, 0.5334064663885928]
P2_3J = [-0.04634095913328622, -0.500298146799991, 0.19197879956479655, -2.2706039340717976, 1.3517417563993777, 1.7451742865008535, 0.6226000255263514]
P2_3C = [0.39803535590524136, 0.16295725329294883, 0.6021253072721556, -0.7528065960682574, 0.31516369790479953, 0.21722605944435364, 0.535506219886729]
P2_4J = [-0.04588454488704078, -0.11879301164338461, 0.17253295489544793, -1.9322555725277557, 1.3506558810472489, 1.7432673245105479, 0.5666096872008509]
P2_4C = [0.5188410547734816, 0.1597076050548163, 0.5971887300296507, -0.7387668172415218, 0.2985124051210677, 0.22991248550929427, 0.5587970854779093]
P2_5J = [-0.014213539050597869, 0.2301830812629901, 0.1574471423798379, -1.4966378166045344, 1.223055840630688, 1.7933451030637386, 0.6906833316798584]
P2_5C = [0.631465197775872, 0.15937651599458316, 0.6025302089017807, -0.7481899353650718, 0.32369902472557127, 0.20903901094917698, 0.5401235543017109]

P3_approach = [0.5466557320837387, -0.47780395999258407, -0.7791358385420682, -2.5830599661572213, 0.700608902959995, 1.994127100057072, 0.24255214770706235]
P3_1J = [0.012705621521587053, -0.6234902446897407, 0.5746509715716099, -3.0548351944036645, 1.8027292547088067, 1.9786604989998868, 0.010825228235787816]
P3_1C = [0.22827322273334974, 0.17592480453055587, 0.2759337122929782, -0.791656326192993, 0.3287755219350638, 0.2075565084858189, 0.4712825194722545]
P3_2J = [-0.21959418161500965, -0.20370600153718896, 0.5740075902771532, -2.706895165895161, 1.570738256219238, 2.0711673670444224, -0.046418119159479854]
P3_2C = [0.3488312254422869, 0.17421168619512867, 0.27894099649390547, -0.7959185073885473, 0.3326046947978658, 0.2072459915961018, 0.4614509134915155]
P3_3J = [-0.2724423179668292, 0.18462566918522944, 0.498087084627988, -2.3773784849742565, 1.5147258359157436, 2.0501359364820853, -0.15439708154234622]
P3_3C = [0.4627326180552287, 0.16514375708016388, 0.2598678600522547, -0.7527480295176544, 0.3129202040142745, 0.21337209937622253, 0.5384456306673279]
P3_4J = [-0.25126360089737093, 0.4945476175525732, 0.4655171341207565, -1.9514455776609123, 1.2837263456507233, 2.0998405199620245, 0.05284365048193428]
P3_4C = [0.5907301530165354, 0.16204957573752965, 0.2609476474938284, -0.7565778223245718, 0.31921174695345267, 0.21819407523670525, 0.5273378470251613]

Handling_J =  [0.18471083331944646, 0.43472414678021476, -0.7240435380024176, -2.2398730750378975, 2.7865273981516996, 2.5375278862809227, 0.5124577455517487]
Handling_C = [0.44168590135055885, -0.28202591464998605, 0.20874092986163167, 0.17046152151228713, 0.8333672430863134, -0.10688834860119495, 0.5147978134838401]

def GoForBIN(P_appraoch, P_C, dxa=0, dya=0, dza=0):
    pandica.set_joints(P_appraoch[0],P_appraoch[1],P_appraoch[2],P_appraoch[3],P_appraoch[4],P_appraoch[5],P_appraoch[6])
    pandica.move_robot_L_absolute(P_C[0:3],panda_api_ETF.euler_from_quaternion(P_C[3:]),dx=dxa,dy=dya,dz=dza)
    pandica.move_robot_L_absolute(P_C[0:3],panda_api_ETF.euler_from_quaternion(P_C[3:]))
    pandica.grasp_client(0.00,0.005,0.005,0.25,10)
    pandica.move_robot_L_absolute(P_C[0:3],panda_api_ETF.euler_from_quaternion(P_C[3:]),dx=0,dy=0,dz=dza)
    pandica.move_robot_L_absolute(P_C[0:3],panda_api_ETF.euler_from_quaternion(P_C[3:]),dx=0,dy=dya,dz=dza)
    pandica.set_joints(P_appraoch[0],P_appraoch[1],P_appraoch[2],P_appraoch[3],P_appraoch[4],P_appraoch[5],P_appraoch[6])

def PutBackBin(P_appraoch, P_C, dxa=0, dya=0, dza=0):
    pandica.set_joints(P_appraoch[0],P_appraoch[1],P_appraoch[2],P_appraoch[3],P_appraoch[4],P_appraoch[5],P_appraoch[6])
    pandica.move_robot_L_absolute(P_C[0:3],panda_api_ETF.euler_from_quaternion(P_C[3:]),dx=0,dy=dya,dz=dza)
    pandica.move_robot_L_absolute(P_C[0:3],panda_api_ETF.euler_from_quaternion(P_C[3:]),dx=0,dy=0,dz=dza)
    pandica.move_robot_L_absolute(P_C[0:3],panda_api_ETF.euler_from_quaternion(P_C[3:]))
    pandica.grasp_client_variable(0.05,0.05)
    pandica.move_robot_L_absolute(P_C[0:3],panda_api_ETF.euler_from_quaternion(P_C[3:]),dx=dxa,dy=dya,dz=dza)
    pandica.set_joints(P_appraoch[0],P_appraoch[1],P_appraoch[2],P_appraoch[3],P_appraoch[4],P_appraoch[5],P_appraoch[6])



def toWorker(P_appraoch,Handling):
    pandica.set_joints(P_appraoch[0],P_appraoch[1],P_appraoch[2],P_appraoch[3],P_appraoch[4],P_appraoch[5],P_appraoch[6])
    pandica.set_joints(Handling[0],Handling[1],Handling[2],Handling[3],Handling[4],Handling[5],Handling[6])

def fromWorker(P_appraoch):
    pandica.set_joints(P_appraoch[0],P_appraoch[1],P_appraoch[2],P_appraoch[3],P_appraoch[4],P_appraoch[5],P_appraoch[6])

if __name__ == '__main__':
    try:
        pandica = panda_api_ETF.robot_dealerNODE()          #Init robot object
        
        pandica.grasp_client_variable(0.05,0.05)            #Move gripper

        #Pick bin 1_1
        GoForBIN(P1_approach,P1_1C,0,-0.1,0.1)

        pandica.set_joints(P2_approach[0],P2_approach[1],P2_approach[2],P2_approach[3],P2_approach[4],P2_approach[5],P2_approach[6])
        pandica.set_joints(P3_approach[0],P3_approach[1],P3_approach[2],P3_approach[3],P3_approach[4],P3_approach[5],P3_approach[6])
        pandica.set_joints(Handling_J[0],Handling_J[1],Handling_J[2],Handling_J[3],Handling_J[4],Handling_J[5],Handling_J[6])
        pandica.set_joints(P3_approach[0],P3_approach[1],P3_approach[2],P3_approach[3],P3_approach[4],P3_approach[5],P3_approach[6])
        pandica.set_joints(P2_approach[0],P2_approach[1],P2_approach[2],P2_approach[3],P2_approach[4],P2_approach[5],P2_approach[6])

        PutBackBin(P1_approach,P1_1C,0,-0.1,0.1)

        #Pick bin 1_2
        #GoForBIN(P1_approach, P1_2C,0,-0.05,0.05)
        #PutBackBin(P1_approach,P1_2C,0,-0.05,0.05)

        #Pick bin 1_3
        #GoForBIN(P1_approach, P1_3C,0,-0.05,0.05)
        #PutBackBin(P1_approach,P1_3C,0,-0.05,0.05)

        #Pick bin 1_4
        #GoForBIN(P1_approach, P1_4C,0,-0.025,0.025)
        #PutBackBin(P1_approach,P1_4C,0,-0.025,0.025)

        #Pick bin 2_1
        GoForBIN(P2_approach,P2_1C,0,-0.05,0.05)

        pandica.set_joints(P3_approach[0],P3_approach[1],P3_approach[2],P3_approach[3],P3_approach[4],P3_approach[5],P3_approach[6])
        pandica.set_joints(Handling_J[0],Handling_J[1],Handling_J[2],Handling_J[3],Handling_J[4],Handling_J[5],Handling_J[6])
        pandica.set_joints(P3_approach[0],P3_approach[1],P3_approach[2],P3_approach[3],P3_approach[4],P3_approach[5],P3_approach[6])

        PutBackBin(P2_approach,P2_1C,0,-0.05,0.05)

        #Pick bin 2_2
        #GoForBIN(P2_approach,P2_2C,0,-0.05,0.05)
        #PutBackBin(P2_approach,P2_2C,0,-0.05,0.05)

        #Pick bin 2_3
        #GoForBIN(P2_approach,P2_3C,0,-0.05,0.05)
        #PutBackBin(P2_approach,P2_3C,0,-0.05,0.05)

        #Pick bin 2_4
        #GoForBIN(P2_approach,P2_4C,0,-0.05,0.05)
        #PutBackBin(P2_approach,P2_4C,0,-0.05,0.05)

        #Pick bin 2_5
        #GoForBIN(P2_approach,P2_5C,0,-0.05,0.05)
        #PutBackBin(P2_approach,P2_5C,0,-0.05,0.05)
        
        #Pick bin 3_1
        #GoForBIN(P3_approach,P3_1C,0,-0.05,0.05)
        #PutBackBin(P3_approach,P3_1C,0,-0.05,0.05)

        #Pick bin 3_2
        GoForBIN(P3_approach,P3_2C,0,-0.05,0.05)
        pandica.set_joints(Handling_J[0],Handling_J[1],Handling_J[2],Handling_J[3],Handling_J[4],Handling_J[5],Handling_J[6])
        PutBackBin(P3_approach,P3_2C,0,-0.05,0.05)

        #Pick bin 3_3
        #GoForBIN(P3_approach,P3_3C,0,-0.05,0.05)
        #PutBackBin(P3_approach,P3_3C,0,-0.05,0.05)

        #Pick bin 3_4
        #GoForBIN(P3_approach,P3_4C,0,-0.05,0.05)
        #PutBackBin(P3_approach,P3_4C,0,-0.05,0.05)


    except rospy.ROSInterruptException:
        print("program interrupted before completion")
