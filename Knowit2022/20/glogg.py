gloggPoints = set()
from matplotlib import pyplot as plt

moveDict = {
    "n": [0,1],
    "v": [-1, 0],
    "s": [0, -1],
    "e": [1, 0]
}

class Elf:
    pos = None
    path: str = None
    count = -1
    points = None

    def __init__(self, start_pos, path):
        self.pos = start_pos
        self.path = path
        self.points = [[self.pos[0]], [self.pos[1]]]
    
    def move(self):
        nextDir = self.path[self.count] 
        moveVec = moveDict[nextDir]

        if not self.canMove():
            return

        self.pos[0] += moveVec[0] 
        self.pos[1] += moveVec[1] 
        self.points[0].append(self.pos[0])
        self.points[1].append(self.pos[1])
        
        self.count += 1
        
        if self.canMove() and self.path[self.count] == 'g':
            gloggPoints.add((self.pos[0], self.pos[1]))
            self.count += 1
        

    def canMove(self):
        return self.count <= (len(self.path) - 1)

elf_1 = Elf([0,0], "nngeesvvseennnnvssesvnennneesvvsegnvsvvnesesssvvneesvnesenenvngnvnnessvsssseeeeennvnnvngnvneenenvnennnesssvvsvgnvsegneessvsvvvgnennesgvseseneeseenneeseneeenneeeessvsegsenvgvvneenneeesvnnnneseessgeegngenvsgenvsgessvgsvsvgvvvsvsgeennnvsvvgnneenvvsesseneesegesgenenessssenenvneseeenvvvssvsvnneneessvnvseessvnvnenenvnnvsssvvgnvsegnvneseseneneesvnvsvsenesvsvnnneesvssssvvnennvsseseneesvvvvsvsssenvnneeeesgvssenennenvsessvvvnneessseeeeenenngvnvvsgenesvvgnvsegsvnegseeseegnesenennvneeegnvsegnneessenvssvsesvnnnvgnnesvvssvneegnnennessseseseeessvnennnnvvssesseneeennnesseseesvsgsvgnvvssenneegsegnvgnvvgvvsssenvseeeenegnvgnennvssvnesvvgneneennvnnesgsennnngesesvsegsseenessvsvgsvsgvvvnnvsenesvsvgvvvsvsenvnvsvgsvvvvngnvssvnennessgenvnenneeenegnvssvngnnvngeennvvnnnvngvvvgneegsseeenneseesvgnneesssvnvgvnvnngvvssgvvnnesgsegsssvnenvnngeesvgsesvsvsvvssvnesvvsvvnvnnvsvnvnvvnesvnvnnvvvnneessssvnnvnvvvvvvnnvvneesvsvnnnennnnnvvnvnngeegesennnnnenesegneeneeneennvvvnnnenvneeesessessenvvvnvneneesesssvssvnnvvneeeeennngvnesgsssvsvvssenennvnnennnnnnvgvsvsenegngeengvnnnvvnegsennnnvvgvneegngnnvngvsgsvssvnngneneegneeesvnnvvnvgsvvvnngvnvgnnesvvvvnnnvseesesvnenvvnvvsvsvsessssvsennvvnvvvnnnenngngeennnneeesesesenengvvvnvssvvsvneeesesesvnenvnnnvsessvvvvnneeenesesesssvnvssennvneneengnnnvnnegengnvnvsvvngvsvsseeesgeeegegesvssvsvgvvvssesvvnnennesenvvneenneegegnennneneneennngnngnngvseeseesgessenesvnnnngengnesesvvsenesvvnngeeennvsvneeeeenvgssssseenvvsvsssvnenvsssvneesenvssvvssesvvnvsssegennvvvvsvvneenneseesvneennvnessvnesegeeeenneseenenvgvgsvsssesvseeennvnnnngvgvvneneeegesseegeesenvvseessvsvnnvsvvsvvnneneseenesvnngnnnnvvgvngnnvnnnessvnvsgenennvvsenneeesgesessenenenvngvvssesesvvnvnvsvnengennenegeneseneeessesennnegsvnvvvvseneeeegssgesvngvseesvnngneneesesvvgnenesvnesesgseneesvvsesgvnesgeesvvsvvvsgssenenesesvvsseennvsvsvsegsssvvnngeesvsssengesvngvnvsvsegsvssgvnvsvsgvgnesgessenenvsvssegennvvnnvsgvgvgsengegenvsgvgssvgsenvgssvvssvvvsgsessvsegsvnegennvvnvssessssesegenvvvvgnnngvngvgvnesgvsesesgesgseesgeenvgvsgsvnvgseengvnnnvvgvsvvgssengvvgsvsvnvvgvsesvvsgvnenvnneenvnvvvvgneennneneneesesenenegneeeseseesvnvssgvgvssvngesesegnnngenenennvvvsssvvvnnnngeneeenesenvssgeesvsvgnngeenenvssvnesenesvvssssvssgsenneeegenvnvvvsssssvvvsgsvnegeenessgvneenessvnneeenegeenvsenvneenvvssvnnnvnegnnvvvsvvsennnnvvnnvnvvvvsenesvvvnenngvnvssseneeessenvnnnegnvvnnvsvvvvvsvsesegeessvnesvnvvvnessvgsseeneseesengvnnnvsvssvnvsessssvnnnenvsvseneneeessesseenvssessvvvvsenvsenvseenesgsvnnvsvsvvvnenvnvvgneeeeegnvsssvsennnnneegnesesssssgsessgsvnvvnvseeenesgvvneesgssesgesvsssvsvssenvvsvgnvvnnvsvnvseeeseenegesenessvssssvvnenvvvgnngegseessvssvvvvvnesesssgsssgsenengnnesgengegsvvgsvgvnvngvvsssvvssssegsvvgsseeneenvvsssegseeeesvnngvnnvvvsssvgvsengvnnvvnnesvneegnvvneenneeseenvsssenvvnese")
elf_2 = Elf([0,99], "ssegsennnvgvssegeseenvvnenessvvsssvssvngeeneeeegsvvsvssesvneseennvssvsseeesvsvvvsssgsvsvsvnennneenvvvsesesssvnnnvnennnneneneeneesvvsvseesessenvnnnnnvneenvvnegeesegseseesegsvvnesvvvnnvnengnnnvvssvgnvgvnvsesessenngvsvnvsvnnnvsvnvnnegseenennvvsvngvseenvgvssssesvgnenvsesvgneesesenvsennnvsenvneeesssgeeeeeegessvnngngegegenvvgnnnesvvvsseegesgesvngesvsesvvvvsenesvneeeesseessssseesenvsssesvvsvneneeengvneeeenvsvssvvnvseengvssvnvnngeesssvvnvvvseenvnnennnengvsvsgeneenvgngvnesgesengvvgsgesvsvnvsgsvseeegsssenenvnesvvvvnvvvvssvsssgvvngeeenvsvnvnvvsssvvvgnvvgssvnvnnvgneneneeeennnvsesvsesvnesssvnvsgeeesseegsssvneenvngvnvvnvnvnvnnesvvssvnnvsenvnennnvnneesssvvnnnnesssvnesvnnenvsennvngeessvnnvgngneeesvseneneennvnenvssesvseegnenvssgvsgesgeessesseesvvsesvnvsenvsvnngvvnvvvnesvnvseeeessennvnesvnesvvnnvvnnvvsvngeeeesssseenvvsessvnvnvvvsennneneessvnvssvnvssssesvneenvsenvvssesvnnnesvsseneenvvnvnnenneeeennnegsvvnvnvnvsvsgsgssesessseneeeeegeseesvneeesvssessssvneeennnvnngnnngvvsesvnnneesgessssesvneesesvvvnvnenvgnvsvvnvvnnvvnennvngneeessgennegeengvgsesesvnennenvnneeseesgsvvsvssesgvvsgseneenengnenesseenvvvvvvsenvsvneseegegsvngegsvvnegnneneesvvvnngvgnnesvsgvnnvneseesenvvnvvsvvvnvvsvseenvssvvvvnnneeeesenvssenneeesesesegsessvvvnvsssenesgssgeegsgessvnvvnvnvssegsssssssvnnvsseeseneessseenvneenvgvgvsesvsseennnvvvsvnvnvnnnneseenvnngesvvsssvvvsvnnennnvnnnenvnnvssenneessegnneneenvssvssesgseegssenvsssgvsvsssssenvvsesvvnvsvvgvsssgvnenvnvssesssvsennnvssssgeeegeenvngnesgegnvnenesesseesgesvngenvneegsgsvnegessssvnennvsvvvnnnvssgeegnvnvsenessgvnesgvsssenvnvssgsvvvnesvnvvsegenvnnvgvvnvnnnnenvvvnvnvngeseneseenngvnvnnvnnvneessesssvnenneeesvsvngnenvvvvnvvvnvvnvnvneeeesennnessseennnvsvvvseeessegesvssseenvnessesenvvsgvvvnvvvsesenessssvnvnennnvssvsgssgvvnegesgvngnngvseegesvvgvnvnnnvsssgeenvvnessenvsenvvneeeesvgsvssengvvvngesvsenvngneennvvsseeegssgsvnvnennvnennnesesvvvvsennvnnnnnnessssvnesesvnessenvnnnnnenvnnnneeneesvseenvsvvvsenenenvssenvsvvvvngeennvvgvsesgenvvssseesvvgnnessvgnnnnnegeeessssssseenvnvvsesssseeeennnvsvsessvsessesvneenvssvsvsvvsgvvvssvneesengvsvvsseegegsvvnvsseenesvnesesgeesgvssesenesgsssgvgvnnvgnneeeeennvvnennnnvsssgssseenvnvvvnnnnvngesvngnvsgvngvsessgsvsvsgseeessennneesvgvnvgsenvgvvsseneesvnennneeenvvvgssenvngeesvnnesvvgnngnnvgvngvnvnnvnnesvnnnneennnvnvgsgesvngeesvvsseennvvseseeeseenenesennegnnnvnvvvvvnnesennvvsvseeneesennvvvvvvseenvvvgvsengesenesesvssvnvvvseesenennvvvgnngvsssseseeeeegengvsgsvvvsesvsesssssenvneseessvnessvsenenvssvnvnvnnessvsvsgvvnesegeesssgssgvnngnvgvvnneegesgenvnnvsvvvseeegssgsegsvvsgvvsssegnessenvnenvvsenvnegnenegegssgvsssgesvsessvvngennenenvnngneessssessssgsvssgvvvvsesssegssesessvvvvnnenvvvsegnvsssvssssgeesssvvssgeenvsvgsesgsvnegeenesvsvsvvnnegeeneneessvnnennvnvnegsvsssessenenvssvv")
elf_3 = Elf([99,0], "nvnnvnnnvgseeegnvnegsvnegsvsssesvssvvvnnnvgsgvvsseenvgvvseeenesenennnvsvsssenesvvneeennvvsgvsvvgvvnnnvnvnnneeeneeennesvnenenngvnesgenvvvsvgnnvsvnnnvgvgnvvvseenvseegsvseeneessesgeesengvssvneessssvvneseeegsvnvssessegnngvsesgssssvnesvvvvnnnvvsegsgvvsseeennegenessvsvnngenvvssengnesesvsvnvvngennenngenvvnnnneenvvvvsseeeenvsvsessvvsssennegeesssesvsvsennvsseenvnvnvvssvvgvsvvvgnvnneeeneeesgvnesgvnesgeesgvvgsvgsenngngeennngnnvvnnngnvsegssvsvseessvgvnnnvnengvsvvsseenvvsssesssgvvsvvnngvnvgsvsvsvvnnvsssvnnneesvvsvnnneeessenneseeeneesvgvvssgseeenesegeenneesgvnnenngvvsvnesvsesenvnvnvsvnngnenvseneennegenegsesseennengngvvssenegengvgsgsenngnvsgsgvseenvgvssenngvnvssvneeegsesgsvsegnvssssengvvvssvvgsgsvgsenvgnegeseesvneesenvnnvnvnngeenegnvvvnesvsvnnesvvvsssgsesgsgeegseesenvnnesvvnnesesvnnnegnvnnvssseegnngnvssesgvnvvgvvvnennesenvsvnvsenvsssessessvgvsgvvsvvgneeenvsvngeneeegsgsesvnenvgvsgvnvnnennvsesvnesssvvgnnnvvvngnnnneegnnvsesgeesvneseesvnngnnvvgvvnneeesesssgssesssgvvnvsennennesvvvnvvsssgsvngegnvnnnvnesvvnvgvvsenvnnvsvvsvnesenvssvssssessesvvsvvnvsvvnengvneessvngneneneeeesvsssvsvnvneeesessvvsenenvsesvvnvvvvnenvngnvsegnvnenesvseeeeenvsenesvvssvneseneesseseegeneenvgnesseessgeneeegeesvvngvseenennnnvvgsvnegenesvssgsgssvvnnneegessesvnvseneesvnesennnnessssvnnvvgsvvvgnvsvvseeengvnnneeenesesvneenegssvnvnvsessseesvvvnngvvgseeeeesvnvvngeennvnesesvvsvgvnvgsgvvnvnvnvvngesvngnesssvvnesvssvvnvngnesvgnvgnvvvssesvsvnesvvsvvnenvneseeeenenegesgvsengvngnvvneeegsssgssennnessgsvnvvssegsvgnegenesvvgvsgeeeeeegnnvsesgenennnnnnvvneenvvvnegsvvsennegengngnesenvnvnvseeeeegenvnnesengesvsenessegnvnvvngvneenvssgenegenngnnvgvgnvvseegsengvgnennvvnnvgnvvgvngnvngvvnnvsgeeenvnesvvnengenvsgvvvvvgsesvgnngvsvneegesegnessenesvnengesseeeeeesvnnvvngvnesgssenvsvvnessgsvsvssssvsesgesenvvgvvnvsvsvvseneeegeeeesesvnneennvnnegnneesgsssvvvsenvnengvssseennenngeengvnnnnvseegngvvvsvnvsvgssssgennvsesenesssesvnnnnnvgvsvvgnvsegssgesvgngesssvsessvssvgnenesgvnennvsvneenvsvvvgnvnnvseseeegnnnneegsennengennnvvnesvvvvnneesssgenvsgvgvvsvnvgnvvnvsgvgvsgvsvgnenneenvnnnesvvngvgnnessgseesvsssegegnesvgsvssvvssesgenvnnenvvnnesgssesseesssvnvneenvvsssgeesenenvneessvsenesvvnnnngvnvnnnvsssvssennvssvgvnvvngvnnvnnvnvvsvnneegnegnnnnnessssvvvsvnnennnnvvnessvsesenneneneesssenvnvssvsenvnesvnvvnvnngvgvvsgenvvvsvngessgenneenvvssegsgenvgvssessvsvgnnnvvsvsesenneseeeeenvvvnvsssssegesvsvsvsssgessvsvgsvnegsvsseenessgesvgvngegsgsvnvvnnvssvsvnnvgvsgsvnnengenvnvgsssesgvvnngvsvgssvnvnvgsvssvsessgeenesvssvnvngnnvnesssgvsesseeennenvvvsvngvsessvgneeeenenennnnenvvngesvngnnnegeegesvsegsegssvsvvssvvnnvneenenvvgvsvneegssvssvnenvseneneeeegesvsesenvnneeneenvsvvnvnnvnvvnesvvnnnesvnnenvgssssvngesenneeeenvvvsvnnnngvssgeesvvngenegsssvssvseesgvvgsgvsesssesssssessvsvsvnneennnvssessesenvssssesgennnennvgvseessssssvssgssseseeeegnengeseenneeeennvnvnvnnneeegess")
elf_4 = Elf([99,99], "vssvseessvvvnvsesvsssvnvvssssessvnenennnnvvvnvvsenvnesvvsseeeeegnvvvnesvnnnesvssvnvnenvsesenvvssenenenenvnnnvvgssesenvnvvvnvnvvsseeesesvseeesvvnnvvgsvssgssvsvvnneesenessgsesseeeseennnvssssvnessennenessvvnnvsvsennvvvvnnvseeneenvvsvvngenvvvsseesennnvnvvnegegeesvseesesvssesesvvsennneesvsenennenennvnvvsegnneneseseseessssvnenvnvvgvneenesennvvvnvnvvneseennenesennvnessvvsesvgssvsvvvssgenvvssvssvsvvvnvvnesesvnennvgvnvvneesvvsesesvsgsvvssseseneenenennvnnnvgnnennennneneeeenngeeeeseenvssvsvsssvsssvnenvseneennvvvseeeenenvssessssvsssessvvnvnvvnvnvsenesvnennennvvvsennvneseesvsssvngvnnneseneeeesessvsvvgsvsvsessvnvvsvsseeseennenvseegsenenvnessvnesssvnvngesssssesgvnesgvnnnesvnvnvvnnnvvvnenvssvvnnvvnvvvssenvsesvnnvgvsvssvvvvvnvsgesssennvnvgvsvvgvsvgnesesvnnneenesssvnenegessesvssesvnvnvvsesesesesenennvnnvnvnennvnvvvneeenvssvssengvvsssenegsennenneeseseesvvvvvnvvngennnnnenngngegnnnvvvseesgsgvnnnvvvgnvvnngeneessesgseesvvnngesssegesgssseessvgnenesesvvsgvvngvvsssvgvvsvgvvnvvsssssegessvvvvvseesvvnvgvsvvssssssvsenessvneessssesesvnesvnnvnvnvnnennenvsvnennnvvsvgvsengnvsegseeeeeegsseenvgvvseessssgeeesvnnenvvnenvsenesssseeeeenvssesvseeesenvvngvnennnesssseesgsegsvvsesvsvnenvvvgsesvsegsvnegenvvnvsgeennvgsvvsvvsvsvgnnvvnesvvvgngnneenenesengnnesvnvvsvvvnneegsvsseenneennnvssseennnvseneeneneenvnessegnegnvnnnnnenenennvnesvnneessvvseeseeneegsvnvsseeesvneenngnnvvvnvsessssvnvnvvnvsenvsenvnvvnvngvnvsvvsvvvseegnnesegssenvvssvsvgsennnngvvsssegsvvvgsssvvvnngeesvgnngnnvgnnvngneeeesennvgnesvgvsengneesgeseenvngnvvnvssenvvgnnegsvsgesssvssvnvvvgsvnegeeeenngnvgsvsesvvsssgsvnegennenvssvsgeeeseesesvvnvgsvngnvnvgneesenvseeesegesssengvvnvvvgvgseennesvvgnnvnnneesvnnngvssvssenesvvsessgegnvvvngneeneesennnvvsenvsvnvnesssvnesennngvsssvvneesvsvnnessvsgsvsesgsvnnvnennenvsenvvsvneeeennvvnneeegeesegsesvvsenvneseesgvssvsseesegnvssengvvsvsgseseneenneeenennessvsvsgvseesesvvvnvsgenesvvgnvvsvnneeeessvgvsesenenvvgnesvgvnesgeeeesgenvvsegeenvvsgenvsgvvsvvsvsenvnvnenegnvnneenesgsvnvsenegesvvseenvseennvsvngeesvvngneseenneeegseennnvseeeesesennnneenvvvsseessssgvnnenenvvvnnvvnvseneesesseeneesvnvvvneeeennngeeseengeennvnesvnvgvvnnvvvvsvsseenvvvvvvvnneeeeneessvvvsvvssvnenesvnnesvneneseeessenesvvvsessvnvsvvneeneenennnnnnnvvvsvvnnnvsvvngvvvnenvsvvssesenennvsvvnesssvsgvgvvvvsesenessvsgvnvvnvsvvvnnessvnenvnnvnnnnvvnnesgseengnnvsesgssvseeegeneesgssvnnvvgvseegnvgvvvnvsessvsenvnnenenngneessengnnessvgssessesssessvneeesvnnesssvgvneessvseegssvnesseeesvsvssvvsseenvnneesvnvnesssvnneseenvvsvsvsseneeessgsssvsesgvneenvsennvsenenennvsvseessvseesvneeessennvnvnvvnnnnvvgvvsenegneeeseeseeneneeesgeesenegsvnvngvvnenvsseegenvngvvnvnesvvsennvsenvseeenvseesgvsssseeesvgnnegnvnvvvnesvvvnvvvsesvgvssssvnnvvnvnvsgssenvvvvssvnnnvsse")

elves = [elf_1, elf_2, elf_3, elf_4]

for elf in elves:
    while True:
        if not elf.canMove():
            break
        elf.move() 

print(len(gloggPoints))


xs, ys = zip(*gloggPoints)
plt.plot(elf_1.points[0], elf_1.points[1])
plt.plot(elf_2.points[0], elf_2.points[1])
plt.plot(elf_3.points[0], elf_3.points[1])
plt.plot(elf_4.points[0], elf_4.points[1])
plt.scatter(xs, ys, edgecolors="yellow")
plt.show()